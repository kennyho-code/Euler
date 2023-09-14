from helper import sumOfDivisors

def sumMultiples3or5(target: int):
  return sumOfDivisors(target, 3) + sumOfDivisors(target, 5) - sumOfDivisors(target, 15)
  


print(sumMultiples3or5(1000))
# assert sumMultiples3or5(10) == 23, "target 10, result should be 23"
assert sumMultiples3or5(1000) == 233168, "target 1000, result should be 233168"
