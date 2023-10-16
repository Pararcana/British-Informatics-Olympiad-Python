friends = int(input("Number of friends: "))
ring = [i for i in range(friends)]

words = int(input("Words in rhyme: "))
counter = 0

for _ in range(friends - 1):
  counter += (words-1) % len(ring)
  if counter > len(ring) - 1:
    counter -= len(ring)
  ring.pop(counter)

print(ring[0] + 1)
