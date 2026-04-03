#area of square
# area=side* side
#create a variable side
#input from user -side
# input store it in variable
#area=side* side
#1 brutefore code
# side=float(input("enter side of square="))
# area=side*side
# print("area of square=",area)
#optimised for reusebility
# use functions for reusebility
# def area_square(side):
#     return side*side
# side=float(input("enter side of square="))
# print(area_square(side))
# def area_square():
#     side=float(input("enter side of square="))
#     return side*side

# print(area_square())
# reduce the time we use side**2
def area_square():
    side=float(input("enter side of square="))
    return side**2

print(area_square())
