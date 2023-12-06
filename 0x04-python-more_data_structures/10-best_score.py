#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    val = 0
    ke = None
    for k, v in a_dictionary.items():
        if v > val:
            val = v
            ke = k
    return ke
