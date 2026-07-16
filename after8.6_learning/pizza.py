
def make_pizza(size,*toppings):
    print(f"the pizza is {size} size\n")
    print("the toppings with pizza are")
    for topping in toppings:
        print(f"- {topping}")
