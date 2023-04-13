"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a121
Title: 質數又來囉
"""

prime = [2]
is_prime = [True for _ in range(int(100000000**0.5) + 1)]
is_prime[0] = is_prime[1] = False

for i in range(3, int(100000000**0.5) + 1, 2):
    if is_prime[i] is True:
        for j in prime:
            if i % j == 0:
                is_prime[i] = False

                break
        if is_prime[i] is True:
            prime.append(i)

            for j in range(i * i, int(100000000**0.5) + 1, 2 * i):
                is_prime[j] = False


def is_Prime(num):
    if num <= int(100000000**0.5):
        return is_prime[num]

    for i in prime:  # n > int(100000000 ** 0.5)
        if num % i == 0:
            return False
    return True


while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break

    c = 0

    if a <= 2 <= b:
        c += 1
        a = 3
    for i in range(a + (1 - a % 2), b + b % 2, 2):  # a改為奇數，b改為偶數
        if is_Prime(i) is True:
            c += 1

    print(c)
