"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a022
Title: 迴文
"""

str = input()

if str == str[::-1]:
    print("yes")
else:
    print("no")
