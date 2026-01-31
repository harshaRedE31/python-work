# # Basic function
# def greet(name):
#   return f"Hello, {name}!"

# # Function with default parameter
# def add(a, b=0):
#   return a + b

# # Function with multiple return values
# def divide_and_remainder(a, b):
#   quotient = a // b
#   remainder = a % b
#   return quotient, remainder

# # Function with *args (variable positional arguments)
# def sum_all(*numbers):
#   return sum(numbers)

# # Function with **kwargs (variable keyword arguments)
# def print_info(**info):
#   for key, value in info.items():
#     print(f"{key}: {value}")

# # Lambda function (anonymous)
# square = lambda x: x ** 2

# # Using the functions
# print(greet("Alice"))
# print(add(5, 3))
# q, r = divide_and_remainder(17, 5)
# print(sum_all(1, 2, 3, 4, 5))
# print_info(name="Bob", age=30, city="NYC")
# print(square(4))

#waf to print length of a list
# nums = [1,3,3,4,53,2,1]
# def lengthoflsi(nums):
#   print(len(nums))
#   return len(nums)
# lengthoflsi(nums)

#waf to print elmets of list in single line
# nums = [1,3,3,4,53,2,1]
# def printliste(nums):
#   for i in nums:
#     print(i, end=" ")
# printliste(nums)

#waf to find factorial of n

# def factorial(n):
#   factl=1
#   for i in range(1,n+1):
#     factl *= i
#   print("factporial is",factl)
# factorial(0)

#usd to inr
# def converter(usdval):
#   inrval = usdval * 89
#   print(usdval, "Usd = ", inrval, "Inr")
# converter(39)

#Recursion - when a function calls itself repeatedly
# def show(n):
#   if(n==0):
#     return
#   print(n)
#   show(n-1)
# show(8)

# def fact(n):
#   if(n==0 or n==1):
#     return 1
#   else:
#     return n*fact(n-1)
# print(fact(8))

# def sumofn(n):
#   if(n==0):
#     return 0
#   return sumofn(n-1) + n
# print(sumofn(10))

def printlis(list, idx=0):
  if(idx == len(list)):
    return
  print(list[idx])
  printlis(list, idx+1)

letters = [1,2,3 ]
printlis(letters)
