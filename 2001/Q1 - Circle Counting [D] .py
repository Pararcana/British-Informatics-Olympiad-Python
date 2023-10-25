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
"""
Difficulty: D
To solve this, you can use a counter to point to the person that
is going to get eliminated and increment it based on the number of
words in the rhyme. To prevent an overflow error, you should loop 
the counter back around when it goes above the length of the list.
"""
