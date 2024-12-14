import math
def primeFactors(n: int):
  limit = math.floor(math.sqrt(n))
  candidates = [False, False] + [True for i in range(2, limit + 1)]
  for i in range(2, len(candidates)):
    for j in range(i + i, len(candidates), i):
      candidates[j] = False

  res = None
  for i in range(len(candidates)):
    if(candidates[i] and n % i == 0):
      res = i
  return res
    


# primeFactors(20)
assert primeFactors(600851475143) == 6857