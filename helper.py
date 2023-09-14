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