num1 = int(input("enter your number 1: "))
num2 = int(input("enter your number 2: "))
num3 = int(input("enter your number 3: "))

if(num1 > num2 and num1>num3):
    print("Greatest number is: ", num1)
elif(num2 > num1 and num2>num3):
    print("Greatest number is: ", num2)
else:
    print("Greatest number is: ", num3)