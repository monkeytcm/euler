import math

palindrome = 0

def isPalindrome (v) :
    vStr = str(v)
    result = True
    for i in range(0, math.floor(len(vStr) / 2 )):
        if(vStr[i] != vStr[-(i + 1)]):
            result = False
    return result


for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindrome(i * j) and i * j > palindrome:
            palindrome = i * j

print(palindrome)