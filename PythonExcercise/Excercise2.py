#List 

fruits =["apple","banana","Mango"]

print(type(fruits))
print("OG List ",fruits)  #Orginal 

fruits.append("Strawberry") # List append
print("Append" ,fruits)

fruits[1]="grape"  #Change item at index /Replace item
print("index /Replace",fruits)

print(" get Indexing" ,fruits[2]) # access item at position

fruits.remove("apple") #remove an item 
print("Remove ", fruits)

print("Length",len(fruits)) # Length of List

# fruits.Clear
# fruits.copy
# fruits.count
# fruits.extend
# fruits.index
# fruits.insert
# fruits.pop
# fruits.remove
# fruits.reverse
# fruits.sort



print("Clear"  )


#Tuples

colors=("red","blue","green")

#colors.append("yellow")
#print("Append " ,colors)

print("get " ,colors[2])

#colors[1]="gold"
#print("Remove ", colors.remove("red")) Tuple has no remove

print(len(colors))


# get the Datatype 
name= "sonia"
age=27

print("name",type(name))

print("age ", type(age))

print("Colors " ,type(colors))

print("fruits ",type(fruits))
