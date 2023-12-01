target = int(input("Enter a number: "))
counter = 0

primes = [2]
for i in range(3, target, 2):
  if all([i % j != 0 for j in range(2, i)]):
    primes.append(i)

for i in range(len(primes)):
  for j in range(i, len(primes)):
    if primes[i] + primes[j] == target:
      counter += 1
print(counter)
"""
Difficulty: D
You can split this problem into two parts: generating the primes;
and using a nested for loop to count the number of different ways
the target number can be achieved. All in all, not too hard.
"""
