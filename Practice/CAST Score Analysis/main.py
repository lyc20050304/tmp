import tkinter as tk
import name
import analysis

# 初始化
root = tk.Tk()

root.title("CAST Score Analysis")

# 設定視窗大小
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

width = screen_width // 2
height = screen_height // 2
top = screen_width // 4
left = screen_height // 4

root.geometry(f"{width}x{height}+{top}+{left}")

# 創建有滑動條的畫布
canvas = tk.Canvas(root, width=width, height=height)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.config(yscrollcommand=scrollbar.set)

# 使用者介面
main_frame = tk.Frame(canvas)

tk.Label(main_frame, text="分科測驗成績分析").grid(row=0, column=0, sticky="w")

# 輸入成績
frame1 = tk.Frame(main_frame)

tk.Label(frame1, text="輸入學測級分").grid(row=0, column=0, sticky="w")
tk.Label(frame1, text="輸入分科成績").grid(row=1, column=0, sticky="w")

j = 0
for i in range(1, 13 + 1):
    if i == 7:
        j = 1

    exec(f"subject{i} = tk.IntVar()")
    exec(f"frame1_{i} = tk.Frame(frame1)")
    exec(
        f"tk.Label(frame1_{i}, text='{name.subject[i]}').grid(row=0, column=0, sticky='w')"
    )
    exec(
        f"tk.Entry(frame1_{i}, textvariable=subject{i}, width=2).grid(row=0, column=1, sticky='w')"
    )
    exec(f"frame1_{i}.grid(row={j}, column={i % 7 + j}, sticky='w')")

frame1.grid(row=1, column=0, sticky="w")


# 確定成績
def input_score():
    global score
    score = [eval(f"subject{i}.get()") for i in range(1, 13 + 1)]


tk.Button(
    main_frame,
    text="確定",
    command=lambda: [
        input_score(),
        frame2.grid(row=3, column=0, sticky="w"),
        button.grid(row=4, column=0, sticky="w"),
    ],
).grid(row=2, column=0, sticky="w")

# 依大學篩選
click1, click2 = False, False


def select_all1():
    global click1

    if click1 is False:
        for i in range(1, 31 + 1):
            exec(f"button{i}.select()")

            click1 = True
    else:
        for i in range(1, 31 + 1):
            exec(f"button{i}.deselect()")

            click1 = False


def select_all2():
    global click2

    if click2 is False:
        for i in range(32, 62 + 1):
            exec(f"button{i}.select()")

            click2 = True
    else:
        for i in range(32, 62 + 1):
            exec(f"button{i}.deselect()")

            click2 = False


frame2 = tk.LabelFrame(main_frame, text="依大學篩選")

tk.Checkbutton(frame2, text="公立全選", command=select_all1).grid(
    row=0, column=0, columnspan=5, sticky="w"
)
tk.Checkbutton(frame2, text="私立全選", command=select_all2).grid(
    row=8, column=0, columnspan=5, sticky="w"
)

j, k = 1, 0
for i in range(1, 62 + 1):
    if i == 32:
        j, k = 9, 0

    exec(f"college{i} = tk.StringVar()")
    exec(
        f"button{i} = tk.Checkbutton(frame2, text='{name.college[i]}', variable=college{i}, onvalue='{name.college[i]}', offvalue='')"
    )
    exec(f"button{i}.grid(row={j}, column={k}, sticky='w')")

    k += 1

    j += k // 5
    k %= 5


# 開始分析
def create_list():
    select = " ".join([eval(f"college{i}.get()") for i in range(1, 62 + 1)])

    global admit
    admit = [
        {
            "系組代碼": "系組代碼",
            "校名": "校名",
            "系組名": "系組名",
            "錄取人數": "錄取人數",
            "錄取分數": "錄取分數",
            "滿分率": "錄取分數/滿分",
            "加權分數": "加權分數",
        }
    ] + sorted(
        analysis.calculate_weight(score, select),
        key=lambda d: d["滿分率"],
        reverse=True,
    )


button = tk.Button(main_frame, text="開始分析", command=lambda: [create_list(), show()])


# 顯示錄取校系
def show():
    global frame4

    frame4.destroy()

    frame4 = tk.Frame(main_frame)

    for i in range(len(admit)):
        tk.Label(frame4, text=admit[i]["系組代碼"]).grid(row=i, column=0, sticky="w")
        tk.Label(frame4, text=admit[i]["校名"]).grid(row=i, column=1, sticky="w")
        tk.Label(frame4, text=admit[i]["系組名"]).grid(row=i, column=2, sticky="w")
        tk.Label(frame4, text=admit[i]["錄取人數"]).grid(row=i, column=3, sticky="w")
        tk.Label(frame4, text=admit[i]["錄取分數"]).grid(row=i, column=4, sticky="w")
        if i == 0:
            tk.Label(frame4, text=f"{admit[i]['滿分率']}").grid(
                row=i, column=5, sticky="w"
            )
        else:
            tk.Label(frame4, text=f"{admit[i]['滿分率']:.2f}%").grid(
                row=i, column=5, sticky="w"
            )
        tk.Label(frame4, text=admit[i]["加權分數"]).grid(row=i, column=6, sticky="w")

    frame4.grid(row=5, column=0, sticky="w")


frame4 = tk.Frame(main_frame)


canvas.create_window(0, 0, anchor="nw", window=main_frame)

# 滑動設定
main_frame.bind(
    "<Configure>", lambda event: canvas.config(scrollregion=canvas.bbox("all"))
)  # 動態規劃滑動範圍，因為要包含上面的所有元素，所以要放在最下面，不加event(可改)會沒效果不知道為什麼
canvas.pack()


root.mainloop()
