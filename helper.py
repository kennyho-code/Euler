def sumOfDivisors(target: int, divisor: int):
  numDivisors = target // divisor

  lastTerm = numDivisors * divisor
  if(target % divisor == 0):
    lastTerm = target - divisor
    numDivisors -= 1
  

  return numDivisors * (divisor + lastTerm) / 2


assert sumOfDivisors(10, 3) == 18, "1, 2, 3, 4 should equal to 18"