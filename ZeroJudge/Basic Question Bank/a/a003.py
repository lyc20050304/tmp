"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a003
Title: 兩光法師占卜術
"""

S = eval(f"({input().replace(' ', ' * 2 + ')}) % 3")

if S == 0:
    print("普通")
elif S == 1:
    print("吉")
else:
    print("大吉")
