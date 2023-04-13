"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a149
Title: 乘乘樂
"""

for _ in range(int(input())):
    n = input()

    s = 1
    for i in n:
        s *= int(i)

    print(s)
