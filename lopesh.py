#whileloops
# i=1
# while i<6:
#   print(i)
#   i += 1

#wap to perint 1-100

# i=1
# while i<=100:
#   print(i)
#   i += 1

#wap to print 100 to 1

# i=100
# while i>=1:
#   print(i)
#   i -= 1

#print multiplaction table of a number n

# n= int(input("Enter an number: "))
# i=1
# while i<=10:
#   print(n*i)
#   i +=1

#wap to print elments in following loop
# i=1
# while i<=10:
#   print(i*i)
#   i += 1

#wap to search number x in tuple using llop
# tuop = (1, 4, 9,16,25,36,49,81,100)
# k=len(tuop)
# x = int(input("enter x: "))
# i=0
# while i<=k-1:
#   if x == i:
#     print("nmber found :",x)
#   i+=1

#Break -used to terminate the loop when encountered
#Continue

#for 
# str= "apnacollege"
# for char in str:
#   if(char =='o'):
#     print("fountd")
#     break
#   print(char)

#print elemebts of following loop
# tp = [1, 4, 9,16,25,36,49,81,100]
# k = len(tp)
# i=0
# for i in tp:
#   print(i)

#serch for num x in tuplw using llop
# tp = [1, 4, 9,16,25,36,49,81,100]
# i=0
# x= int(input("en num: "))
# for i in tp:
#   if(i==x):
#     print("found")
#     break
# print('not found')

#range returns sequenc of nums stating from 0 by default and incremnts by 1 and stops at specified number rand(start?,stop,step?)
# for i in range(1,100,1):
#   print(i)

# for i in range(100,1,-1):
#   print(i)

# n=int(input("enter anum : "))
# for i in range(1,11):
#   print(n*i)

#pass is a null statement that does nothing. it is used as placeholder for future code

#find sum of first n numbers
# n=int(input("enter anum : "))
# i=0
# sum=0
# while i<=n:
#   sum+=i
#   i+=1
# print(sum)

# n=7
# sum=0
# for i in range(1,n+1):
#   sum+=i

#find factorial of n
# n=int(input("enter anum : "))
# fact=1
# for i in range(1,n+1):
#   fact*=i
# print('fact is:',fact )