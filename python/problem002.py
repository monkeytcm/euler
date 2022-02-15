fibonnaci = [1, 2]
sum = 0

def fib (arr) :
    return arr[-1] + arr[-2]

while fib(fibonnaci) < 4000000:
    fibonnaci.append(fib(fibonnaci))

for i in fibonnaci:
    if i % 2 == 0:
        sum += i
print(sum)

