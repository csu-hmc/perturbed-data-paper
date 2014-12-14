#!/usr/bin/env python

import os
from collections import defaultdict

import numpy as np
import pandas as pd

import utils

print('Generating subject table.')

script_path = os.path.realpath(__file__)
src_dir = os.path.dirname(script_path)
root_dir = os.path.realpath(os.path.join(src_dir, '..'))
raw_dir, processed_dir = utils.config_paths(root_dir)

tables = utils.generate_meta_data_tables(raw_dir)

subject_df = tables['TOP|subject']

for trial in ['001', '002']:
    if trial in subject_df.index:
        subject_df = subject_df.drop(trial)

# Create columns for each speed that contain a list of the
for_group = subject_df.copy()
for_group['Speed'] = tables['TOP|trial']['nominal-speed']
grouped_by_id_speed = for_group.groupby(['id', 'Speed'])

index = defaultdict(list)
trials_per = defaultdict(list)
for (subject_id, speed), trial_ids in grouped_by_id_speed.groups.items():
    index[speed].append(subject_id)
    trials_per[speed].append(', '.join([t.lstrip("0") for t in trial_ids]))

unique_subjects = subject_df.drop_duplicates()
unique_subjects.index = unique_subjects['id']

for speed, trials in trials_per.items():
    speed_key = '{:1.1f} m/s'.format(speed)
    unique_subjects[speed_key] = pd.Series(trials, index[speed])

unique_subjects.rename(columns={'mass': 'self-reported mass'}, inplace=True)

cols = ['id', 'gender', 'age', 'height', 'self-reported mass', '0.8 m/s',
        '1.2 m/s', '1.6 m/s']
units = ['', '', ' [yr]', ' [m]', ' [kg]', '', '', '']
new_cols = [s.capitalize() + u for s, u in zip(cols, units)]
unique_subjects.rename(columns=dict(zip(cols, new_cols)), inplace=True)

formatters = {'Height [m]': lambda x: 'NA' if np.isnan(x)
              else '{:0.2f}'.format(x),
              'Self-reported mass [kg]': lambda x: 'NA' if np.isnan(x)
              else '{:0.0f}'.format(x)}

unique_subjects = unique_subjects.drop_duplicates()
unique_subjects = unique_subjects.drop(0)  # remove null subject

measured = utils.measured_subject_mass(raw_dir, processed_dir)


def format_sigma(x):
    if x[1] >= 1.0:
        return 'dollar{:0.0f}plusminus{:0.0f}dollar'.format(*x)
    else:
        return 'dollar{:0.1f}plusminus{:0.1f}dollar'.format(*x)

measured['Measured Mass [kg]'] = zip(measured['Measured Mass'],
                                     measured['Standard Deviation'])
measured['Measured Mass [kg]'] = \
    measured['Measured Mass [kg]'].map(format_sigma)

unique_subjects['Measured Mass [kg]'] = measured['Measured Mass [kg]']
new_cols.insert(4, 'Measured Mass [kg]')

table_dir = os.path.join(root_dir, 'tables')
if not os.path.exists(table_dir):
    os.makedirs(table_dir)

table_path = os.path.join(table_dir, 'subjects.tex')
tex = unique_subjects.sort().to_latex(na_rep='NA', index=False,
                                      columns=new_cols,
                                      formatters=formatters)
tex = tex.replace('dollar', '$')
tex = tex.replace('plusminus', '\pm')
tex = tex.replace('rlrrlrlll', 'rlrrrrlll')
with open(table_path, 'w') as f:
    f.write(tex)
print('Table at: {}'.format(table_path))
