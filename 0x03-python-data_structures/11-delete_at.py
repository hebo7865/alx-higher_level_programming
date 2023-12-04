#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in my_list:
        if my_list.index(i) == idx:
            my_list.remove(i)
    return my_list
