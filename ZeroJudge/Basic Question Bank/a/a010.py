"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a010
Title: 因數分解
"""

num = int(input())

find = False

for i in [2, 3] + [k for j in range(6, int(num**0.5) + 1, 6) for k in [j - 1, j + 1]]:
    c = 0
    while num % i == 0:
        c += 1
        num //= i
    if c > 0:
        if find is True:
            print(" * ", end="")
        print(i, end="")
        if c > 1:
            print(f"^{c}", end="")

        find = True

    if num == 1:
        break

if num != 1:
    if find is True:
        print(" * ", end="")
    print(num)
