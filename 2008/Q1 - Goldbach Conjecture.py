primes = []
target = int(input("Enter a number: "))
counter = 0

for i in range(2, target + 1):
  prime = True
  for j in range(2, int(i**(1/2)) + 1):
    if i % j == 0:
      prime = False
      break
  if prime:
    primes.append(i)

for i in range(len(primes)):
  for j in range(i, len(primes)):
    if primes[i] + primes[j] == target:
      counter += 1
print(counter)
    
