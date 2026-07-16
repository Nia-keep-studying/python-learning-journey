#读取字符串
# from pathlib import Path

# # path = Path('pi_digits.txt')
# # contents = path.read_text()
# # print(contents)

# path1 = Path(__file__).parent / 'learning_python.txt'
# contents = path1.read_text(encoding='utf-8')
# print(contents)
# lines = contents.splitlines()
# string = ""
# for line in lines:
#     string += line
# string = string.replace("In Python you can","python中你可以")
# print(string)


#写入字符串
# from pathlib import Path

# path1 = Path(__file__).parent/ 'learning_python.txt'
# contents = "I want to be a ai agent\n"
# contents += "but i just studying python\n"
# contents += "i still have a long way to pass"
# path1.write_text(contents)
# string = ""
# for line in contents.splitlines():
#     string += line

# print(path1.read_text())
# print(string)

#10.4练习
# from pathlib import Path

# name = input("请输入你的名字")
# name_path = Path(__file__).parent/"guest_name.txt"
# name_path.write_text(str(name))
# print(name_path.read_text())

#10.5练习
# from pathlib import Path

# all_name = Path(__file__).parent/"all_name.txt"
# names = ''
# while True:
#     name = input("请输入名字(q退出)")
#     if name != "q":
#         names += f"{name}\n"
#     else:
#         all_name.write_text(names,encoding="utf-8")
#         break

# print(all_name.read_text(encoding="utf-8"))
# from pathlib import Path

# def count_words(file_name:str):
#     fill = Path(__file__).parent/file_name
#     words = fill.read_text(encoding="utf-8").split()
#     return len(words)

# print(count_words("learning_python.txt"))