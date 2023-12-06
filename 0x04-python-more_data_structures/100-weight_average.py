#!/usr/bin/pythpn3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        return (sum(a * b for a, b in my_list) / sum(a + b  for a, b in my_list))
