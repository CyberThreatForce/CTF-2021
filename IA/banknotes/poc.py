#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 14:40:45 2021.

@author: tristantacule
"""

import os

from collections import defaultdict
from pathlib import Path

import pandas as pd

from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import confusion_matrix


# %%
# Path for the csv files.
str_path = Path(os.environ['CTF_CHALL1'])

# Read the files, df_train contains labels i.e. if the bill is fake or not, df_test does not contain this information.
df_train = pd.read_csv(str_path / 'bank_notes.csv')
df_test = pd.read_csv(str_path / 'notes_to_test.csv')

str_target = 'is_genuine'
lst_features = [elt for elt in df_train.columns if elt not in [str_target, 'num_serie']]

# %%
# Scale variable, important for logisitic regression.
scaler = defaultdict(RobustScaler)

for var in lst_features:
    # The scaler is fitted on the train and used on the train and the test.
    df_train.loc[:, var] = scaler[var].fit_transform(df_train[var].values.reshape(-1, 1))
    df_test.loc[:, var] = scaler[var].transform(df_test[var].values.reshape(-1, 1))

# %%
# Reglog is enough.
logreg = LogisticRegressionCV(solver='liblinear', penalty='l1', max_iter=100)
logreg.fit(df_train[lst_features], df_train['is_genuine'])

df_test['preds'] = logreg.predict(df_test[lst_features])

# print(confusion_matrix(df_test['is_genuine'], df_test['preds']))

# The flag is contained in the serial numbers of the bills.
res = ''.join(df_test.loc[~df_test['preds'], 'num_serie'].str.replace(r'\d', '').values).upper()

print(f'\nFlag :\n {res}')
