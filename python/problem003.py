prime = 1
factors = 1

number = 600851475143

def isPrime (v):
    prm = True
    for i in range(2, v):
        if  v % i == 0:
            prm = False
    return prm

#print(isPrime(5))

for i in range(1, number, 2):    
    if number % i == 0 and isPrime(i) and i > prime:
        print("current:" + str(i))
        prime = i
        factors *= prime
    elif factors >= number:
        print("result: " + str(prime))
        exit() 




