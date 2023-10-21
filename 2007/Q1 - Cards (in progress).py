cards = [int(x) for x in input("Enter cards: ").split()]
comb = []
points = 0

def factorial(n):
  return 1 if n == 0 else n == 1 and 1 or n * factorial(n - 1)

def nChoose2(n):
  if n != 0 and n >= 2:
    return int(factorial(n)/(2*factorial(n-2)))
  return 0

def combinations(n, size, lb):
  if n != 0:
    for i in range(lb, len(cards)):
      buffer[abs(n - size)] = cards[i]

      if n == 1:
        comb.append(buffer.copy())
      combinations(n - 1, size, i + 1)

for i in range(1, 11):
  points += nChoose2(cards.count(i))

for i in range(2, 6):
  comb.clear()
  buffer = [0] * i
  combinations(i, i, 0)
  for c in comb:
    if sum(c) == 15:
      points += 1
    
print(points)
