"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a981
Title: 求和問題

https://www.youtube.com/watch?v=VizVXAyhAAM&ab_channel=davidchien
此題用DFS會TLE
"""

from itertools import combinations

ign, m = map(int, input().split())
money = sorted(list(map(int, input().split())))

money1 = money[: (len(money) // 2)]
money2 = money[(len(money) // 2) :]

combination = {}

for i in range(1, len(money2) + 1):
    for j in combinations(money2, i):
        if sum(j) <= m:
            try:
                combination[sum(j)].append(j)
            except KeyError:
                combination[sum(j)] = [j]
[combination[i].sort() for i in combination.keys()]

find = False

for i in range(2 ** len(money1) - 1, 0 - 1, -1):
    binary = bin(i)[2:].zfill(len(money1))
    choose = [a for a, b in zip(money1, binary) if b == "1"]

    if sum(choose) == m:
        print(*choose)

        find = True
    elif sum(choose) < m:
        if (m - sum(choose)) in combination.keys():
            for k in combination[m - sum(choose)]:
                print(*choose, *k)

            find = True

if find is False:
    print(-1)
