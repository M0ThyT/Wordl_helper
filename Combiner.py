#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 14:09:29 2022

@author: timothy
"""
import pandas as pd
import numpy as np
from Remover import *
from Scorer import *

def tried_word(df):
    print('please input the word')
    word = input()
    if len(word) !=5: 
        print('Error, incorrect word')
    i = 0
    for elm in word: 
        i +=1
        print(f'------------------------Letter Number {i}:{elm}------------------------')
        print('1 letter not in word')
        print('2 letter in wrong position')
        print('3 letter in correct position')
        answer = input()
        answer = int(answer)
        if answer == 1: 
            print('Thanks for indicating that the letter does not exist in the word')
            df = letter_not_in_word(df, elm)
        elif answer == 2: 
            print('Thanks for indicating that the letter is in the wrong position')
            df = letter_not_in_position(df, elm, i)
            df = letter_in_word(df, elm)
        elif answer == 3: 
            print('Thanks for indicating the letter is in the right position')
            df = letter_in_position(df, elm, i)
        else: 
            print('error, wrong input. Please go again.')
        
     
    #score and rearange the new df
    df = scorer(df)
    df.reset_index(inplace = True)
    print('The best next words are:')
    print(df.Word.head(10)) 
    
    return(df)
