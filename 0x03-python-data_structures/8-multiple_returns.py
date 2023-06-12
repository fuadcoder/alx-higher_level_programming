#!/usr/bin/python3
# Author - Olamide Olasupo

def multiple_returns(sentence):
    """Return the length of a string and its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
