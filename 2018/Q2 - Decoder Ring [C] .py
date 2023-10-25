alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ring, answer = [], []
counter = 0

number, word = input("Input a number and word. ").split()
number, word = int(number), word.upper()

for _ in range(26):
  counter += (number % len(alphabet)) - 1
  if counter >= len(alphabet):
    counter %= len(alphabet)
  elif counter == -1:
    counter = len(alphabet) - 1
  ring.append(alphabet.pop(counter))
print("".join(ring[0:6]))

for char in word:
  answer.append(ring[ord(char)-65])
  ring.append(ring.pop(0))
print("".join(answer))
"""
Difficulty: C
This one wasn't too hard, you can split the problem into two parts:
generating the ring, which is the encryption key, and using a
circular shift after each individual letter is encrypted.
"""
