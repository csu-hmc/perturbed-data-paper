#!/usr/bin/env python

"""This script generates the subject table in the paper by parsing the meta
data."""

import os
from collections import defaultdict

import numpy as np
import pandas as pd

import utils

print('Generating subject table.')

# This just returns absolute paths to the all the necessary files and
# directories.
script_path = os.path.realpath(__file__)
src_dir = os.path.dirname(script_path)
root_dir = os.path.realpath(os.path.join(src_dir, '..'))
raw_dir, processed_dir = utils.config_paths(root_dir)

tables = utils.generate_meta_data_tables(raw_dir)

subject_df = tables['TOP|subject']

for trial in ['001', '002']:
    if trial in subject_df.index:
        subject_df = subject_df.drop(trial)

# Create columns for each speed that contain a list of the trial numbers at
# that speed for that subject.
for_group = subject_df.copy()
for_group['Speed'] = tables['TOP|trial']['nominal-speed']
grouped_by_id_speed = for_group.groupby(['id', 'Speed'])

index = defaultdict(list)
trials_per = defaultdict(list)
for (subject_id, speed), trial_ids in grouped_by_id_speed.groups.items():
    index[speed].append(subject_id)
    trials_per[speed].append(', '.join([t.lstrip("0") for t in trial_ids]))

# This reduces down to individual subjects indexed by id.
unique_subjects = subject_df.drop_duplicates()
unique_subjects.index = unique_subjects['id'].astype(int)

for speed, trials in trials_per.items():
    speed_key = '{:1.1f} m/s'.format(speed)
    unique_subjects[speed_key] = pd.Series(trials, index[speed])

unique_subjects.rename(columns={'mass': 'self-reported mass'}, inplace=True)

unique_subjects = unique_subjects.drop_duplicates()
subject_zero_trials = unique_subjects.loc[0, :][['0.8 m/s', '1.2 m/s', '1.6 m/s']]  # trial lists for subject 0
unique_subjects = unique_subjects.drop(0)  # remove null subject

# This computes the measured value of the mass from force plate data from
# each trial.
measured = utils.measured_subject_mass(raw_dir, processed_dir)

# The following formats the measured masses into 50.0+\-0.1.

def format_sigma(x):
    if x[1] >= 1.0:
        return 'dollar{:0.0f}plusminus{:0.0f}dollar'.format(*x)
    else:
        return 'dollar{:0.1f}plusminus{:0.1f}dollar'.format(*x)

measured['Mass'] = zip(measured['Mean Measured Mass'],
                       measured['Measured Mass Std. Dev.'])
measured['Mass'] = measured['Mass'].map(format_sigma)

unique_subjects['mass'] = measured['Mass']

# for each subject who has an NA for the measured mass, replace that with
# the self reported mass and an asterik
na_idx = unique_subjects['mass'].isnull()
unique_subjects['mass'][na_idx] = unique_subjects['self-reported mass'][na_idx]

# Make nicer column names.
cols = ['id', 'gender', 'age', 'height', 'mass', '0.8 m/s', '1.2 m/s',
        '1.6 m/s']
units = ['', '', ' [yr]', ' [m]', ' [kg]', '', '', '']
new_cols = [s.capitalize() + u for s, u in zip(cols, units)]
unique_subjects.rename(columns=dict(zip(cols, new_cols)), inplace=True)


formatters = {'Height [m]': lambda x: 'NA' if np.isnan(x)
              else '{:0.2f}'.format(x),
              'Mass [kg]': lambda x: '{:0.0f}'.format(x) if isinstance(x, float) else x}

table_dir = os.path.join(root_dir, 'tables')
if not os.path.exists(table_dir):
    os.makedirs(table_dir)

table_path = os.path.join(table_dir, 'subjects.tex')
tex = unique_subjects.sort('1.6 m/s', na_position='first').to_latex(
    na_rep='NA', index=False, columns=new_cols, formatters=formatters)

tex = tex.replace('dollar', '$')
tex = tex.replace('plusminus', '\pm')
tex = tex.replace('rlrrllll', 'rlrrrrrr')
lines = tex.split('\n')
lines.insert(5, r'\midrule[0.25pt]')
lines.insert(9, r'\midrule[0.25pt]')
tex = '\n'.join(lines)
with open(table_path, 'w') as f:
    f.write(tex)
print('Table at: {}'.format(table_path))

# This creates a table of the calibration trials.
table = (r'\begin{tabular}{rr}' '\n'
          r'\toprule' '\n'
          r'Speed & Trial Numbers \\' '\n'
          r'\midrule' '\n')
for i, trials in enumerate(subject_zero_trials):
    speed = subject_zero_trials.index[i]
    table += r'{} & {} \\'.format(speed, trials)
    table += '\n'
table += (r'\bottomrule' '\n' r'\end{tabular}')

table_path = os.path.join(table_dir, 'compensation_trials.tex')

with open(table_path, 'w') as f:
    f.write(table)

print('Table at: {}'.format(table_path))
