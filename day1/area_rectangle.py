#find area of rectangle
#length * breadth
# brute force code
# l=float(input("enter length="))
# b=float(input("enter breadth="))
# area=l*b
# print("area of rectangle=",area)
# for dsa optimised code
# def area_rec(l,b):
#     return float(l)*float(b)

# print(area_rec(7,9))
def area_rec(l:float,b:float):
    if l==0 or b==0:
        return "invalid inputs"
    return l*b
print(area_rec(8,0))


