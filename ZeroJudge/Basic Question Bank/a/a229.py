"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a229
Title: 括號匹配問題
"""

DP = [[[] for _ in range(14)] for _ in range(14)]  # DP[L][R]代表剩餘L個左括號與R個右括號的所有情況

for right in range(1, 13 + 1):
    DP[0][right] = [")" * right]
for left in range(1, 13 + 1):
    DP[left][left] = ["(" + i for i in DP[left - 1][left]]
    for right in range(left + 1, 13 + 1):
        DP[left][right] = ["(" + i for i in DP[left - 1][right]] + [
            ")" + i for i in DP[left][right - 1]
        ]

while True:
    try:
        N = int(input())
    except ValueError:
        break

    print("\n".join(DP[N][N]))  # 使用列表推導式會TLE
