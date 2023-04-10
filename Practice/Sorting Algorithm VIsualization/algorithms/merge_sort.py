def merge_sort(li, L, R, draw):  # 雖然是合併排序，但是為了方便上色，實際上是原地合併排序
    if L < R:
        M = (L + R) // 2

        merge_sort(li, L, M, draw)
        merge_sort(li, M + 1, R, draw)

        i, j = L, M + 1
        while i <= M and j <= R:
            draw(li, ["blue" if k in [i, j] else "white" for k in range(len(li))])

            if li[i] <= li[j]:
                i += 1
            else:
                for k in range(j, i, -1):
                    li[k - 1], li[k] = li[k], li[k - 1]

                i += 1
                j += 1
                M += 1

    draw(li, ["white" for _ in range(len(li))])
