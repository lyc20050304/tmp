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

if os.path.isdir(f"{ROOT}\\{file[0]}") is False:
    os.chdir(ROOT)  # 不知道為什麼不能使用os.system("cd..")退回前一層資料夾
    os.system(f"md {file[0]} && cd {file[0]}")
with open(f"{ROOT}\\{file[0]}\\{file}.py", "x") as new_file:
    new_file.write("z")
