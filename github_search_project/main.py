import search_function
import display

while True:
    print(
        "1.查询用户基本信息\n"
        "2.查询用户全部信息\n"
        "3.查看查询操作的状态码\n"
        "4.退出\n"
    )
    option = input("请选择要执行的操作： ")  
    if option == "1":
        username = input("请输入查询的用户名： ")
        display.get_user_info(username=username)
    elif option == "2":
        username = input("请输入要查询所有信息的用户名称： ")
        display.show_all_info(username=username)
    elif option == "3":
        username = input("请输入要查询的用户名 的查询状态")
        display.status_code(search_username=username)
    elif option == "4":
        break
    else:
        print("输入的数字无效")