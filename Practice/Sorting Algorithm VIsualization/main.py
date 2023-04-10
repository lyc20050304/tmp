import tkinter as tk
from tkinter import ttk
import random

from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.cocktail_sort import cocktail_sort
from algorithms.bucket_sort import bucket_sort
from algorithms.counting_sort import counting_sort
from algorithms.merge_sort import merge_sort
from algorithms.pigeonhole_sort import pigeonhole_sort
from algorithms.radix_sort import radix_sort
from algorithms.gnome_sort import gnome_sort

MAX = 200
AMOUNT = 100

# 初始化
root = tk.Tk()

root.title("Sorting Algorithm Visualization")

root.state("zoomed")

# 使用者介面
algorithm = tk.StringVar()
algorithm_li = [
    "Bubble Sort",
    "Insertion Sort",
    "Cocktail Sort",
    "Bucket Sort",
    "Counting Sort",
    "Merge Sort",
    "Pigeonhole Sort",
    "Radix Sort",
    "Gnome Sort",
]


def initialize():
    global li
    li = [random.randint(1, MAX) for _ in range(AMOUNT)]
    color = ["white" for _ in range(AMOUNT)]

    draw(li, color)


def sort(algorithm):
    if algorithm == "Merge Sort":
        merge_sort(li, 0, AMOUNT - 1, draw)
    else:
        exec(f"{algorithm.lower().replace(' ', '_')}(li, draw)")


UI = tk.Frame(root)

frame1 = tk.Frame(UI)
tk.Label(frame1, text="Algorithm: ").grid(row=0, column=0)
ttk.Combobox(frame1, textvariable=algorithm, values=algorithm_li).grid(row=0, column=1)
frame1.grid(row=0, column=0)

frame2 = tk.Frame(UI)
tk.Button(frame2, text="Initialize", command=initialize).grid(row=0, column=0, padx=20)
tk.Button(frame2, text="Sort", command=lambda: sort(algorithm.get())).grid(
    row=0, column=1, padx=20
)
frame2.grid(row=1, column=0)

UI.pack()

root.update_idletasks()


# 排序可視化區
def draw(li, color):
    canvas.delete("all")

    bar_width = canvas.winfo_width() / AMOUNT
    canvas_height = canvas.winfo_height()
    percentage = [i / MAX for i in li]

    for i, percent in enumerate(percentage):  # 左上、右下
        x1 = i * bar_width
        y1 = canvas_height - percent * canvas_height
        x2 = (i + 1) * bar_width
        y2 = canvas_height

        canvas.create_rectangle(x1, y1, x2, y2, fill=color[i])

    root.update_idletasks()


canvas = tk.Canvas(
    root,
    width=root.winfo_width(),
    height=(root.winfo_height() - UI.winfo_height()),
    bg="black",
)
canvas.pack()

root.update_idletasks()


root.mainloop()
