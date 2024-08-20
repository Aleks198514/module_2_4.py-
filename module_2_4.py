numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primeNum = []
nonPrimeNum = []
for num in numbers:
    if num == 1:
        continue
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        primeNum.append(num)
    else:  #
        nonPrimeNum.append(num)
print("Простые числа:", primeNum)
print("Составные числа:", nonPrimeNum)
