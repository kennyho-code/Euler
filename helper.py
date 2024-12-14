import math 
def sumOfDivisors2(target: int, divisor: int):
  numDivisors = (target) // divisor
  lastTerm = numDivisors * divisor
  if(target % divisor == 0):
    lastTerm = target - divisor
    numDivisors -= 1
  

  return numDivisors * (divisor + lastTerm) / 2



def sumOfDivisors(target:int, divisor: int):
  p = (target - 1) // divisor

  return (divisor * p * (p + 1)) / 2

assert sumOfDivisors(10, 3) == 18, "1, 2, 3, 4 should equal to 18"
assert sumOfDivisors(1000, 3) == 166833, "3 should equal to 18"
assert sumOfDivisors(1000, 5) == 99500.0, "5 should equal to 18"
assert sumOfDivisors(1000, 15) == 33165, "15 should equal to 18"


def fibonacciGenerator():
  prev = 1
  current = 1
  while(True):
    prev, current = current, prev + current
    yield prev


def getPrimes(n: int):
  candidates = [False, False] + [True for i in range(2, n)]
  for i in range(2, len(candidates)):
    for j in range(i + i, len(candidates), i):
      candidates[j] = False
  factors = []
  for i in range(len(candidates)):
    if(candidates[i]):
      factors.append(i)
  return factors

