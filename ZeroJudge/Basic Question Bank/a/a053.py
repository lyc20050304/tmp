"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a053
Title: Sagit's 計分程式
"""

N = int(input())

if 0 <= N <= 10:
    print(6 * N)
elif 11 <= N <= 20:
    print(60 + 2 * (N - 10))
elif 21 <= N <= 40:
    print(80 + (N - 20))
else:
    print(100)
