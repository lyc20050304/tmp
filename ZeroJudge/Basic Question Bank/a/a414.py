"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a414
Title: 位元運算之進位篇
"""

from sys import stdin

for input in stdin:
    N = int(input)

    if N == 0:
        break

    print(len(bin(N)) - len(bin(N).rstrip("1")))  # 原本長度 - 扣除右邊連續1後的長度(因為原數字+1後碰到1就會進位)
