target = int(input("Enter a number: "))

primes = [2]
for i in range(3,  int(target**(1/2)) + 1, 2):
  if all([i % j != 0 for j in range(2, int(i**(1/2)) + 1)]):
    primes.append(i)
if all([target % i != 0 for i in range(2, target)]):
  primes.append(target)

ans = {1}
while target != 1:
  for v in primes:
    if target % v == 0:
      ans.add(v)
      target /= v

counter = 1
for v in ans:
  counter *= v
print(counter)
