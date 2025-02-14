#!/usr/bin/python3

def best_score(a_dictionary):
    ''' Returns dictionary key with highes value'''
    if a_dictionary is None:
        return (None)

    key_list = list(a_dictionary)
    value_list = [a_dictionary[key] for key in key_list]
    value_list.sort()
    max_value = value_list[-1]

    for key in a_dictionary:
        val = a_dictionary[key]
        if val == max_value:
            return (key)
