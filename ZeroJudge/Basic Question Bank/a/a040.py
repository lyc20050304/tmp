"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a040
Title: 阿姆斯壯數
"""

find = False
for i in range(*list(map(int, input().split()))):
    if sum([int(j) ** len(str(i)) for j in str(i)]) == i:
        print(i, end=" ")

        find = True
if find is False:
    print("none")
