# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.odometer = 0
#         self.gas_tank_size = 0

#     def get_describe_car(self):
#         long_name = f"{self.year} {self.brand} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"车的里程为{self.odometer}")

#     def update_odometer(self,mileage):
#         if mileage >= self.odometer:
#             self.odometer = mileage
#         else:
#             print("你不能减小车的里程数")

#     def increase_odometer(self,increase_mileage):
#         self.odometer += increase_mileage

#     def fill_gas_tank(self,gas_tank):
#         if gas_tank != 0:
#             self.gas_tank_size = gas_tank
#             print(f"车的油箱容量为{self.gas_tank_size}L")
#         else:
#             print("该车还没有加装油箱")


# class ElectricCar(Car):
#     def __init__(self, brand, model, year):
#         super().__init__(brand, model, year)
#         self.battery = Battery() #下面那个class 自动创建一个实例 将实例赋值给属性

#     def show_battery_size(self):
#         if self.battery_size != 0:
#             print(f"电池的容量为{self.battery_size}")
#         else:
#             print("该车暂时无电池装备")

#     def fill_gas_tank(self, gas_tank):
#         print("电车没有油箱")

# class Battery:
#     def __init__(self,battery_size=40):
#         self.battery_size = battery_size
    
#     def show_battery_size(self):
#         print(f"电池容量为{self.battery_size}")

#     def get_range(self):
#         self.range = self.battery_size*3
#         print(f"车的里程为{self.range}")

#     def change_battery_size(self,new_battery_size):
#         self.battery_size = new_battery_size

# electriccar1 = ElectricCar("byd","qin","2025")

# electriccar1.battery.change_battery_size(65)
# electriccar1.battery.show_battery_size()
# electriccar1.battery.get_range()
