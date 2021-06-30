#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:50:47 2021.

@author: tristan
"""

import os
from pathlib import Path

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from imblearn.combine import SMOTETomek

import nltk
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

# %%
# Just to check.
nltk.download('stopwords')

path_chall3 = Path(os.environ['CTF_CHALL3'])
os.chdir(path_chall3)

# Importing datasets.
df_comments = pd.read_csv('comments.csv')[['Auteur', 'Commentaire']]
df_sus = pd.read_csv('sus.csv')

# Creating working dataset.
df = pd.concat([df_comments, df_sus])
df.loc[df['Auteur'] != 'SUS', 'Auteur'] = 'Autre'

# %%
# Stop words.
stop_words = stopwords.words("english")

# Stemmer.
stemmer = SnowballStemmer('english')

# Declaring the vectorizer
vectorizer = TfidfVectorizer(stop_words=stop_words).build_analyzer()
stem_vectorizer = TfidfVectorizer(analyzer=lambda doc: (stemmer.stem(w) for w in vectorizer(doc)))

# Creating the training dataset
train = pd.DataFrame(stem_vectorizer.fit_transform(df['Commentaire']).toarray(), columns=stem_vectorizer.get_feature_names())
y = df['Auteur']

# Rebalencing the dataset.
# The SUS category is absolutly negligable and in theory it should be imperative to rebalence the dataset.
# As of now it still works fine without doing that and I don't know why.
# If I can figure out why I will be able to make it a little harder.
se = SMOTETomek(random_state=42)
train, y = se.fit_resample(train, df['Auteur'])

# Training
clf = LogisticRegression(C=1, class_weight='balanced').fit(train, y)

lst_sus = clf.predict(stem_vectorizer.transform(df_sus['Commentaire']))
lst_com = clf.predict(stem_vectorizer.transform(df_comments['Commentaire']))

print('\n')
print(lst_sus)
print("We can see that every SUS message is indeed classified as such.\n")
print(sum([elt == 'SUS' for elt in lst_com]))
print("We can see that none of the other 4500 messages are classified as SUS.\n")

print("Prediction on the phrase : 'I like drugs'")
print(clf.predict(stem_vectorizer.transform(['I like drugs'])))
print("\nPrediction on the phrase : 'I like spaghetti'")
print(clf.predict(stem_vectorizer.transform(['I like spaghetti'])))

