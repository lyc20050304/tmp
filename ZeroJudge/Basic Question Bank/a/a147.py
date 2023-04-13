"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a147
Title: Print it all
"""

while True:
    try:
        n = int(input())
    except EOFError:
        break

    if n == 0:
        break

    print(*[i for i in range(1, n) if i % 7 != 0])
