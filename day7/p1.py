#you are at step 0 you want to reach step n you can move 
#1 step 
#2 steps
#how many different ways you reach the top?
n=6
count=0
def step(total=0):
    global count
    if total==n:
        count+=1
        return
    if total>n:
        return
    step(total+1)
    step(total+2)
step()
print(count)
print("------------------🌸🌸🌸🌸🌸🌸---------------")

print(step(5))
print('----------------------------')
def step(n):
    if n==1 or n==0:
        return 1
    return (step(n-1)+step(n-3))
print(step(5))