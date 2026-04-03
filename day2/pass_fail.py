# marks=[23,55,37]
# count=0
# for i in marks:
#     if i<35:
#         count+=1
# if count>0:
#     print("fail")
# else:
#     print("pass")
# def is_pass(marks:list):
#     return any([i<35 for i in marks])
# print("fail" if(is_pass([77,55,67])) else "pass")
#optimized
def is_pass(marks:list):
    return any([i>35 for i in marks])
print("pass" if(is_pass([77,15,17])) else "fail")
#brute force
marks=[14,20,38]
count=0
for i in marks:
    if i>35:
        count+=1
if count>=1:
    print("pass")
else:
    print("fail")


