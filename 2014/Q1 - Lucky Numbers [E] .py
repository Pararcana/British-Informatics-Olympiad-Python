lucky = [i for i in range(1, 10005, 2)]
n = 3

for _ in range(168):
  luckyNew = []
  for i, v in enumerate(lucky):
    if (i+1) % n != 0:
      luckyNew.append(v)
  lucky = luckyNew.copy()
  n = lucky[lucky.index(n) + 1]

num = int(input("Enter a number: "))

highest = max([v for v in lucky if v < num])
lowest = min([v for v in lucky if v > num])

print(highest, lowest)
"""
Difficulty: E
Again, the only challenge is generating the list of lucky numbers.
Finding the closest higher and lower number than the target is easy.
"""
