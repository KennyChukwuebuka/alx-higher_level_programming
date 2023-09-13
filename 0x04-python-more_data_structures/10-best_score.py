#!/usr/bin/python3
def best_score(a_dictionary):
    """best_score

        Args:
            a_dictionary:

        Return:
            Best score
    """
    if a_dictionary is None:
        return None

    best_score = None
    best_student = None

    for student, score in a_dictionary.items():

        if best_score is None or score > best_score:
            best_student = student
            best_score = score
    return best_student
