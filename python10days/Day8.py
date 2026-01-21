#Function Greet

name=str(input("Enter ur name : "))

def greet(name):
    print("Welcome to the SE ",name)
    #or
    print(f"Welcome to the SE {name}")

#Function Calculator

A=int(input("Enter the first value : "))
B=int(input("Enter the second value : "))

def add(A,B):
    return A+B 

def sub(A,B):
    return A-B 

def multi(A,B):
    return A*B 

def div(A,B):
    return A/B 

def mod(A,B):
    return A%B 

def floor_div(A,B):
    return A//B 

def exponent(A,B):
    return A**B

print("add" , add(A,B))
print("sub" , sub(A,B))
print("multi" , multi(A,B))
print("div" , div(A,B))
print("mod" , mod(A,B))
print("floor_div" , floor_div(A,B))
print("exponent" , exponent(A,B))



