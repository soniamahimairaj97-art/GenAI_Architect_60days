#set

numbers = {1,2,3,4}
print("OG  numbers " , numbers)
print(type(numbers))
numbers.remove(3)
print("Remove " , numbers)
numbers.add(5)
print("Add " , numbers)
print("Length" , len(numbers))

#set 2 

fruits = {"apple","orange","banana","tomato"}
veggies ={"onion","carrot","beans","tomato"}
print(type(fruits))
dry_fruits=fruits.copy()
print("copy :" ,dry_fruits)
fruits.add("berry")
print("add : ", fruits)
print("diff : " ,fruits.difference(veggies))
fruits.remove("apple")
print("remove : " , fruits)
# fruits.pop("orange") TypeError: set.pop() takes no arguments (1 given)
fruits.discard("orange")
print("Discard : " ,fruits)
fruits.clear()

#Dict

student = {"name":"soni","age":29,"grade":"10th"}
staff = {"name": "DD", "designation":"SE" ,"gender": "male"}
print(type(student))
admin=student.copy()
print(admin)
print("name : " ,student["name"])
print("age : ", student["age"])
print("grade : " , student["grade"])
print("get age  : " ,student.get("age")) 
student["age"]=32
print("update : " ,student)
student["gender"]="Female"
print("add " , student)
student.update(staff)
print("update : " ,student)
print("pop key " ,student.pop("name")) #  removes the item associated with a specified key and returns the corresponding value
#print("pop value ",student.pop("soni") ) #  value is not retrivable
del student["grade"]
print("remove : " , student)
print("clear : ",student.clear())
print("student :",student)
print("admin :", admin)