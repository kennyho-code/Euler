def sumMultiples3or5(target: int):
  res = 0
  for i in range(target):
    if(i % 3 == 0 or i % 5 == 0):
      res += i
  return res


assert sumMultiples3or5(10) == 23, "target 10, result should be 23"
assert sumMultiples3or5(1000) == 233168, "target 10, result should be 233168"
