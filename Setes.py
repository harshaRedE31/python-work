#set is collection of unordered items, each elemetn iin set must be unique and immutable
#set is mutable
collection = {1,2,2,3,4,"hi","oo",8}
print(collection)
print(type(collection))
print(len(collection))

#create empty set
tion = set()
tion.add(1)
tion.add("oop")
tion.add(90)
tion.add(1)
tion.add(9)
tion.add(10)
# tion.remove(1)

# print(tion.pop())
print(type(tion))
print(tion)
#set methiods

print(collection.intersection(tion))