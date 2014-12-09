#!/usr/bin/env python

import os

import yaml
from numpy import rad2deg
from scipy.constants import golden
import matplotlib.pyplot as plt
import pandas
from gaitanalysis.utils import _percent_formatter
import seaborn as sbn

from utils import trial_file_paths, load_data, remove_bad_gait_cycles


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
    one = remove_bad_gait_cycles(unperturbed_gait_data_1, 1.18, 1.22,
                                 'Average Belt Speed')
    two = remove_bad_gait_cycles(unperturbed_gait_data_2, 1.18, 1.22,
                                 'Average Belt Speed')
    unperturbed_gait_cycles = pandas.concat((one[0], two[0]),
                                            ignore_index=True)
    unperturbed_gait_cycle_stats = pandas.concat((one[1], two[1]),
                                                 ignore_index=True)

    perturbed_gait_data = load_data('Longitudinal Perturbation', paths, tmp)

    # Time series comparison plot.
    num_unperturbed_cycles = unperturbed_gait_cycles.shape[0]
    num_perturbed_cycles = perturbed_gait_data.gait_cycles.shape[0]

    mean_of_perturbed = perturbed_gait_data.gait_cycles.mean(axis='items')
    std_of_perturbed = perturbed_gait_data.gait_cycles.std(axis='items')

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

                sigma_mul = 3.0

                pmean = con[i](mean_of_perturbed[col_name])
                pstd = sigma_mul * con[i](std_of_perturbed[col_name])

                umean = con[i](mean_of_unperturbed[col_name])
                ustd = sigma_mul * con[i](std_of_unperturbed[col_name])

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
                            label=side + ' Perturbed, N = {}'.format(num_perturbed_cycles))
                row[i].plot(upercent, umean.values, linetype, color=purple,
                            label=side + ' Unperturbed, N = {}'.format(num_unperturbed_cycles))

    plt.subplots_adjust(top=0.85)

    axes[0, 0].set_title('Joint Angles [deg]')
    axes[0, 1].set_title('Joint Torques [Nm]')
    axes[-1, 0].xaxis.set_major_formatter(_percent_formatter)
    axes[-1, 1].xaxis.set_major_formatter(_percent_formatter)
    axes[-1, 0].set_xlabel('Percent Right Gait Cycle')
    axes[-1, 1].set_xlabel('Percent Right Gait Cycle')
    axes[0, 0].legend(loc='upper left', ncol=2, bbox_to_anchor=(0.15, 1.75))

    if not os.path.exists('../figures'):
        os.makedirs('../figures')

    fig.savefig('../figures/unperturbed-perturbed-comparison.pdf')

    # Boxplots comparing the gait cycle stats. The figure will have three
    # pairs of boxplots for the belt speed, stride frequency, and stride
    # length.

    fig, axes = plt.subplots(1, 3)

    columns = ['Average Belt Speed', 'Stride Frequency', 'Stride Length']
    units = ['[m/s]', '[Hz]', '[m]']

    for col, ax, unit in zip(columns, axes.flatten(), units):
        ax.set_title('{} {}'.format(col, unit))
        u = unperturbed_gait_cycle_stats[col]
        p = perturbed_gait_data.gait_cycle_stats[col]
        sbn.boxplot([p.values, u.values], ax=ax, color=[blue, purple],
                    names=['Perturbed\nN = {}'.format(num_perturbed_cycles),
                           'Unperturbed\nN = {}'.format(num_unperturbed_cycles)])

    plt.tight_layout()
    plt.savefig('../figures/unperturbed-perturbed-boxplot-comparison.pdf')
