from math import sqrt, ceil

def summation_primes(limit):
    universe = [True] * (limit + 1)
    universe[0] = False
    universe[1] = False
    boundary = ceil(sqrt(limit))
    for n in range(2, boundary):
        for m in range(n + n, limit + 1, n):
            universe[m] = False
    res = 0
    for n in range(len(universe)):
        if universe[n]:
            res += n
    print(f'answer: {res}')
    return res


def main():
    summation_primes(2000000)

main();
