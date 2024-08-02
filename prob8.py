# Python program to Find the Largest Among Three Numbers
num1 = int(input("please enter a 1st number here"))  # 2
num2 = int(input("please enter a 2nd number here"))  # 1
num3 = int(input("please enter a 3rd number here"))  # 3
if num1 > num2 and num1 > num3:
    print("num1 is the largest number")
elif num2 > num1 and num2 > num3:
    print("num2 is the largest number")
else:
    print("num3 is the largest number")
