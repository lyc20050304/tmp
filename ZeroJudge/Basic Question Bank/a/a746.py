"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a746
Title: 画蛇添足
"""

while True:
    try:
        tmp = input()
    except EOFError:
        break

    if tmp.strip() == "":
        continue

    n, m = map(int, tmp.split())

    ma = []

    for i in range(n + 2):
        if i == 0 or i == n + 2 - 1:  # 邊界
            ma.append(["-" for _ in range(n + 2)])
        else:
            ma.append(["|"] + [" " for i in range(n)] + ["|"])

    pre_x, pre_y = 0, 0
    for _ in range(m):
        x, y = map(int, input().split())

        ma[x][y] = "*"
        if x == pre_x:
            for i in range(min(y, pre_y), max(y, pre_y)):
                ma[x][i] = "*"
        elif y == pre_y:
            for i in range(min(x, pre_x), max(x, pre_x)):
                ma[i][y] = "*"

        pre_x, pre_y = x, y

    [print("".join(i)) for i in ma]
