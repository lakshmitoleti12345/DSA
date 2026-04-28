# 🔹 Problem 1: Count number of 1’s in binary

n = 7

# Method 1: Using built-in
print(bin(n), bin(n).count('1'))

# Method 2: Bit manipulation (better)
count = 0
temp = n
while temp:
    count += temp & 1
    temp >>= 1
print("Count of 1s:", count)


# 🔹 Problem 2: Power of Two
def power_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(power_two(16))   # True
print(power_two(18))   # False


# 🔹 Problem 3: Power of Four
def isPowerOfFour(n):
    return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

print(isPowerOfFour(4))   # True
print(isPowerOfFour(8))   # False


# 🔹 Problem 4: Power of Three
def power_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

print(power_three(27))   # True
print(power_three(10))   # False