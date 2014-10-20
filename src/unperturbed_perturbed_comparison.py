#!/usr/bin/env python

import os
import random

import yaml
from numpy import rad2deg
from scipy.constants import golden
import matplotlib.pyplot as plt
import pandas
from gaitanalysis.motek import DFlowData, markers_for_2D_inverse_dynamics
from gaitanalysis.gait import WalkingData
from gaitanalysis.utils import _percent_formatter
import seaborn as sbn


def trial_file_paths(trials_dir, trial_number):
    """Returns the most common paths to the trials in the gait
    identification data set.

    Parameters
    ==========
    trials_dir : string
        The path to the main directory for the data. This directory should
        contain subdirectories: `T001/`, `T002/`, etc.
    trial_number : string
        Three digit trial number, e.g. `005`.

    """

    trial_dir = 'T' + trial_number
    mocap_file = 'mocap-' + trial_number + '.txt'
    record_file = 'record-' + trial_number + '.txt'
    meta_file = 'meta-' + trial_number + '.yml'

    mocap_file_path = os.path.join(trials_dir, trial_dir, mocap_file)
    record_file_path = os.path.join(trials_dir, trial_dir, record_file)
    meta_file_path = os.path.join(trials_dir, trial_dir, meta_file)

    return mocap_file_path, record_file_path, meta_file_path


def load_data(event, paths, tmp):
    """Loads an event and processes the data, if necessary, from a trial
    into a WalkingData object.

    Parameters
    ==========
    event : string
        A valid event for the given trial.
    paths : list of strings
        The paths to the mocap, record, and meta data files.
    tmp : string
        A path to a temporary directory in which the processed data can be
        stored.

    Returns
    =======
    gait_data : gaitanalysis.gait.WalkingData
        The WalkingData instance containing the data for the event.

    """

    file_name = '_'.join([n.lower() for n in event.split(' ')]) + '.h5'

    tmp_data_path = os.path.join(tmp, file_name)

    try:
        f = open(tmp_data_path, 'r')
    except IOError:
        print('Cleaning and processing {} data...'.format(event))
        # Load raw data, clean it up, and extract the perturbation section.
        dflow_data = DFlowData(*paths)
        dflow_data.clean_data(ignore_hbm=True)
        perturbed_df = \
            dflow_data.extract_processed_data(event=event,
                                              index_col='TimeStamp',
                                              isb_coordinates=True)

        # Compute the lower limb 2D inverse dynamics, identify right heel
        # strike times, and split the data into gait cycles.
        gait_data = WalkingData(perturbed_df)
        marker_set = dflow_data.meta['trial']['marker-set']
        subject_mass = dflow_data.meta['subject']['mass']
        labels = markers_for_2D_inverse_dynamics(marker_set)
        args = list(labels) + [subject_mass, 6.0]
        gait_data.inverse_dynamics_2d(*args)
        gait_data.grf_landmarks('FP2.ForY', 'FP1.ForY',
                                filter_frequency=10.0,
                                threshold=27.0)
        gait_data.split_at('right', num_samples=80,
                           belt_speed_column='RightBeltSpeed')
        if not os.path.exists(tmp):
            os.makedirs(tmp)
        gait_data.save(tmp_data_path)
    else:
        print('Loading processed {} data from file...'.format(event))
        f.close()
        gait_data = WalkingData(tmp_data_path)

    return gait_data


def remove_bad_steps(gait_data, lower, upper, col):
    """Returns the gait cycles with outliers removed based on the step_data
    DataFrame column.

    Parameters
    ==========
    gait_data : gaitanalysis.gait.WalkingData
        The data object containing both the steps Panel and step_data
        DataFrame.
    lower : int or float
        The lower bound for the step_data histogram.
    upper : int or float
        The upper bound for the step_data histogram.
    col : string
        The column in step_data to use for the bounding.

    Returns
    =======
    gait_cycles : Panel
        A reduced Panel of gait cycles.
    gait_cycle_data : DataFrame
        A reduced DataFrame of gait cycle data.

    """

    valid = gait_data.step_data[col] < upper
    lower_values = gait_data.step_data[valid]
    valid = lower_values[col] > lower
    mid_values = lower_values[valid]

    return gait_data.steps.iloc[mid_values.index], mid_values


if __name__ == '__main__':

    params = {'backend': 'ps',
              'axes.labelsize': 8,
              'axes.titlesize': 10,
              'text.fontsize': 10,
              'legend.fontsize': 8,
              'xtick.labelsize': 8,
              'ytick.labelsize': 8,
              'text.usetex': True,
              'font.family': 'serif',
              'font.serif': ['Computer Modern'],
              'figure.figsize': (6.0, 6.0 / golden),
             }
    plt.rcParams.update(params)

    trial_number = '020'

    with open('config.yml', 'r') as f:
        config = yaml.load(f)

    root = config['root_data_directory']
    paths = trial_file_paths(root, trial_number)

    tmp = config['tmp_data_directory']

    unperturbed_gait_data_1 = load_data('First Normal Walking', paths, tmp)
    unperturbed_gait_data_2 = load_data('Second Normal Walking', paths, tmp)
    one = remove_bad_steps(unperturbed_gait_data_1, 1.18, 1.22,
                           'Average Belt Speed')
    two = remove_bad_steps(unperturbed_gait_data_2, 1.18, 1.22,
                           'Average Belt Speed')
    unperturbed_gait_cycles = pandas.concat((one[0], two[0]),
                                            ignore_index=True)
    unperturbed_step_data = pandas.concat((one[1], two[1]),
                                          ignore_index=True)

    perturbed_gait_data = load_data('Longitudinal Perturbation', paths, tmp)

    # Time series comparison plot.
    num_steps = unperturbed_gait_cycles.shape[0]

    idxs = random.sample(range(perturbed_gait_data.steps.shape[0]), num_steps)

    mean_of_perturbed = perturbed_gait_data.steps.iloc[idxs].mean(axis='items')
    std_of_perturbed = perturbed_gait_data.steps.iloc[idxs].std(axis='items')

    mean_of_unperturbed = unperturbed_gait_cycles.mean(axis='items')
    std_of_unperturbed = unperturbed_gait_cycles.std(axis='items')

    angles = ['Ankle.PlantarFlexion.Angle',
              'Knee.Flexion.Angle',
              'Hip.Flexion.Angle']

    torques = ['Ankle.PlantarFlexion.Moment',
               'Knee.Flexion.Moment',
               'Hip.Flexion.Moment']

    y_labels = ['Ankle Plantar Flexion',
                'Knee Flexion',
                'Hip Flexion']

    fig, axes = plt.subplots(3, 2, sharex=True)

    blue = sbn.xkcd_rgb['windows blue']
    purple = sbn.xkcd_rgb['dusty purple']

    ppercent = mean_of_perturbed.index.values.astype(float)
    upercent = mean_of_unperturbed['Percent Gait Cycle']

    con = [lambda x: rad2deg(x), lambda x: x]

    for row, angle, torque, y_label in zip(axes, angles, torques, y_labels):
        for side, linetype in zip(['Right', 'Left'], ['-', '--']):

            row[0].set_ylabel(y_label)

            for i, col in enumerate([angle, torque]):

                col_name = side + '.' + col

                pmean = con[i](mean_of_perturbed[col_name])
                pstd = 2.0 * con[i](std_of_perturbed[col_name])

                umean = con[i](mean_of_unperturbed[col_name])
                ustd = 2.0 * con[i](std_of_unperturbed[col_name])

                row[i].fill_between(ppercent,
                                    (pmean - pstd).values,
                                    (pmean + pstd).values,
                                    alpha=0.25,
                                    color=blue,
                                    label='_nolegend_')

                row[i].fill_between(upercent,
                                    (umean - ustd).values,
                                    (umean + ustd).values,
                                    alpha=0.40,
                                    color=purple,
                                    label='_nolegend_')

                row[i].plot(ppercent, pmean.values, linetype, color=blue,
                            label=side + ' Perturbed')
                row[i].plot(upercent, umean.values, linetype, color=purple,
                            label=side + ' Un-perturbed')

    plt.subplots_adjust(top=0.85)

    axes[0, 0].set_title('Joint Angles [deg]')
    axes[0, 1].set_title('Joint Torques [Nm]')
    axes[-1, 0].xaxis.set_major_formatter(_percent_formatter)
    axes[-1, 1].xaxis.set_major_formatter(_percent_formatter)
    axes[-1, 0].set_xlabel('Percent Right Gait Cycle')
    axes[-1, 1].set_xlabel('Percent Right Gait Cycle')
    axes[0, 0].legend(loc='upper left', ncol=2, bbox_to_anchor=(0.4, 1.75))

    if not os.path.exists('../figures'):
        os.makedirs('../figures')

    fig.savefig('../figures/unperturbed-perturbed-comparison.pdf')

    # Step data histogram comparisons.
    columns = ['Average Belt Speed', 'Cadence', 'Step Duration',
               'Stride Length']
    units = ['[m/s]', '[Hz]', '[s]', '[m]']
    axes = perturbed_gait_data.step_data.iloc[idxs].hist(column=columns,
                                                         color=blue)
    for i, ax in enumerate(axes.flatten()):
        ax = unperturbed_step_data[columns[i]].hist(ax=ax, color=purple)
        ax.set_title(columns[i] + ' ' + units[i])

    plt.savefig('../figures/unperturbed-perturbed-hist-comparison.pdf')
