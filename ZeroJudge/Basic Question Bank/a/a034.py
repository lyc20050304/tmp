"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a034
Title: 二進位制轉換
"""

while True:
    try:
        print(f"{int(input()):b}")
    except EOFError:
        break
