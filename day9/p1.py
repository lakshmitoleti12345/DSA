#METHOD 1
#spacae complexity=1+1+1=O(1)
#time complexity =3+1,4+n=O(N)
n=121
m=n
res=0
while n>0:
    temp=n%10
    res=res*10+temp
    n=n//10
if res==m:
    print("pallindrome")
else:
    print("not palindrome")
#-----------------------------------------------
#METHOD 2
#space complexity=1+n+1=2+n=O(N)
#time complexity=3+1=O(N)
n=121
s=str(n)
res=''
for i in s:
    res=i+res
if n==int(res):
    print('pallindrome')
else:
    print('pallindrome')
#----------------------------------------------
#METHOD 3
#space complexity=1+n+1+1=O(N)
#time complexity=n/2+1=O(N)
def pal():
    n=121
    s=str(n)
    left=0
    right=len(s)-1
    while(left<=right):
        if s[left]!=s[right]:
            print('not palindrome')
            return
        
        left+=1
        right-=1
    print('palindrome')
pal()
        

