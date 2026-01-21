#Dict{Key:Value} key is immutable(mostly string)

profile={
    "name":"soni",
    "age":26,
    "score":98
}

print(type(profile))
print(profile)
profile["age"]+=2
print(profile["age"])
print(profile)


#Multi dict Merge and update 

data1={
    "a":10,
    "b":20
}

data2={
    "b":60,
    "c":70
}
print("data1 " ,data1)
print("data2 " ,data2)
data1.update(data2)
print("data1 " ,data1)
print("data2 " ,data2)


#dict 

dict1 = {"name": "Alice"}
dict2 = {"age": 25,"city": "chennai"}
dict3 = {"city": "Bengaluru"}
dict4 = {"city": "kerala"}

# Merge all three
merged = {**dict1, **dict2, **dict3 ,**dict4}

print(merged)
