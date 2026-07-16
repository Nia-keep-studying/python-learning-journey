import search_function


while True:
    print(
        "1.查询用户信息\n"
        "2.pass\n"
        "3.退出\n"
    )
    option = input("请选择要执行的操作： ")  
    if option == "1":
        search_function.get_user_info()
    elif option == "2":
        pass
    elif option == "3":
        break
    else:
        print("输入的数字无效")