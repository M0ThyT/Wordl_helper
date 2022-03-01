#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:50:57 2022

@author: timothy
"""
#%%Run once
#load libraries
import pandas as pd
import numpy as np

from Remover import *
from Scorer import *
from Combiner import *

#load df
#df = pd.read_csv("wordle-allowed-guesses.txt", sep=" ", header=0, names = ['words']) #hard
df = pd.read_csv("wordle-answers-alphabetical.txt", sep = " ", header = 0, names = ['words']) #easy
#remove those words I already know are wrong (wrong length or numbers in them)
df = keep_only_rel_words(df)
#make a df that the rest of my functions expect
df = df_preparer(df) #issue, doesn't recognize the pd in the function


#%%Reset Dictionary
df_word = df #click this to reset the dictionary


#%%execute helper
df_word = tried_word(df_word) #click this to enter info on new word
