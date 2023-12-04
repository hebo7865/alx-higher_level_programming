#!/usr/bin/python3
def no_c(my_string):
    no_c = ""
    for i in range(len(my_string)):
        if (my_string[i] != "C" and my_string[i] != "c"):
            no_c += my_string[i]
    return no_c
