"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a017
Title: 五則運算
"""

while True:
    try:
        print(eval(input().replace("/", "//")))
    except EOFError:
        break
