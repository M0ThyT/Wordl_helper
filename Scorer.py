#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 22:02:49 2022

@author: timothy
"""
import pandas as pd
df = pd.read_csv("/home/timothy/Downloads/words.txt", sep=" ")


def word_preparer(df = df):
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

rel_words = word_preparer()

#in how many words does a certain letter appear, that should be the weight (fraction of words with the letter)
#turn every word into a set and determin how many sets have a letter




#create a dataframe with the sorted relevant words


def word_lists_creator(df): 
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

    return(words, words_split, words_set)



def frac_calculator(letter, words_set):
    ''' Calculates the fraction of the words in the dataframe that use the particular letter. 
    '''
    letter_frac = 0
    for elm in words_set:
        if letter in elm:
            letter_frac +=1
    letter_frac = letter_frac/len(words_set)
    #could expand this, not only take letter into consideration but letter at this specific position as well
    return(letter_frac)


def weight_dict_creator(words_set): 
    '''Creates a dict with the letter weights'''
    a = frac_calculator('a', words_set)
    b = frac_calculator('b', words_set)   
    c = frac_calculator('c', words_set)
    d = frac_calculator('d', words_set)
    e = frac_calculator('e', words_set)
    f = frac_calculator('f', words_set)   
    g = frac_calculator('g', words_set)
    h = frac_calculator('h', words_set)  
    i = frac_calculator('i', words_set)
    j = frac_calculator('j', words_set)   
    k = frac_calculator('k', words_set)
    l = frac_calculator('l', words_set)
    m = frac_calculator('m', words_set)
    n = frac_calculator('n', words_set)   
    o = frac_calculator('o', words_set)
    p = frac_calculator('p', words_set)       
    q = frac_calculator('q', words_set)
    r = frac_calculator('r', words_set)   
    s = frac_calculator('s', words_set)
    t = frac_calculator('t', words_set)
    u = frac_calculator('u', words_set)
    v = frac_calculator('v', words_set)   
    w = frac_calculator('w', words_set)
    x = frac_calculator('x', words_set)  
    y = frac_calculator('y', words_set)
    z = frac_calculator('z', words_set)
    
    sum_dict = {'a' : a, 'b' : b, 'c' : c, 'd' : d,
                'e' : e, 'f' : f, 'g' : g, 'h' : h,
                 'i' : i, 'j' : j, 'k' : k, 'l' : l,
                'm' : m, 'n' : n, 'o' : o, 'p' : p,
                
                'q' : q, 'r': r , 's' : s, 't' : t,
                'u' : u, 'v' : v, 'w' : w, 'x' : x,
                'y':y, 'z' : z}
    
    return(sum_dict)



def weight_scorer(word_set, letter_weights):
    '''
    Create a score per word and returns a list of scores
    '''
    words_scores = []
    #calculate the word scores
    for elm in words_set: 
        weight_word = 0
        #print(elm)
        for e in elm:
            #print(e)
            weight_letter = letter_weights[e]
            weight_word += weight_letter
        words_scores.append(weight_word)
        #print('')
        
        
    return(words_scores)
         
def data_sorter(words, words_split, words_set, words_scores):        
    df = pd.DataFrame(list(zip(words, words_split, words_set, words_scores)),
                   columns =['Word', 'List', 'Set', 'Score'])
    
    df.sort_values(by=["Score"], inplace = True, ascending=False)
    
    return(df)


#%%combine scorer
def scorer(df):
    '''Takes in a word pandas with word collumn caled "word" and returns the dict scored and sorted'''
    words, words_list, words_set = word_lists_creator(rel_words)
    words_weights = weight_dict_creator(words_set)
    words_scores = weight_scorer(words_set, words_weights)
    final_df = data_sorter(words, words_list,words_set, words_scores)
    
    return(final_df)
