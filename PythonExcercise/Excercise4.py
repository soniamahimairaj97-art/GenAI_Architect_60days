#Control flow If

amount = int(input("enter the amount : "))
if amount==30:
    print("drink tea")
else:
    print("Go home")

#Control flow elif

rate=int(input("Ente the Rate : "))
if rate==30:
    print("tea available")
elif rate==20:
    print("Bajji")
elif rate==40:
    print("pongal")
else:
    print("Go Home")

#Netsed If 

price=int(input("enter the price : "))
if price==30:
    food=str(input("dosai or pongal"))
    if food=="dosai":
        print("ordered Dosa")
    else:
        print("Ordered Pongal")
else:
    print("Get Menu ")
