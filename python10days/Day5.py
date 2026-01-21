#list 
#operation-> indexing
#methos ->default

# List Syntax List[]

task=["eat","code","sleep","eat"]
print(type(task))
print(task)

task.append("repeat")
print("append " , task)
print("eat Count ", task.count("eat"))
task.insert(3,"dream")
print(task)
task.remove("eat") # remove only first eat not all eat word
print(task)
task.sort()  
print("sort" ,task)
task.extend("wake")
print("extend" ,task)
for i in task:
    # print(i)
    if i=="code":
        print(i," task is running")
    else:
        print(i,"Task is over")
task.reverse()
print("reverse" , task)
print("index", task.index("code"))
print("Pop " ,task.pop(3))
print(task)
task.clear()
print(task)