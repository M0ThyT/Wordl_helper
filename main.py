#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:50:57 2022

@author: timothy
"""
import pandas as pd
import numpy as np
import Scorer
df = pd.read_csv("/home/timothy/Downloads/words.txt", sep=" ")


def word_preparer(df = df):
    df.rename(columns={'2': 'Word'}, inplace=True)
    #replace non aplphabetic values
    df['Word'] = df.Word.str.replace('[^a-zA-Z]', '')
    #make lowercase
    df['Word'] = df['Word'].str.lower()
    #only keep 5 letter words
    rel_words = df[df['Word'].str.len() == 5]
    #drop duplicates
    rel_words = rel_words.drop_duplicates()
    
    return(rel_words)

rel_words = word_preparer()

df = scorer(rel_words)

#in how many words does a certain letter appear, that should be the weight (fraction of words with the letter)
#turn every word into a set and determin how many sets have a letter


