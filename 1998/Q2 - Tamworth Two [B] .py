class Animal: 
  def __init__(self, type, *coords): 
    self.letter = type
    self.coords = int(coords[0]), int(coords[1])
    self.dir = "T"

  def __str__(self):
    x, y = self.coords
    return " ".join([str(x), str(y), self.dir])

  def move(self):
    x, y = self.coords
    grid[-y + 10][x - 1] = "."
    match self.dir:
      case "R": x += 1
      case "L": x -= 1
      case "T": y += 1
      case "B": y -= 1

    if not(0 < x < 11 and 0 < y < 11) or [x, y] in trees: 
      x, y = self.coords
      self.dir = faces[(faces.index(self.dir) + 1) % 4]
      
    self.coords = x, y

def updateGrid():
  if pigs.coords == farmer.coords:
    grid[-pigs.coords[1] + 10][pigs.coords[0] - 1] = "+"
  else:
    x, y = pigs.coords
    grid[-y + 10][x - 1] = pigs.letter
    
    x, y = farmer.coords
    grid[-y + 10][x - 1] = farmer.letter

position1 = input("Input the pig's co-ordinates: ").upper().split(" ")
position2 = input("Input the farmer's co-ordinates: ").upper().split(" ")
pigs, farmer = Animal("P", *position1), Animal("F", *position2)
grid = [["."] * 10 for _ in range(10)]
faces = ["T", "R", "B", "L"]
trees = []
move = 0

updateGrid()
for row in grid: 
  print(*row)

while (action := input("\nAction: ").upper()) != "X":
  action = action.split()
  match action[0]:
    case "M":
      for _ in range(int(action[1])): 
        move += 1
        pigs.move()
        farmer.move()
        
        if pigs.coords == farmer.coords:
          print(f"Meeting at ({pigs.coords[0]}, {pigs.coords[1]}) on move {move}.")
          
      updateGrid()

    case "T":
      for _ in range(int(action[1])):
        pos = [int(x) for x in input("Enter tree position: ").split()]
        trees.append(pos)
        grid[-pos[1] + 10][pos[0] - 1] = "*"

  for row in grid: 
    print(*row)

"""
Difficulty: B
Another implementation question. Much like 'Ants' (2000 Q2"), this one
followed similar principles (Yes, I know that this one came first, but
I did Ants first).

The use of classes for the pigs and farmer is encouraged here, you can
reuse the same class for both of them, considering how the movement is
the same.

You just need a function for movement, collision detection and meeting
detection. That is essentially all this question boils down to.
"""
