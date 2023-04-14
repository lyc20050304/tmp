"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a244
Title: 新手訓練 ~ for + if
"""

dic = ["", "+", "-", "*", "//"]

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    print(eval(f"{b} {dic[a]} {c}"))
