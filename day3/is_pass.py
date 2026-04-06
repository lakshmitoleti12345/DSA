#in three subjects lo any one subject marks is 
# less than 35 print fail
def is_pass(marks:list):
    return any([True for i in marks if i<35])
print("Fail" if is_pass([34,39,70])else "pass")
#in three subjects lo any one subject marks
#  is greater than 35 print pass
def is_pass(marks:list):
    return any([True for i in marks if i>35])
print("pass" if is_pass([10,20,36])else "fail")