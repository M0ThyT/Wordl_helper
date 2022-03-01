#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:45:42 2022

@author: timothy
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 22:02:49 2022

@author: timothy
"""
#import pandas as pd
#df = pd.read_csv("/home/timothy/Downloads/words.txt", sep=" ")
import pandas as pd
import numpy as np

def keep_only_rel_words(df):
    df.rename(columns={'2': 'words'}, inplace=True)
    #replace non aplphabetic values
    df['words'] = df.words.str.replace('[^a-zA-Z]', '')
    #make lowercase
    df['words'] = df['words'].str.lower()
    #only keep 5 letter words
    rel_words = df[df['words'].str.len() == 5]
    #drop duplicates
    rel_words = rel_words.drop_duplicates()
    
    return(rel_words)

#rel_words = word_preparer()

#in how many words does a certain letter appear, that should be the weight (fraction of words with the letter)
#turn every word into a set and determin how many sets have a letter


def df_preparer(df):  #probs only have to run this once in the beginning
    '''
    This function takes a dataframe of words and returns the words as a list of strings and list of sets nad list of lists
    '''
    #make function later if figured out what I need
    words = []
    words_split = []
    words_set = []
    
    for elm in df['words']:
        word = elm
        word_split = list(word)
        word_set = set(word_split)
         #append them
        words.append(word)
        words_split.append(word_split)
        words_set.append(word_set)
        
    df_new = pd.DataFrame(list(zip(words, words_split, words_set)),
                   columns =['Word', 'List', 'Set'])

    return(df_new)



#needs to be done after each itteration fo removing
def frac_calculator(letter, df):
    ''' Calculates the fraction of the words in the dataframe that use the particular letter. 
    '''
    letter_frac = 0
    for elm in df.Set:
        if letter in elm:
            letter_frac +=1
    letter_frac = letter_frac/len(df)
    #could expand this, not only take letter into consideration but letter at this specific position as well
    return(letter_frac)


def weight_dict_creator(df): 
    '''Creates a dict with the letter weights'''
    a = frac_calculator('a', df)
    b = frac_calculator('b', df)   
    c = frac_calculator('c', df)
    d = frac_calculator('d', df)
    e = frac_calculator('e', df)
    f = frac_calculator('f', df)   
    g = frac_calculator('g', df)
    h = frac_calculator('h', df)  
    i = frac_calculator('i', df)
    j = frac_calculator('j', df)   
    k = frac_calculator('k', df)
    l = frac_calculator('l', df)
    m = frac_calculator('m', df)
    n = frac_calculator('n', df)   
    o = frac_calculator('o', df)
    p = frac_calculator('p', df)       
    q = frac_calculator('q', df)
    r = frac_calculator('r', df)   
    s = frac_calculator('s', df)
    t = frac_calculator('t', df)
    u = frac_calculator('u', df)
    v = frac_calculator('v', df)   
    w = frac_calculator('w', df)
    x = frac_calculator('x', df)  
    y = frac_calculator('y', df)
    z = frac_calculator('z', df)
    
    sum_dict = {'a' : a, 'b' : b, 'c' : c, 'd' : d,
                'e' : e, 'f' : f, 'g' : g, 'h' : h,
                 'i' : i, 'j' : j, 'k' : k, 'l' : l,
                'm' : m, 'n' : n, 'o' : o, 'p' : p,
                
                'q' : q, 'r': r , 's' : s, 't' : t,
                'u' : u, 'v' : v, 'w' : w, 'x' : x,
                'y':y, 'z' : z}
    
    return(sum_dict)



def weight_scorer(df, letter_weights):
    '''
    Create a score per word and returns a list of scores
    '''
    words_scores = []
    #calculate the word scores
    for elm in df.Set: 
        weight_word = 0
        #print(elm)
        for e in elm:
            #print(e)
            weight_letter = letter_weights[e]
            weight_word += weight_letter
        words_scores.append(weight_word)
        #print('')
        
    df['Score'] = words_scores 
    df.sort_values(by=["Score"], inplace = True, ascending=False)
        
    return(df)



#combined function
def scorer(df):
    '''Takes in a word pandas with word collumn caled "word" and returns the dict scored and sorted'''
    weights = weight_dict_creator(df)
    df_new = weight_scorer(df, weights)
    
    return(df_new)












