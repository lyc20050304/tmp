def bubble_sort(li, draw):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

                draw(
                    li, ["red" if k in [j, j + 1] else "white" for k in range(len(li))]
                )

    draw(li, ["white" for _ in range(len(li))])
