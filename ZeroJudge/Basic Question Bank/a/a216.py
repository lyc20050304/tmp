"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a216
Title: 數數愛明明
"""

f = [0 for _ in range(30001)]
g = [0 for _ in range(30001)]
f[1] = g[1] = 1

for i in range(2, 30000 + 1):
    f[i] = i + f[i - 1]
    g[i] = f[i] + g[i - 1]

while True:
    try:
        n = int(input())
    except EOFError:
        break

    print(f[n], g[n])
