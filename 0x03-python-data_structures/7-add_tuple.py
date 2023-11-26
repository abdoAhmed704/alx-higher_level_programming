#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n1 = tuple_a[0] if len(tuple_a) > 0 else 0
    n2 = tuple_a[1] if len(tuple_a) > 1 else 0
    n3 = tuple_b[0] if len(tuple_b) > 0 else 0
    n4 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (n1 + n3, n2 + n4)
