def radix_sort(li, draw):
    max_val = max(li)
    digit = 1

    while max_val > 10**digit:
        digit += 1

    for i in range(digit):
        bucket = [[] for _ in range(10)]

        for j in range(len(li)):
            bucket[li[j] // (10**i) % 10].append(li[j])

            draw(li, ["blue" if k == j else "white" for k in range(len(li))])

        j = 0
        for k in bucket:
            for m in k:
                li[j] = m

                draw(li, ["red" if n == j else "white" for n in range(len(li))])

                j += 1

    draw(li, ["white" for _ in range(len(li))])
