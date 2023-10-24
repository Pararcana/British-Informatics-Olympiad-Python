def permutations(n, total, limit, parity):
  if n != limit:
    for i in range(1, length):
      if length > total + 2*i and i != 0:
        spl[n], spl[-n-1] = i, i
        permutations(n + 1, total + 2*i, limit, parity)
  else:
    if parity:
      spl[(len(spl)-1)//2] = length - (sum(spl)-spl[(len(spl)-1)//2])
      comb.append(spl.copy())
    else:
      midSum = (length - (sum(spl) - (spl[(len(spl)-1)//2] + spl[len(spl)//2])))//2
      spl[len(spl)//2], spl[(len(spl)-1)//2] = midSum, midSum
      comb.append(spl.copy())

def splitter(splArr):
  counter, outArr = 0, []
  for v in splArr:
    outArr.append(palindrome[counter : counter + v])
    counter += v
  return outArr

def checkPalindrome(arr):
  parts = []
  for v in arr:
    if v not in parts:
      parts.append(v)
  
  compressed = []
  for v in arr:
    compressed.append(parts.index(v))
  return compressed == list(reversed(compressed))
