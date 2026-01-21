# a=5
# b=10


# def add(a,b):
#     c=a+b
#     return c

# print("add" ,add(a,b))


# def add_avg(a,b):
#     return add(a,b)/2

# print("avg" ,add_avg(a,b))


#assignment task 

# Function for simple if control flow
def check_amount(amt):
    if amt == 30:
        print("drink tea")
    else:
        print("Go home")


# Function for if-elif-else control flow
def check_rate(rate):
    if rate == 30:
        print("tea available")
    elif rate == 20:
        print("Bajji")
    elif rate == 40:
        print("pongal")
    else:
        print("Go Home")


# Function for nested if control flow
def check_price(price, food=None):
    if price == 30:
        if food == "dosai":
            print("ordered Dosa")
        else:
            print("Ordered Pongal")
    else:
        print("Get Menu")

# Example calls
amt = int(input("Enter the amount: "))
check_amount(amt)

rate = int(input("Enter the rate: "))
check_rate(rate)

price = int(input("Enter the price: "))
if price == 30:
    food = input("Enter food (dosai or pongal): ")
    check_price(price, food)
else:
    check_price(price)