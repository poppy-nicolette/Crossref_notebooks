# false_match_on_title
# use Levenshtein token-based distance, instead of character
import numpy as np
from Levenshtein import distance as lev_distance, seqratio as lev_seqratio
#for stopword removal option
import nltk
import os
from tarfile import LENGTH_LINK
from tarfile import LENGTH_NAME
from nltk.corpus import stopwords

NLTK_DATA = "/Users/poppyriddle/nltk_data" # this is a default lookup path

stopWords = set(stopwords.words('english'))

def remove_stopwords(x:str)->list:
    """
    for a given string, returns a list with no stopwords
    to do:
        include language version
    """
    words:list = x.split(" ")
    wordsFiltered:list = [w for w in words if w not in stopWords]
    return wordsFiltered

def token_based_levenshtein(text1:str, text2:str, stopwords_arg=None)->float:
    """takes as input, two multi-token strings, and calculates the normalized distance between them.
    There is an commented line to use seqratio instead of distance.
    there is an option in the args to remove stopwords.

    Input: text1:str, text2:str, stopwords_arg=None
        text1: This is a string of any length.
        text2: This is a string of any length.
        stopwords_arg: This is a boolean value indicating whether to remove stopwords or not.

    Output: float as normalized distance between the two
    """

    # remove stopwords option
    if stopwords_arg == True:
        tokens1 = remove_stopwords(text1)
        #print(f"tokens1: {tokens1}")
        tokens2 = remove_stopwords(text2)
        #print(f"\n----\ntokens2: {tokens2}\n")
    else:
        #tokenize - no cleaning at this point
        tokens1 = text1.split()
        tokens2 = text2.split()

    #compute levenshtein distance
    #distance = lev_seqratio(tokens1,tokens2)
    distance = lev_distance(tokens1,tokens2)

    #normalize by distance to the max length of token seq
    max_length = max(len(tokens1), len(tokens2))
    normalized_distance = distance / max_length if max_length > 0 else 0

    return normalized_distance
