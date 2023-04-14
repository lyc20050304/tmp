"""
Problem: https://zerojudge.tw/ShowProblem?problemid=a410
Title: 解方程
"""

"""
ax + by = c
dx + ey = f

△ = ae - bd
△x = ce - bf
△y = af - cd

x = △x / △ = (ce - bf) / (ae - bd)
y = △y / △ = (af - cd) / (ae - bd)
"""

a, b, c, d, e, f = map(int, input().split())

delta = a * e - b * d
delta_x = c * e - b * f
delta_y = a * f - c * d

if delta == 0:
    if delta_x == delta_y == 0:
        print("Too many")
    else:
        print("No answer")
else:
    print(f"x={(delta_x / delta):.2f}")
    print(f"y={(delta_y / delta):.2f}")
