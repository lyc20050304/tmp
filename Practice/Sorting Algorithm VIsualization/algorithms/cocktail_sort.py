def cocktail_sort(li, draw):
    for i in range(len(li) - 1, 1 - 1, -1):
        swap = False

        for j in range(i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

                draw(
                    li, ["red" if k in [j, j + 1] else "white" for k in range(len(li))]
                )

                swap = True

        for j in range(i - 1, 1 - 1, -1):
            if li[j - 1] > li[j]:
                li[j - 1], li[j] = li[j], li[j - 1]

                draw(
                    li, ["red" if k in [j - 1, j] else "white" for k in range(len(li))]
                )

                swap = True

        if swap is False:
            break

    draw(li, ["white" for _ in range(len(li))])
