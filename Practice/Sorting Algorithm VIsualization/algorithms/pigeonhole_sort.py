def pigeonhole_sort(li, draw):
    min_val = min(li)
    max_val = max(li)

    c = [0 for _ in range(max_val - min_val + 1)]

    for i in range(len(li)):
        c[li[i] - min_val] += 1

        draw(li, ["blue" if j == i else "white" for j in range(len(li))])

    result = [0 for _ in range(len(li))]

    i = 0
    for num, time in enumerate(c):
        for j in range(time):
            result[i] = num

            draw(result, ["red" if k == i else "white" for k in range(len(result))])

            i += 1

    draw(result, ["white" for _ in range(len(result))])
