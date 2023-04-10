import os

ROOT = "D:\\Code\\ZeroJudge\\Basic Question Bank"

# 提交
info = input().split()

file = info[0]
version = f"v{info[1]}.{info[2]}"

os.chdir(f"{ROOT}\\{file[0]}")
str = os.popen(f"git add .\\{file}.py")
if str.read() == "":
    os.system(f'git commit -m "ZeroJudge {file} {version}"')

# 創建
file = input()

with open(
    f"{ROOT}\\{file[0]}\\{file}.py", "x"
) as new_file:
    new_file.write("z")
