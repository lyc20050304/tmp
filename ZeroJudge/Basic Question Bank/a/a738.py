"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a738
Title: 最大公约数
"""

from math import gcd

while True:
    try:
        print(gcd(*list(map(int, input().split()))))
    except TypeError:  # 此題無EOF
        break
