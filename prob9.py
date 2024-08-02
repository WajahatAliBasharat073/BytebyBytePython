# Python program to check given number is a Prime Number or Not
num = int(input("Please enter a number "))  # 11
if num == 1:
    print(num, "is not a prime number ")
else:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number ")
                break
        else:
            print(num, "is a prime number ")
