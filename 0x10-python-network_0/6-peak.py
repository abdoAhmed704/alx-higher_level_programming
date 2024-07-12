#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(lista):
    """the peak"""
    if lista is None or lista == []:
        return None
    lista.sort()
    return lista[-1]
