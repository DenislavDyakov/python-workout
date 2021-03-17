#!/usr/bin/env python3
"""Solution to chapter 3, exercise 9, beyond 4: even_odd_sums"""


def even_odd_sums(numbers):
    """Takes a list of numbers, and returns a two-element
list containing the sum of the even-indexed elements and the
sum of the odd-indexed elements.
"""
    evens = []
    odds = []

    for idx in range(len(input_list)):
        if idx % 2:
            evens.append(input_list[idx])
        else:
            odds.append(input_list[idx])

    return [sum(evens), sum(odds)]
