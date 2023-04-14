"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a271
Title: 彩色蘿蔔
"""

for _ in range(int(input())):
    x, y, z, w, n, m = map(int, input().split())

    dic = [0, x, y, -z, -w]

    eat = list(map(int, input().split()))

    c = 0
    for i in eat:
        m -= c * n  # 中毒
        if m <= 0:
            break

        m += dic[i]  # 吃東西
        if m <= 0:
            break

        if i == 4:  # 中毒疊加
            c += 1

    if m > 0:
        print(f"{m}g")
    else:
        print("bye~Rabbit")
