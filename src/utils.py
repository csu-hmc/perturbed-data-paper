#!/usr/bin/env python

import os
from collections import defaultdict

import yaml
import numpy as np
import pandas as pd
from gaitanalysis.motek import DFlowData, markers_for_2D_inverse_dynamics
from gaitanalysis.gait import GaitData


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
    into a GaitData object.

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
    gait_data : gaitanalysis.gait.GaitData
        The GaitData instance containing the data for the event.

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
        gait_data = GaitData(perturbed_df)
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
        gait_data = GaitData(tmp_data_path)

    return gait_data


def remove_bad_gait_cycles(gait_data, lower, upper, col):
    """Returns the gait cycles with outliers removed based on the
    gait_cycle_stats DataFrame column.

    Parameters
    ==========
    gait_data : gaitanalysis.gait.GaitData
        The data object containing both the gait_cycles Panel and
        gait_cycle_stats DataFrame.
    lower : int or float
        The lower bound for the gait_cycle_stats histogram.
    upper : int or float
        The upper bound for the gait_cycle_stats histogram.
    col : string
        The column in gait_cycle_stats to use for the bounding.

    Returns
    =======
    gait_cycles : Panel
        A reduced Panel of gait cycles.
    gait_cycle_data : DataFrame
        A reduced DataFrame of gait cycle data.

    """

    valid = gait_data.gait_cycle_stats[col] < upper
    lower_values = gait_data.gait_cycle_stats[valid]
    valid = lower_values[col] > lower
    mid_values = lower_values[valid]

    return gait_data.gait_cycles.iloc[mid_values.index], mid_values


def generate_meta_data_tables(trials_dir, top_level_key='TOP', key_sep='|'):
    """Returns a dictionary of Pandas data frames, each one representing a
    level in the nested meta data. The data frames are indexed by the trial
    identification number.

    Parameters
    ----------
    trials_dir : string
        The path to a directory that contains trial directories.

    Returns
    -------
    tables : dictionary of pandas.Dataframe
        The meta data tables indexed by trial identification number.

    """

    def walk_dict(d, key='TOP', key_sep='|'):
        """Returns a dictionary of recursively extracted dictionaries."""
        dicts = {}
        e = {}
        for k, v in d.items():
            if isinstance(v, dict):
                dicts.update(walk_dict(v, key + key_sep + k))
            else:
                e[k] = v
                dicts[key] = e
        return dicts

    # TODO : The check for the 'T' doesn't work if the directory from
    # os.walk is too short.
    trial_dirs = [x[0] for x in os.walk(trials_dir) if x[0][-4] == 'T']

    trial_nums = [x[-3:] for x in trial_dirs]

    all_flattened_meta_data = {}

    tables = {}

    for directory, trial_num in zip(trial_dirs, trial_nums):
        path = os.path.join(directory, 'meta-{}.yml'.format(trial_num))
        try:
            f = open(path)
        except IOError:
            print('No meta file in {}'.format(directory))
            pass
        else:
            meta_data = yaml.load(f)
            flattened_dict = walk_dict(meta_data, top_level_key, key_sep)
            all_flattened_meta_data[trial_num] = flattened_dict
            for table_name, table_row_dict in flattened_dict.items():
                if table_name not in tables.keys():
                    tables[table_name] = defaultdict(lambda: len(trial_nums)
                                                     * [np.nan])

    ordered_trial_nums = sorted(trial_nums)

    for trial_num, flat_dict in all_flattened_meta_data.items():
        trial_idx = ordered_trial_nums.index(trial_num)
        for table_name, table_row_dict in flat_dict.items():
            for col_name, row_val in table_row_dict.items():
                tables[table_name][col_name][trial_idx] = row_val

    for k, v in tables.items():
        tables[k] = pd.DataFrame(v, index=ordered_trial_nums)

    return tables
