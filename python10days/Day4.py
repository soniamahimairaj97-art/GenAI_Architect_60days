# Loop 

for i in range(0,10):
    print("Range : " , i)

list_day4 = ['a','b','c',34,3.45]
for i in list_day4:
    print("List day 4" , i)

#assignment define dictionary

students_score ={
    "name" : "soni",
    "age":27,
    "score":90
}
print(type(students_score))
print(students_score)

# manoj Example define dict

student_score={
    "Alice":95,
    "banu":82,
    "charlie":67,
    "diana":74
}
for name,score in student_score.items():
#  print(student_score)
 print(f"{name} scored {score}")

#converting two list into dictionaly and loop

name = ["soni" , "suba" ,"megha" ,"banu" ,"sneha",]
score= [84,74,64,95,66]

student_score= dict(zip(name,score))
print(student_score)

for name,score in student_score.items():
    print(f"{name} scored : {score}")
