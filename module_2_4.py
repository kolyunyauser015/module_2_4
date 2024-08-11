numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    for j in range(2, (i // 2) + 1):
    # достаточно делители проверить до половины числа
        if i % j != 0:
            is_prime = True
        else:
            is_prime = False
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)
