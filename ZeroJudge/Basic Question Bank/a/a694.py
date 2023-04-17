"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a694
Title: 吞食天地二
"""

from itertools import accumulate

while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break

    pre = [[0 for _ in range(n + 1)]]

    for i in range(n):  # 橫向累加
        pre.append([0] + list(accumulate(list(map(int, input().split())))))
    pre = [
        list(accumulate(col)) for col in zip(*pre)
    ]  # 直向累加(因為*pre會將每個橫列拆分出來，而zip又將每個橫列中索引值相同的元素合成一個tuple，最終效果是把陣列整個翻轉，所以實際上accumulate()做的還是橫向累加)
    pre = [list(col) for col in zip(*pre)]  # 直向累加完後需要將陣列復原

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())

        print(pre[x2][y2] - pre[x1 - 1][y2] - pre[x2][y1 - 1] + pre[x1 - 1][y1 - 1])
