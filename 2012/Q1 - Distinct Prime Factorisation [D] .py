target = int(input("Enter a number: "))

primes = [2]
for i in range(3,  int(target**(1/2)) + 1, 2):
  if all([i % j != 0 for j in range(2, int(i**(1/2)) + 1)]):
    primes.append(i)
if all([target % i != 0 for i in range(2, target)]):
  primes.append(target)

counter = 1
for v in primes:
  if target % v == 0:
    counter *= v
print(counter)
"""
Difficulty: D
Once again, you can split this problem into two parts: prime
generation, and multiplying them together if they are a factor
of the target. Numpy's prod() function may be useful for this.
"""
