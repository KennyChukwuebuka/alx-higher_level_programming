#!/usr/bin/python3

def multiple_returns(sentence):

    if not sentence:
        return (0, None)

    len_of_sen = len(sentence)
    get_first_char = sentence[0]
    return (len_of_sen, get_first_char)
