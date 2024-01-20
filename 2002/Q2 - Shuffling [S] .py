cards = list(range(1, 9))

def riffle(cards, mode):
  split = cards[:4], cards[4:]
  even = "i % 2 == 0" if mode else "i % 2 != 0"
  return [split[1 if eval(even) else 0][i//2] for i in range(8)]

def parse(string):
  try:
    close = string.index(")")
    open = [i for i, x in enumerate(string) if x == "(" and i < close]

    start = string[:open[-1] - 1]
    end = string[close + 1:]
    repeat = int(string[open[-1] - 1])

    return start + string[open[-1] + 1:close] * repeat + end

  except ValueError:
    return False

chars = {
  "b": lambda cards: cards[1:] + [cards[0]],
  "i": lambda cards: riffle(cards, True),
  "o": lambda cards: riffle(cards, False)
}

string = input("Enter a series of shuffles: ").lower()
shuffles = []

i = 0
while i != len(string):
  if string[i].isdigit() and string[i + 1] != "(":
    shuffles += [string[i+1]] * int(string[i])
    i += 2
  else:
    shuffles.append(string[i])
    i += 1

while (brackets := parse(shuffles)) is not False:
  shuffles = brackets.copy()

#print(*shuffles)
for v in shuffles:
  cards = chars[v](cards)
print(*cards)

"""
Difficulty: S
The difficulty in this question comes from parsing the
series of shuffles they give you. Making algorithms to
perform each individual shuffle is trivial.

For my parser algorithm, I did it in two steps. The
first step was to repeat individual letters (if present).
The second step was to repeat the series of letters in
a bracket. I did this from the inside out. This means
that inner brackets will be done first.

The result is a series of letters that can be executed
sequentially. I did this using lamda, but eval can be
used as well. You can uncomment line 45 to see the string
after parsing.
"""
