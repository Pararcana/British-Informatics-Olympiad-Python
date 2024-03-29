cards = [int(x) for x in input("Enter cards: ").split()]
points = 0

def combinations(n, lb=0):
  if n != 0:
    for i in range(lb, len(cards)):
      buffer[n - 1] = cards[i]

      if n == 1:
        comb.append(buffer.copy())
      combinations(n - 1, i + 1)

for i in range(2, 6):
  comb, buffer = [], [0] * i
  combinations(i)
  for c in comb:
    if sum(c) == 15 or (i == 2 and c[0] == c[1]):
      points += 1
    
print(points)
"""
Difficulty: B
The only hard part was making the combinations function,
which uses recursion, but you can avoid that by simply
using the premade one in the itertools library.
"""
