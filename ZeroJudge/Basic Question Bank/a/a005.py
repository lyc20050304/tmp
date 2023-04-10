"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a005
Title: Eva 的回家作業
"""

for _ in range(int(input())):
    num = list(map(int, input().split()))

    if num[1] - num[0] == num[2] - num[1]:
        print(*num, num[3] + (num[1] - num[0]))
    else:
        print(*num, num[3] * (num[1] // num[0]))
