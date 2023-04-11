"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a015
Title: 矩陣的翻轉
"""

while True:  # 測資有多筆輸入
    try:
        r, c = map(int, input().split())
    except EOFError:
        break

    A = [input().split() for _ in range(r)]

    [print(*[A[i][j] for i in range(r)]) for j in range(c)]
