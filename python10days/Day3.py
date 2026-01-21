#conditional operator

# score =int(input("enter your score : "))

# if score<0 or score>100 :
#     print("enter valid score")
# elif score>=90 :
#     print("A+")
# elif score>=80:
#     print("B")
# elif score >=70:
#     print("C")
# else:
#     print("FAIL")


#Nested condition

# age = int(input("enter your age : "))



# if age>=18 :
    
#     # pro= str(input("enter sub type : "))
#     pro= input("enter sub type : ")
#     if pro == "Yes":
#         print("FULL ACCESS")
#     else:
#         print("LEARN MODE")
# else :
#     print("Junior Level access granted ")

# #terinary operator

# status = "Adult" if age>=18 else "Minor"

# print(status)


# Define a dictionary
student_scores = {
    "Alice": 95,
    "Bob": 82,
    "Charlie": 67,
    "Diana": 74
}

# Iterate through dictionary using for loop
for score, name in student_scores.items():
    if name >= 90:
        grade = "A+"
    elif name >= 80:
        grade = "B"
    elif name >= 70:
        grade = "C"
    else:
        grade = "FAIL"
    
    print(f"{name} scored {score} → Grade: {grade}")