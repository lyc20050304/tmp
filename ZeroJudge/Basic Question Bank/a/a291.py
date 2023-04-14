"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a291
Title: nAnB problem

https://www.youtube.com/watch?v=IYJLLZ-RjnI&ab_channel=davidchien
有時候AC有時候TLE
"""

from sys import stdin, stdout

input = stdin.read().splitlines()

output = ""

i = 0
while i < len(input):
    tmp = input[i]
    i += 1

    if tmp.strip() == "":
        continue

    answer = tmp.split()

    c_answer = {str(i): 0 for i in range(10)}

    for j in answer:
        c_answer[j] += 1

    n = int(input[i])
    i += 1
    for _ in range(n):
        guess = input[i].split()
        i += 1

        cA, cB, c = 0, 0, c_answer.copy()

        not_match = []
        for j in range(4):
            num = guess[j]
            if c[num] > 0:
                if num == answer[j]:
                    cA += 1
                    c[num] -= 1
                else:
                    not_match.append(num)
        for j in not_match:
            if c[j] > 0:
                cB += 1
                c[j] -= 1

        output += f"{cA}A{cB}B\n"

stdout.write(output)
