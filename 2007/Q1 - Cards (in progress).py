cards = [int(x) for x in input("Enter cards: ").split()]
points = 0

def factorial(n):
  v = 1
  for i in range(2, n + 1):
    v *= i
  return v

def nChoice2(n):
  return int(factorial(n)/(2*factorial(n-2)))

def combinations(n):
  pass

for i in range(1, 11):
  points += nChoice2(cards.count(i))


print(points)
