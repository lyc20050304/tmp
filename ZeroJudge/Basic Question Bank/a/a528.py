"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a528
Title: 大數排序
"""

while True:
    try:
        [print(i) for i in sorted([int(input()) for _ in range(int(input()))])]
    except EOFError:
        break
