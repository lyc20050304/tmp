def gnome_sort(li, draw):
    i = 1
    while i < len(li):
        if i == 0 or li[i - 1] <= li[i]:
            i += 1
        else:
            li[i - 1], li[i] = li[i], li[i - 1]

            draw(li, ["red" if j in [i - 1, i] else "white" for j in range(len(li))])

            i -= 1

    draw(li, ["white" for _ in range(len(li))])
