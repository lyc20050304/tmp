"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a263
Title: 日期差幾天
"""

from datetime import datetime

while True:
    try:
        y1, m1, d1 = map(int, input().split())
    except EOFError:
        break

    y2, m2, d2 = map(int, input().split())

    print(abs(datetime(y1, m1, d1) - datetime(y2, m2, d2)).days)
