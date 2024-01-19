# In progress!
cards = list(range(1, 9))
shuffles = []

def riffle(cards, mode):
  split = cards[:4], cards[4:]
  even = "i % 2 == 0" if mode else "i % 2 != 0"
  return [split[1 if eval(even) else 0][i//2] for i in range(8)]

def brackets():
  counter = 1
  subsection = []
  for v in string:
    if v == "(":
      counter += 1
    elif v == ")":
      counter -= 1

    if counter != 0:
      subsection.append(v)
  return subsection

chars = {
  "b": "cards[1:] + [cards[0]]",
  "i": "riffle(cards, True)",
  "o": "riffle(cards, False)"
}

#string = input("Enter a series of shuffles: ").lower()
string = list("3i")
print(string)

i = 0
while i != len(string):
  v = string[i]
  if v in "bio":
    shuffles.append(v)
  else:
    if string[i + 1] != "(":
      shuffles += [string[i+1]] * int(string[i])
      i += 1
    else:
      pass
      
  i += 1

print(*shuffles)
for v in shuffles:
  cards = eval(chars[v])


print(*cards)
