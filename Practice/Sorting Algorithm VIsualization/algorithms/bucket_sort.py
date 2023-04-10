def bucket_sort(li, draw):
    min_val = min(li)
    max_val = max(li)

    bucket_range = (max_val - min_val) / len(li)
    bucket = [[] for _ in range(len(li) + 1)]

    for i in range(len(li)):
        bucket[int((li[i] - min_val) // bucket_range)].append(li[i])

        draw(li, ["blue" if j == i else "white" for j in range(len(li))])

    result = [0 for _ in range(len(li))]

    i = 0
    for j in bucket:
        for k in j:
            result[i] = k

            draw(result, ["red" if m == i else "white" for m in range(len(result))])

            i += 1

    # Bubble Sort
    x1, x2 = 0, 0
    for i in bucket:
        x1, x2 = x2, x2 + len(i)

        for j in range(x2 - x1 - 1):
            for k in range(x1, x2 - j - 1):
                if result[k] > result[k + 1]:
                    result[k], result[k + 1] = result[k + 1], result[k]

                    draw(
                        result,
                        [
                            "red" if m in [k, k + 1] else "white"
                            for m in range(len(result))
                        ],
                    )

    draw(result, ["white" for _ in range(len(result))])
