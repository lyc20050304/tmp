"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a915
Title: 二维点排序
"""

[
    print(*i)
    for i in sorted([list(map(int, input().split())) for _ in range(int(input()))])
]
