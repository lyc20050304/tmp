def insertion_sort(li, draw):
    for i in range(1, len(li)):
        num = li[i]
        j = i - 1

        while li[j] > num and j >= 0:
            li[j + 1] = li[j]

            draw(
                li,
                [
                    "blue" if k == i else "red" if k in [j + 1, j] else "white"
                    for k in range(len(li))
                ],
            )

            j -= 1

        li[j + 1] = num

        draw(li, ["red" if k == j + 1 else "white" for k in range(len(li))])

    draw(li, ["white" for _ in range(len(li))])
