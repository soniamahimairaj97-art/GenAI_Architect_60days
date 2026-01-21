skill={"python","GIT","PYTHON","python"}

print("skill",skill)

required={"python","SQL","AI"}

print("required",required)

# Intersection (elements in both A and B)
common=(skill & required)
print("Intersection " , common)

# Union (elements in A or B)
common =(skill | required)
print("Union ",common)

# Difference (elements in A but not in B)
common=(skill - required)
print("Difference ", common)

# Symmetric Difference (elements in A or B but not both)
print("Symmetric Difference:" , skill ^ required)


frozen =frozenset(skill)
print("frozen " ,frozen)

#creating frozen set 

fs= frozenset([1,2,3,4,1])
print("frozen ", fs)

#loop through frozenset
print("Loop through frozen ")

for item in fs:
    print(item)

#using frozenset in operation 

A=frozenset([1,2,3])
B=frozenset([3,4,5])

print("union ", A|B)
print("Interscetion ",A&B)
print("Diff ", A-B)
print("Symm ", A^B)