fib1, fib2, index = input("Enter two letters and a number: ").split()
fib1, fib2 = ord(fib1) - 64, ord(fib2) - 64

fib = [fib1, fib2]

for _ in range(int(index) - 2):
  newEntry = fib[-1] + fib[-2]
  fib.append(newEntry > 26 and newEntry - 26 or newEntry)

print(chr(fib[int(index) - 1] + 64))
"""
Difficulty: D
Not too bad, you just need to create a list using fibonacci rules with the 2 starting
letters' indexes in the alphabet.
"""
