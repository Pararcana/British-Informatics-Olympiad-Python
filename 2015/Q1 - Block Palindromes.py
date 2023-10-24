def permutations(n, total, limit, parity):
  if n != limit:
    for i in range(1, length):
      if length > total + 2*i and i != 0:
        spl[n], spl[-n-1] = i, i
        permutations(n + 1, total + 2*i, limit, parity)
  else:
    if parity:
      spl[(len(spl)-1)//2] = length - (sum(spl)-spl[(len(spl)-1)//2])
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

palindrome = input("Enter a string: ")
length = len(palindrome)
total = 0

for i in range(2, length + 1):
  if length%2==0 or (length%2!=0 and i%2!=0):
    spl = [0] * i
    comb = []
    permutations(0, 0, (i-1)//2, i%2!=0)
    for v in comb:
      if checkPalindrome(splitter(v)):
        total += 1
print(total)
