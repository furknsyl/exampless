##largest prime

def prime(n):
    x = []
    for num in range(1, n + 1):  
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break  
            else:
                x.append(num)
    return x



n  = 600851475143

primes = prime(10000)

for x in primes:
    if n % x == 0:
        print(x) 