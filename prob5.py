# ### Python program to swap two numbers
# # using third variable
# X = int(input("Please enter x here: "))
# Y = int(input("Please enter y here: "))
# temp = X
# x = Y
# y = X
# print(f"The value of {X} and {Y} after swapping is ", x,y)


# without using third variable
X = int(input("Please enter x here: "))
Y = int(input("Please enter y here: "))
x, y = Y, X
print(f"The value of {X} and {Y} after swapping is ", x,y)