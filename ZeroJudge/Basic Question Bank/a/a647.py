"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a647
Title: 投資專家
"""

for _ in range(int(input())):
    m, p = map(int, input().split())

    x = (p - m) / m * 100

    if x > 0:  # 消除誤差(f-string的:.2f會無條件捨去，0.05有可能是0.04999...)，但不知道為什麼是0.00001
        x += 0.00001
    elif x < 0:
        x -= 0.00001

    if x >= 10 or x <= -7:
        print(f"{x:.2f}% dispose")
    else:
        print(f"{x:.2f}% keep")
