import csv
from itertools import groupby

s_to_i = {
    "國": 0,
    "英": 1,
    "數A": 2,
    "數B": 3,
    "自": 4,
    "社": 5,
    "數甲": 6,
    "物": 7,
    "化": 8,
    "生": 9,
    "歷": 10,
    "地": 11,
    "公": 12,
}


def calculate_weight(score, select):
    admit = []

    for key, val in groupby(dic, lambda d: d["校名"]):
        if key in select:
            for i in list(val):
                weight = [0 for _ in range(13)]

                major = False
                for j in i["採計及加權"].split():
                    tmp = j.split("x")

                    if tmp[0] == "術科":
                        major = True

                        break

                    weight[s_to_i[tmp[0]]] = float(tmp[1])

                if i["錄取人數"] != 0 and major is False:
                    i["加權分數"] = sum([a * b for a, b in zip(score, weight)])
                    if i["加權分數"] >= float(i["錄取分數"]):
                        i["滿分率"] = (
                            float(i["錄取分數"]) / sum([a * 60 for a in weight]) * 100
                        )

                        admit.append(i)

    return admit


dic = []

with open("score.csv") as csvfile:
    dic = [
        {
            "系組代碼": i[0],
            "校名": i[1],
            "系組名": i[2],
            "採計及加權": i[3],
            "錄取人數": int(i[4]),
            "錄取分數": i[5],
        }
        for i in csv.reader(csvfile)
        if len(i) != 0
    ]
