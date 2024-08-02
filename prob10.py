# Python program to find average of N numbers
num = int(input("Please enter a number here : "))  # 3
sum = 0
for i in range(num):
    numbers = float(input("Enter a number: "))  # 5 , 10, 15
    sum += numbers  # 5 ,15, 30
avg = sum/num
print("The average of these numbers is : ", avg)
