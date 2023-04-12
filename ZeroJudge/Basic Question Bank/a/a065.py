"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a065
Title: 提款卡密碼
"""

password = input()

print(
    "".join(
        [
            str(abs(ord(password[i]) - ord(password[i - 1])))
            for i in range(1, len(password))
        ]
    )
)
