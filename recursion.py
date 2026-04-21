#1 to 10
def func(n):
    if n==10:
        print(n)
        return
    print(n)
    func(n+1)
func(1)
#10 to 1
def func(n):
    if n==1:
        print(n)
        return
    print(n)
    func(n-1)
func(10)
# factorial of 7
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(7))
# sum of digits
def sum_d(n,sum=0):
    if n==0:
        print(sum)
        return 
    d=n%10
    sum+=d
    sum_d(n//10,sum)
# sum of digits
sum_d(567)
def sum_d(n,sum=0):
    if n==0:
       return sum
    return sum_d(n//10,sum+n%10)
print(sum_d(567))
#reverse num
# def rev_num(n):
#     rev=0
#     while n>0:
#         d=n%10

#         rev=rev*10+d
#         n//=10
#     print(rev)
# rev_num(12340)
# def reverse_number(n: int) -> int:
#     # Preserve the sign
#     sign = -1 if n < 0 else 1
#     n = abs(n)

#     reversed_num = 0
#     while n > 0:
#         digit = n % 10               # Extract last digit
#         reversed_num = reversed_num * 10 + digit
#         n //= 10                     # Remove last digit

#     return sign * reversed_num

# # Example
# print(reverse_number(1230))   # Output: 321
# def reverse_with_leading_zero(n: int) -> str:
#     # Convert to string, reverse it, and return
#     return str(n)[::-1]

# Example
# print(reverse_with_leading_zero(1230))   # Output: '0321'
def rev_number(n,rev=0):
     
    if n==0:
        return rev
    return rev_number(n//10,rev*10+n%10)
print(rev_number(123))
#pallindrome
def rev_number(n, rev=0, original=None):
    if original is None:   # store the original number once
        original = n

    if n == 0:
        if rev == original:
            return "Palindrome"
        else:
            return "Not Palindrome"

    return rev_number(n // 10, rev * 10 + n % 10, original)

# Examples
print(rev_number(12221))   # Palindrome
print(rev_number(12321))   # Palindrome
print(rev_number(12345))   # Not Palindrome



