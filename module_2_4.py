numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_Primes = []
k = 0
for i in numbers:
    for g in range(2, i+1):
        if i % g == 0:
            k = k + 1
            if k == 2:
                break
    if k > 1:
        Not_Primes.append(i)
    elif k == 1:
        Primes.append(i)
    k = 0
print('Primes:', Primes)
print('Not Primes:', Not_Primes)
