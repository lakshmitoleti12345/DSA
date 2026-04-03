# n=15
# if n%5==0 and n%10!=0:
#     print("satisfied")
# else:
#     print("not satisfied")
# def is_divisible(n):
#     if n%5==0 and n%10!=0:
#         print("satisfied")
#     else:
#         print("not satisfied")

# is_divisible(10)
def is_divisible(n):
    return n%5==0 and n%10!=0
print("satisfied" if(is_divisible(25)) else "not satisfied")
