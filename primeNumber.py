
def isPrime(n: int):
    for m in range(2, n):
        if (n % m == 0):
            return False
    return True


def primeNumber(n: int):
    numPrimes = 0
    currentPrime = 2
    currentNum = 2

    while numPrimes < n:
        if (isPrime(currentNum)):
            currentPrime = currentNum
            numPrimes += 1
        currentNum += 1
    return currentPrime


print(primeNumber(10001))
