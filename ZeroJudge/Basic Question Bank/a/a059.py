"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a059
Title: 完全平方和
"""

from math import ceil, floor

for i in range(1, int(input()) + 1):
    a = ceil(int(input()) ** 0.5)
    b = floor(int(input()) ** 0.5)

    print(f"Case {i}: {sum([j ** 2 for j in range(a, b + 1)])}")
