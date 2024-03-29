class Ant: 
  def __init__(self, *coords): 
    self.coords = int(coords[0]), int(coords[1]), coords[2]

  def __str__(self):
    return " ".join(str(v) for v in self.coords) if self.coords else "Removed"

  def move(self):
    if self.coords:
      x, y, dir = self.coords
      match dir:
        case "R": x += 1
        case "L": x -= 1
        case "T": y += 1
        case "B": y -= 1

      if not(0 < x < 12 and 0 < y < 12): 
        self.coords = False
      else:
        empty = 1 if grid[-y + 11][x - 1] == "." else -1
        grid[-y + 11][x - 1] = "*" if empty == 1 else "."
        self.coords = x, y, faces[(faces.index(dir) + empty) % 4]

position1 = input("Input ant 1's co-ordinates and direction: ").upper().split(" ")
position2 = input("Input ant 2's co-ordinates and direction: ").upper().split(" ")
ant1, ant2 = Ant(*position1), Ant(*position2)
grid = [["."] * 11 for _ in range(11)]
faces = ["T", "R", "B", "L"]

while (moves := int(input("\nNumber of moves: "))) != -1:
  for _ in range(moves): 
    ant1.move()
    ant2.move()
  for row in grid: 
    print(*row)

  print(ant1)
  print(ant2)

"""
Difficulty: B
This question involves the use of classes, so you can define how both ants move according to
the question. This isn't that hard to do, considering the ants have fairly simple rules. Another
thing to remember is that you need to update the grid each turn. All in all, not too difficult,
assuming you know how to create and use classes.

Another similar question to this is 'Tamworth Two' - 1998 Q2. Try that if you wish.
"""
