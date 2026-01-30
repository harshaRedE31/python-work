num1= int(input("Enter a number1 : "))
num2= int(input("Enter a number2 : "))
num3= int(input("Enter a number3 : "))
if(num1>num2 and num1>num3):
  print("Greatest number is num1", num1)
elif(num2>num1 and num2>num3):
  print("Greatest number is num2", num2)
else:
  print("Greatest number is num3", num3)