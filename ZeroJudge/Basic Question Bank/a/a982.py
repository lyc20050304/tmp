"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a982
Title: 迷宮問題#1
"""

from queue import Queue

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 右、下、左、上


def in_bound(x, y, ma):
    if ma[x][y] == ".":
        return True
    return False


N = int(input())
ma = [list(input()) for _ in range(N)]

find = False
coo = Queue()
ma[1][1] = "x"
coo.put([1, 1, 1])  # [x, y, 步數]
while coo.empty() is False:  # BFS
    (
        x,
        y,
        c,
    ) = coo.get()

    for i in range(4):
        if in_bound(x + dir[i][0], y + dir[i][1], ma):
            if x + dir[i][0] == y + dir[i][1] == N - 2:
                print(c + 1)

                find = True
                break

            ma[x + dir[i][0]][y + dir[i][1]] = "x"
            coo.put([x + dir[i][0], y + dir[i][1], c + 1])

    if find is True:
        break

if find is False:
    print("No solution!")
