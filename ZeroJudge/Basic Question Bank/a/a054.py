"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a054
Title: 電話客服中心
"""

dic = ["BNZ", "AMW", "KLY", "JVX", "HU", "GT", "FS", "ER", "DOQ", "CIP"]

ID = input()

s = sum([(8 - i) * int(ID[i]) for i in range(len(ID) - 1)])

print(dic[(10 - s % 10 - int(ID[-1])) % 10])
