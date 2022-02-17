#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:52:51 2022

@author: timothy
"""
#Remover
dft = final_df.copy()


#letter in word
def letter_in_word(df, letter):
    #get the index of the words who contain the letter specified
    index_words = []
    for row in df.Set.iteritems():
        index = row[0]
        word_set = row[1]
        if letter in word_set: 
            index_words.append(index)

    df_new = df[df.index.isin(index_words)]
    
    return(df_new)

#letter not in word
def letter_not_in_word(df, letter):
    #get the index of the words who contain the letter specified
    index_words = []
    for row in df.Set.iteritems():
        index = row[0]
        word_set = row[1]
        if letter in word_set: 
            index_words.append(index)

    df_new = df[~df.index.isin(index_words)]
    
    return(df_new)






#letter in position
def letter_in_position(df, letter, position):
    '''
    Parameters
    ----------
    df : dataframe
        Df with words, needs to at least have the set and list version of words.
    letter : string
        The letter you know the position of. Make sure to put it in ''
    position : int
        The position of the letter you know.

    Returns a filtered df with only relevant words remaining
    -------

    '''
    index_words = []
    for row in df.List.iteritems():
        #get the word list and index seperated
        word_list = row[1]
        index = row[0]
        #create a var that stores the letter of the word in the position we are interested in 
        #(I did position - 1 because python counts from 0 but thats not intuitive for entering)
        letter_in_word = word_list[position -1 ]
        #if the word letter in the specified position is equal to the one we are looking for, add the index to the list
        if letter_in_word == letter:
            index_words.append(index)
    #create a filtered df with only relevant words remaining
    df_new = df[df.index.isin(index_words)]

    return(df_new)


#letter not in position
def letter_in_position_not(df, letter, position):
    '''
    Parameters
    ----------
    df : dataframe
        Df with words, needs to at least have the set and list version of words.
    letter : string
        The letter you know in which position it is not. Make sure to put it in ''
    position : int
        The position you know the letter is not in.

    Returns a filtered df with only relevant words remaining
    -------

    '''
    index_words = []
    for row in df.List.iteritems():
        #get the word list and index seperated
        word_list = row[1]
        index = row[0]
        #create a var that stores the letter of the word in the position we are interested in 
        #(I did position - 1 because python counts from 0 but thats not intuitive for entering)
        letter_in_word = word_list[position -1 ]
        #if the word letter in the specified position is equal to the one we are looking for, add the index to the list
        if letter_in_word == letter:
            index_words.append(index)
    #create a filtered df with only relevant words remaining
    df_new = df[~df.index.isin(index_words)]

    return(df_new)
