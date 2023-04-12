"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a095
Title: 麥哲倫的陰謀
"""

while True:
    try:
        N, M = map(int, input().split())
    except EOFError:
        break

    if N == M:
        print(M)
    else:
        print(M + 1)
