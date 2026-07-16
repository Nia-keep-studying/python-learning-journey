# def sum_num():    
#     num_1 = input("输入第一个数")
#     num_2 = input("输入第二个数")
#     try:
#         sum_nums = int(num_1)+int(num_2)
#         print(f"{num_1}和{num_2}的合为{sum_nums}")
#     except ValueError:
#         print("请输入纯数字")
    

# sum_num()
from pathlib import Path

# contents = ''
# def write_name():
#     global contents
#     name = input("请输入名称")
#     path1 = Path(__file__).parent/"name.txt"
#     contents += f"{name}\n"
#     path1.write_text(contents)

# write_name()

# name = input("请输入你的名字")
# path_name = Path(__file__).parent/"name.txt"
# path_name.write_text(name)
# print(path_name.read_text())


#用while循环一次性写入多行名字（应该还能优化，回头重构一下）
# list_name = []
# while True:
#     name = input("请输入名字(q退出)")
#     if name != "q":
#         list_name.append(name)
#     else:    
#         break
# path_names = Path(__file__).parent/"names.txt"
# names = ''
# for i in list_name:
#     names += i+"\n" 
# path_names.write_text(f"{names}")
# print(path_names.read_text())


# def sum_numbers():
"""while语句让用户重复输入,不会因为报错而退出"""
#     while True:
#         try:
#             num_1 = input("输入第一个整数")
#             if num_1 == "q":
#                 break
#             num_2 = input("输入第二个整数")
#             if num_2 == "q":
#                 break
#             num_1 = int(num_1)
#             num_2 = int(num_2)
#         except ValueError:
#             print("输入的不是整数")
#             continue
#         else:
#             print(f"{num_1}和{num_2}的合为{num_1+num_2}")

# sum_numbers()


#检查文件找不到错误，以及静默失败实验
# path_cat = Path(__file__).parent/"cat.txt"
# path_dog = Path(__file__).parent/"dog.txt"

# try:
#     print(path_cat.read_text())
# except FileNotFoundError:
#     pass

# try:
#     print(path_dog.read_text())
# except FileNotFoundError:
#     pass


#分析pg3467.txt中的信息
# path_book = Path(__file__).parent/"pg3567.txt"
# print(path_book.read_text(encoding="utf-8").lower().count("the "))

#分析有多少个单词（大概）
# path_book = Path(__file__).parent/"pg3567.txt"
# print(len(path_book.read_text(encoding="utf-8").split()))

