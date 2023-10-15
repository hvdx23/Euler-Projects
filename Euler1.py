"""Project Euler Problem 1 Solution"""

import sys


new_recursion_limit = 4000000
sys.setrecursionlimit(new_recursion_limit)
values = []


def check(n):
    if n == 1:
        return
    if n % 3 == 0 or n % 5 == 0:
        values.append(n)
    check(n - 1)

check(999)
print(values)
summary = sum(values)
print(summary)
