"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a044
Title: 空間切割
"""

while True:
    try:
        n = int(input())
    except EOFError:
        break

    print((n**3 + 5 * n + 6) // 6)
