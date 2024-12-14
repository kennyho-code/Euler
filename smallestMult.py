def smallestMultiple(limit):
  res = {}
  for i in range(2, limit + 1):
    currentNum = i
    for(j) in range(2, i + 1):
      count = 0 
      while(currentNum % j == 0):
        currentNum //= j
        count += 1
      val = res.get(j, 0)
      res[j] = max(val, count)
  resval = 1
  for k, v in res.items():
    resval *= k ** v

  return resval




print(smallestMultiple(20))