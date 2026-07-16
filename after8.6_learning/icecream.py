from class_practice import Restaurant,User

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []

    def add_flavors(self,*args):
        self.flavors.extend(args)

    def show_flavors(self):
        if self.flavors:
            # print(f"冰淇淋的口味有 {self.flavors}") 这是我写的
            print(f"冰淇淋的口味有{','.join(self.flavors)}")
        else:
            print("暂时未添加口味")
# shop1 = IceCreamStand("冰淇淋小屋","ice cream")
# shop1.add_flavors("香草","草莓","西瓜","酸奶")
# shop1.show_flavors()

class Admin(User):
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.privileges = self.kwargs.pop("privileges",[]) #后面那个空列表是为了防止没有特权而代码崩盘

    def show_privileges(self):
        if self.privileges:
            print(f"Admin 的特权有:{self.privileges}")
        else:
            print("没有特权")

admin1 = Admin("sun","flower",location="linyi",age=25,privileges=["can add post","can delete post","can ban user"])
basic_admin2 = Admin("no","admin",age=32)
admin1.show_privileges()
basic_admin2.show_privileges()
