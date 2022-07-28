#work in progress, only works for dice with up to 3 sides
sides = int(input("Number of sides: "))
if sides < 1 or sides > 8:
  print("\nError: Number of sides on dice is either below one or above eight.\n")
  exit()


dice1 = input("Dice 1: ")
info1 = dice1.split(" ")
if len(info1) != sides:
  print("\nError: Number of sides on dice 1 and sides specified do not match.\n")
  exit()
for i in range(len(info1)):
  if int(info1[i]) < 1 or int(info1[i]) > 8:
    print("\nError: Number on one of the sides on dice 1 is either below one or above eight\n")
    exit()


dice2 = input("Dice 2: ")
info2 = dice2.split(" ")
if len(info2) != sides:
  print("\nError: Number of sides on dice 2 and sides specified do not match.\n")
  exit()
for i in range(len(info1)):
  if int(info2[i]) < 1 or int(info2[i]) > 8:
    print("\nError: Number on one of the sides on dice 2 is either below one or above eight.\n")
    exit()


finish = False
counter = 0
smallSolutions = []
bigSolutions = []
solutions = []
removeSmall = []
removeBig = []
remove = []
check1 = []
check2 = []
numberStorage = []
possibilities = []
middleList = []


for i in range(sides*2):
  if i < sides:
    counter += int(info1[i])
    info1[i] = int(info1[i])
  else:
    counter += int(info2[i-sides])
    info2[i-sides] = int(info2[i-sides])
    

info1 = sorted(info1)
info2 = sorted(info2)


if sides == 1:
  small = int(info1[0]) + int(info2[0])
  for i in range(int(small/2)):
    x = i + 1
    y = small - (i + 1)
    solutions.append([x,y])
  for i in range(len(solutions)):
    if solutions[i] == [info1[0],info2[0]]:
      remove.append(i)
  solutions.pop(remove[0])
  if len(solutions) != 0:
    print("\nDice 1: " + str(solutions[0][0]))
    print("Dice 2: " + str(solutions[0][1]))
  else:
    print("\nImpossible")

    
elif sides == 2:
  small = int(info1[0]) + int(info2[0])
  big = int(info1[sides-1]) + int(info2[sides-1])
  for i in range(int(small/2)):
    x = i + 1
    y = small - (i + 1)
    smallSolutions.append([x,y])
  for i in range(int(big/2)):
    x = i + 1
    y = big - (i + 1)
    bigSolutions.append([x,y])
  for i in range(len(smallSolutions)):
    if smallSolutions[i][0] == info1[0] and smallSolutions[i][1] == info2[0]:
      remove.append(i)
  if len(remove) == 0:
    print("\nImpossible")
  smallSolutions.pop(remove[0])
  remove.clear()  
  for i in range(len(bigSolutions)):
    if bigSolutions[i][0] == info1[1] and bigSolutions[i][1] == info2[1]:
      remove.append(i)
  bigSolutions.pop(remove[0])
  remove.clear()
  for i in range(2):
    for j in range(2):
      check1.append(info1[i]+info2[j])
      check1.sort()
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
      for i in range(2): # sides
        for j in range(2):
          check2.append(smallSolutions[x][i]+bigSolutions[y][j])
          check2.sort()
      if check1 == check2:
        numberStorage.append(x)
        numberStorage.append(i)
        numberStorage.append(y)
        numberStorage.append(j)
        finish = True
      else:
        check2.clear()
  if finish:
    diceStorage = numberStorage.copy()
    diceStorage[1] -= 1
    diceStorage[3] -= 1
    print("\nDice 1: " + str(smallSolutions[diceStorage[0]][(diceStorage[1])]) , str(bigSolutions[(diceStorage[2])][(diceStorage[3])]))
    print("Dice 2: " + str(smallSolutions[numberStorage[0]][numberStorage[1]]) , str(bigSolutions[numberStorage[2]][numberStorage[3]]))
  else:
    print("\nImpossible")

    
elif sides == 3:
  small = int(info1[0]) + int(info2[0])
  big = int(info1[sides-1]) + int(info2[sides-1])
  for i in range(int(small/2)):
    x = i + 1
    y = small - (i + 1)
    smallSolutions.append([x,y])
  for i in range(int(big/2)):
    x = i + 1
    y = big - (i + 1)
    bigSolutions.append([x,y])
  for i in range(3):
    for j in range(3):
      check1.append(info1[i]+info2[j])
      check1.sort()
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][0],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][1],bigSolutions[y][1]])
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][1],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][0],bigSolutions[y][1]])
  for i in range(len(possibilities)):
    possibilities[i].sort()
  for i in range(len(possibilities)):
    evenOdd = possibilities[i][0] + possibilities[i][1]
    if (evenOdd % 2) != 0:
      remove.append(i)
  remove.reverse()
  for i in range(len(remove)):
    possibilities.pop(remove[i])  
  for i in range(len(possibilities)):
    middle = possibilities[i][0] + possibilities[i][1]
    middle = int(middle/2)
    possibilities[i].insert(1, middle)
  for x in range(int(len(possibilities)/2)):
    for i in range(3):
      for j in range(3):
        check2.append(possibilities[x*2][i] + possibilities[(x*2)+1][j])
        check2.sort()
    if check1 == check2:
      if possibilities[x*2] == info1 and possibilities[(x*2)+1] == info2: 
        pass
      elif possibilities[x*2] != info2 and possibilities[(x*2)+1] != info1:
        finish = True
        numberStorage.append(x)
      else:
        check2.clear()
    else:
      check2.clear()
  if finish:
    x = int(numberStorage[0])
    print("\nDice 1: " + str(possibilities[x*2][0]), str(possibilities[x*2][1]), str(possibilities[x*2][2]))
    print("Dice 2: " + str(possibilities[(x*2)+1][0]), str(possibilities[(x*2)+1][1]), str(possibilities[(x*2)+1][2]))
  else:
    print("\nImpossible")

    
elif sides == 4:
  small = int(info1[0]) + int(info2[0])
  big = int(info1[sides-1]) + int(info2[sides-1])
  for i in range(int(small/2)):
    x = i + 1
    y = small - (i + 1)
    smallSolutions.append([x,y])
  for i in range(int(big/2)):
    x = i + 1
    y = big - (i + 1)
    bigSolutions.append([x,y])
  for i in range(4):
    for j in range(4):
      check1.append(info1[i]+info2[j])
      check1.sort()
  print(check1)
  print(smallSolutions)
  print(bigSolutions)
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][0],bigSolutions[y][0]])
        possibilities.append([smallSolutions[x][1],bigSolutions[y][1]])
  for x in range(len(smallSolutions)):
    for y in range(len(bigSolutions)):
        possibilities.append([smallSolutions[x][0],bigSolutions[y][1]])
        possibilities.append([smallSolutions[x][1],bigSolutions[y][0]])
  for i in range(len(possibilities)):
    possibilities[i].sort()
  for i in range(len(possibilities)):
    evenOdd = possibilities[i][0] + possibilities[i][1]
    if (evenOdd % 2) != 0:
      remove.append(i)
  remove.reverse()
  for i in range(len(remove)):
    possibilities.pop(remove[i])  
  for i in range(len(possibilities)):
    middle = possibilities[i][0] + possibilities[i][1]
    middle = int(middle/2)
    possibilities[i].insert(1, middle)
  for x in range(int(len(possibilities)/2)):
    for i in range(3):
      for j in range(3):
        check2.append(possibilities[x*2][i] + possibilities[(x*2)+1][j])
        check2.sort()
    if check1 == check2:
      if possibilities[x*2] == info1 and possibilities[(x*2)+1] == info2: 
        pass
      elif possibilities[x*2] != info2 and possibilities[(x*2)+1] != info1:
        finish = True
        numberStorage.append(x)
      else:
        check2.clear()
    else:
      check2.clear()
  if finish:
    x = int(numberStorage[0])
    print("\nDice 1: " + str(possibilities[x*2][0]), str(possibilities[x*2][1]), str(possibilities[x*2][2]))
    print("Dice 2: " + str(possibilities[(x*2)+1][0]), str(possibilities[(x*2)+1][1]), str(possibilities[(x*2)+1][2]))
  else:
    print("\nImpossible")
    
# i did say it was spaghetti didnt I?
