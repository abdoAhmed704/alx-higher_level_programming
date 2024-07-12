#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(lista):
    """the peak"""
    if list_of_integers is None or list_of_integers == []:
        return None
    lista.sort()
    return lista[-1]
