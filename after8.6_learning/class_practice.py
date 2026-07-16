#9.1 and 9.4
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"the name of restaurant is {self.restaurant_name}")
        print(f"the style of restaurant is {self.cuisine_type}")
        print(f"the restaurant have served {self.number_served} people")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now opening!")

    def set_number_served(self,number):
        if number <= self.number_served:
            print("wrong you can't reduce the number")
        else:
            self.number_served = number

    def increment_number_served(self,increase_number):
        if increase_number > 0:
            self.number_served += increase_number
        else:
            print("the number < 0")

# restaurant1 = Restaurant("水边","小酒馆")

# restaurant1.set_number_served(247)
# restaurant1.increment_number_served(2)
# restaurant1.describe_restaurant()
# restaurant1.open_restaurant()



#9.3 and 9.5
class User:
    def __init__(self,first_name,last_name,**kwargs):
        self.kwargs = kwargs
        self.kwargs["first_name"] = first_name
        self.kwargs["last_name"] = last_name
        self.login_attempts = 0

    def greet_user(self):
        print(f"Hello {self.kwargs["first_name"]} {self.kwargs["last_name"]}")

    def user_infomation(self):
        print(f"{self.kwargs["first_name"]}{self.kwargs["last_name"]}的信息为")
        for key,value in self.kwargs.items():
            print(f"{key} -- {value}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# user1 = User("sam","froest",age=24,location="china",job="none")
# for i in range(4):
#     user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.reset_login_attempts()
# print(user1.login_attempts)

        
