#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    all_score = 0
    all_weight = 0

    for score, weight in my_list:
        all_score += score * weight
        all_weight += weight

    if all_weight == 0:
        return 0

    wght_avg = all_score / all_weight
    return wght_avg
