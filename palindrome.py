import time

def palindrome(digits): 
  maxNum = 10 ** digits - 1
  res = 0
  for i in range(1, maxNum):
    for j in range(i, maxNum):
      candidate = str(i * j)
      mid = len(candidate) // 2
      start = candidate[:mid]
      end = candidate[mid:]

      # print(start, end, mid, candidate)
      if(start == end[::-1] and i * j > res):
        res = i * j
      # print(start + ' | ' + end)
  return res


def backWardsPalindrome(digits): 
  maxNum = 10 ** digits - 1
  res = 0
  for i in range(maxNum, -1, -1):
    for j in range(i, -1, -1):
      candidate = str(i * j)
      mid = len(candidate) // 2
      start = candidate[:mid]
      end = candidate[mid:]

      # print(start, end, mid, candidate)
      if(start == end[::-1] and i * j > res):
        res = i * j
      # print(start + ' | ' + end)
  return res


def palindromeOfDigits(digits): 
  n = int('1' * digits)
  res = n ** 2
  end = (1 * 10 ** (digits)) -1
  for i in range(end, n, - 1):
    for j in range(i, n, - 1):
      # print(i, j)
      candidate = str(i * j)
      cmid = len(candidate) // 2
      cstart = candidate[:cmid]
      cend = candidate[cmid:]

      if(cstart == cend[::-1] and i * j > res):
        res = i * j
  return res

# print(palindrome(4))

# for i in range(10, 5, -1):
#   for j in range(i, 5, -1):
#    print(i, j)