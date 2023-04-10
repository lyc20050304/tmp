def counting_sort(li, draw):
    min_val = min(li)
    max_val = max(li)

    c = [0 for _ in range(max_val - min_val + 1)]

    for i in range(len(li)):
        c[li[i] - min_val] += 1

        draw(li, ["blue" if j == i else "white" for j in range(len(li))])

    for i in range(1, max_val - min_val + 1):
        c[i] += c[i - 1]

    result = [0 for i in range(len(li))]

    for i in range(len(result) - 1, 0 - 1, -1):  # 從後掃到前是為了製造一個穩定的排序法(即相同數字的相對位置不變)
        result[c[li[i] - min_val] - 1] = li[i]

        draw(
            result,
            [
                "red" if j == c[li[i] - min_val] - 1 else "white"
                for j in range(len(result))
            ],
        )

        c[li[i] - min_val] -= 1

    draw(result, ["white" for i in range(len(result))])
