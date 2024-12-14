
def pythagorean_triplet():
    max_num = 1000
    for a in range(max_num):
        a2 = a ** 2
        for b in range(a + 1, max_num):
            b2 = b**2
            for c in range(b + 1, max_num):
                left = a2 + b2
                right = c**2
                if left == right and (a + b + c) == 1000:
                    print(f'found triplet: {a}, {b}, {c}')
                    print(f'sum is: {a + b + c}')
                    print(f'answer is: {a*b*c}')
                    return
    print("couldn't find answer")


def main():
    pythagorean_triplet();

main()
