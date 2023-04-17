"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a524
Title: 手機之謎
"""

from itertools import permutations

while True:
    try:
        [
            print("".join(i))
            for i in permutations([str(j) for j in range(int(input()), 1 - 1, -1)])
        ]
    except ValueError:  # 此題無EOF
        break
