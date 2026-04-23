#Take a list of some numbrs 
#give me a new list with the next number after combining all numbers in a list
lst=[3,7,9]
num=0
for i in lst:
    num=num*10+i
num+=1
result=[]
while num>0:
    d=num%10
    result+=[d]
    num=num//10
print(result[::-1])
