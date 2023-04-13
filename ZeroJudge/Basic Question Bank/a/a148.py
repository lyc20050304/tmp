"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a148
Title: You Cannot Pass?!
"""

while True:
    try:
        num = list(map(int, input().split()))
    except EOFError:
        break

    if sum(num[1:]) / num[0] > 59:
        print("no")
    else:
        print("yes")
