"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a693
Title: 吞食天地
"""

from itertools import accumulate

while True:
    try:
        ign, m = map(int, input().split())
    except EOFError:
        break

    pre = [0] + list(accumulate(list(map(int, input().split()))))

    for _ in range(m):
        l, r = map(int, input().split())

        print(pre[r] - pre[l - 1])
