from helper import fibonacciGenerator



def calculateEvenFib(limit: int):
  gen = fibonacciGenerator()
  current = 0
  sum = 0 
  while(current < limit):
    if(current % 2 == 0):
      sum += current
    current = next(gen)
  return sum


assert(calculateEvenFib(10) == 10, "2 + 8 should equal to 10")
assert(calculateEvenFib(4000000) == 4613732, "fib less than 4000000")

