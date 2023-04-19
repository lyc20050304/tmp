"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a740
Title: 质因数之和
"""

while True:
    try:
        x = int(input())
    except EOFError:
        break

    s = 0
    for i in [2, 3] + [
        k for j in range(6, int(x**0.5) + 1, 6) for k in [j - 1, j + 1]
    ]:
        while x % i == 0:
            s += i
            x //= i

        if x == 1:
            break

    if x != 1:
        s += x

    print(s)
