#!/usr/bin/env python

# standard library
import os
from collections import defaultdict

# external
import yaml
import numpy as np
import pandas as pd
from gaitanalysis.motek import DFlowData, markers_for_2D_inverse_dynamics
from gaitanalysis.gait import GaitData


def config_paths(root_dir):
    """Returns the full path to the directories specified in the config.yml
    file.

    Parameters
    ----------
    root_dir : string
        Absolute path to the root directory of the repository.

    Returns
    -------
    raw_dir : string
        Absolute path to the raw data directory.
    processed_dir : string
        Absolute path to the processed data directory.

    """

    with open(os.path.join(root_dir, 'config.yml'), 'r') as f:
        config = yaml.load(f)

    raw_dir = os.path.join(root_dir, config['raw_data_dir'])
    processed_dir = os.path.join(root_dir, config['processed_data_dir'])

    return raw_dir, processed_dir


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


def measured_subject_mass(raw_data_dir, processed_data_dir):
    """This script computes the mean mass of each subject based on the force
    plate data collected just after the calibration pose. It also compares
    it to the mass provided by the subject. Some subjects may have invalid
    measurements and will not be included, so you should make use of the
    self reported mass.

    Parameters
    ----------
    raw_data_dir : string
        The path to the raw data directory.
    processed_data_dir : string
        The path to the processed data directory.

    Returns
    -------
    mean : pandas.DataFrame
        A data frame containing columns with mean/std measured mass, the
        self reported mass, and indexed by subject id.

    """

    # Subject 0 is for the null subject. For subject 1 we use the self
    # reported value because there is no "Calibration Pose" event. For
    # subject 11 and subject 4, we use the self reported mass because the
    # wooden feet were in place and the force measurements are
    # untrust-worthy.
    subj_with_invalid_meas = [0, 1, 4, 11]

    # Some of the trials have anomalies in the data after the calibration
    # pose due to the subjects' movement. The following gives best estimates
    # of the sections of the event that are suitable to use in the subjects'
    # mass computation. The entire time series during the "Calibration Pose"
    # event is acceptable for trials not listed.
    time_sections = {'020': (None, 14.0),
                     '021': (None, 14.0),
                     '031': (-14.0, None),
                     '047': (None, 12.0),
                     '048': (None, 7.0),
                     '055': (-12.0, None),
                     '056': (-3.0, None),  # also the first 2 seconds are good
                     '057': (-8.0, None),
                     '063': (None, 6.0),  # also the last 6 seconds are good
                     '069': (None, 14.0),
                     '078': (None, 15.0)}

    trial_dirs = [x[0] for x in os.walk(raw_data_dir) if x[0][-4] == 'T']
    trial_nums = [x[-3:] for x in trial_dirs if x[-3:] not in ['001', '002']]

    event = 'Calibration Pose'

    tmp_file_name = '_'.join(event.lower().split(' ')) + '.h5'
    tmp_data_path = os.path.join(processed_data_dir, tmp_file_name)

    subject_data = defaultdict(list)

    for trial_number in trial_nums:

        dflow_data = DFlowData(*trial_file_paths(raw_data_dir,
                                                 trial_number))

        subject_id = dflow_data.meta['subject']['id']

        if subject_id not in subj_with_invalid_meas:

            msg = 'Computing Mass for Trial #{}, Subject #{}'
            print(msg.format(trial_number, subject_id))
            print('=' * len(msg))

            try:
                f = open(tmp_data_path, 'r')
                df = pd.read_hdf(tmp_data_path, 'T' + trial_number)
            except (IOError, KeyError):
                print('Loading raw data files and cleaning...')
                dflow_data.clean_data(ignore_hbm=True)
                df = dflow_data.extract_processed_data(event=event,
                                                       index_col='TimeStamp',
                                                       isb_coordinates=True)
                df.to_hdf(tmp_data_path, 'T' + trial_number)
            else:
                msg = 'Loading preprocessed {} data from file...'
                print(msg.format(event))
                f.close()

            # This is the time varying mass during the calibration pose.
            df['Mass'] = (df['FP1.ForY'] + df['FP1.ForY']) / 9.81

            # This sets the slice indices so that only the portion of the
            # time series with valid data is used to compute the mass.
            if trial_number in time_sections:
                start = time_sections[trial_number][0]
                stop = time_sections[trial_number][1]
                if start is None:
                    stop = df.index[0] + stop
                elif stop is None:
                    start = df.index[-1] + start
            else:
                start = None
                stop = None

            valid = df['Mass'].loc[start:stop]

            actual_mass = valid.mean()
            std = valid.std()

            reported_mass = dflow_data.meta['subject']['mass']

            subject_data['Trial Number'].append(trial_number)
            subject_data['Subject ID'].append(dflow_data.meta['subject']['id'])
            subject_data['Reported Mass'].append(reported_mass)
            subject_data['Measured Mass'].append(actual_mass)
            subject_data['Standard Deviation'].append(std)
            subject_data['Gender'].append(dflow_data.meta['subject']['gender'])

            print("Measured mass: {} kg".format(actual_mass))
            print("Self reported mass: {} kg".format(reported_mass))
            print("\n")

        else:

            pass

    subject_df = pd.DataFrame(subject_data)

    grouped = subject_df.groupby('Subject ID')

    mean = grouped.mean()

    mean['Diff'] = mean['Measured Mass'] - mean['Reported Mass']

    # This sets the grouped standard deviation to the correct value
    # following uncertainty propagation for the mean function.

    def uncert(x):
        return np.sqrt(np.sum(x**2) / len(x))

    mean['Standard Deviation'] = grouped.agg({'Standard Deviation': uncert})

    return mean


def smooth(x, window_len=11, window='flat'):
    """Smooth the data using a window with requested size.

    This method is based on the convolution of a scaled window with the
    signal.  The signal is prepared by introducing reflected copies of the
    signal (with the window size) in both ends so that transient parts are
    minimized in the begining and end part of the output signal.

    Parameters
    ----------
    x: the input signal
    window_len: the dimension of the smoothing window; should be an odd
    integer
    window: the type of window from 'flat', 'hanning', 'hamming',
    'bartlett', 'blackman' flat window will produce a moving average
    smoothing.

    Returns
    -------
    output:
        the smoothed signal

    Examples
    --------

    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)

    See also
    --------

    numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman,
    numpy.convolve scipy.signal.lfilter

    """

    if x.ndim != 1:
        raise ValueError("smooth only accepts 1 dimension arrays.")

    if x.size < window_len:
        raise ValueError("Input vector needs to be bigger than window size.")

    if window_len < 3:
        return x

    if window not in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError("Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")

    s = np.r_[x[window_len - 1:0:-1], x, x[-1:-window_len:-1]]
    if window == 'flat':  # moving average
        w = np.ones(window_len, 'd')
    else:
        w = eval('np.' + window + '(window_len)')

    y = np.convolve(w/w.sum(), s, mode='valid')
    return y[(window_len / 2 - 1):-(window_len / 2)]
