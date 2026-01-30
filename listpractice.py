#lists are mutable, whears tuple cant and alos string also
student= ["kaff", 95, "io", 0]
print(student)
print(student[0])
student[0]="harsha"
print(student)

#list slicing
marks=[9,4,35,88,99]
print(marks[1:3])
print(marks[2:5])
print(marks[-5:-2])
print(marks[::-1])

#list methods
list = [2,1,4,5]
list.reverse()
print(list)
list.append(9)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.insert(3,89)
print(list)
list.remove(9)
print(list)
list.pop(2)
print(list)