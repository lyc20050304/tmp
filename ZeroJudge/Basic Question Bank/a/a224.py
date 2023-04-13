"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a224
Title: 明明愛明明
"""

while True:
    try:
        str = input().lower()
    except EOFError:
        break

    c = 0

    str_set = set(str)
    for i in str_set:
        if i.isalpha() is True:
            if str.count(i) % 2 == 1:
                c += 1

    if c > 1:
        print("no...")
    else:
        print("yes !")
