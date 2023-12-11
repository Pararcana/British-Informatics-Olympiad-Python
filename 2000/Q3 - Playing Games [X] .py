die1 = [sorted([int(x) for x in input("Dice 1: ").split()]), sorted([int(x) for x in input("Dice 2: ").split()])]
dicePerms = sorted([i + j for i in die1[0] for j in die1[1]])
diceCount = [dicePerms.count(v) for v in range(2, 17)]
setPerms = set(dicePerms)
sides = len(die1[0])
small = min(dicePerms)
big = max(dicePerms)

def check(arr): # 13s for 1,000,000
  testPerms = sorted([i + j for i in arr[0] for j in arr[1]])
  if dicePerms == testPerms and arr[0] not in [die1[0], die1[1]]:
    final1 = [str(x) for x in arr[0].copy()]
    final2 = [str(x) for x in arr[1].copy()]
    print("\nDice 1: " + " ".join(final1))
    print("Dice 2: " + " ".join(final2)) 
    exit()

def softCheck(arr): # 17s for 1,000,000; ~750,00 in 1s
  testPerms = []
  testPerms = [i + j for i in arr[0] for j in arr[1]]
  testCount = [testPerms.count(v) for v in range(2, 17)]
  return all([testCount[i] <= diceCount[i] for i in range(15)])

def prune(arr):
  arr[0].append(0)
  prune = []
  for i in range(arr[0][-1], 11):
    arr[0][-1] = i
    if softCheck(arr):
      prune.append(i)
  return prune

def pairs(arr, target=None):
  if target:
    for i in range(1, 11):
      for j in range(i, 11):
        if i+j == target:
          yield (i, j)
  else:
    x = prune(arr)
    arr[0].pop(-1)
    arr.reverse()

    y = prune(arr)
    arr[0].pop(-1)
    arr.reverse()
    
    for i in range(arr[0][-1], 11):
      if i in x:
        for j in range(arr[1][-1], 11):
          if j in y and small <= i + j <= big:
            yield (i, j)


if sides == 1:
  for v in pairs(None, target=small):
    check([[v[0]], [v[1]]])
elif sides == 2:
  for v in pairs(None, target=small):
    for x in pairs([[v[0]], [v[1]]]):
      check([[v[0], x[0]], [v[1], x[1]]])
elif sides == 3:
  for v in pairs(None, target=small):
    for x in pairs([[v[0]], [v[1]]]):
      for y in pairs([[v[0], x[0]], [v[1], x[1]]]):
        check([[v[0], x[0], y[0]], [v[1], x[1], y[1]]])
elif sides == 4:
  for v in pairs(None, target=small):
    for x in pairs([[v[0]], [v[1]]]):
      for y in pairs([[v[0], x[0]], [v[1], x[1]]]):
        for z in pairs([[v[0], x[0], y[0]], [v[1], x[1], y[1]]]):
          check([[v[0], x[0], y[0], z[0]], [v[1], x[1], y[1], z[1]]])
elif sides == 5:
  for v in pairs(None, target=small):
    for x in pairs([[v[0]], [v[1]]]):
      for y in pairs([[v[0], x[0]], [v[1], x[1]]]):
        for z in pairs([[v[0], x[0], y[0]], [v[1], x[1], y[1]]]):
          for i in pairs([[v[0], x[0], y[0], z[0]], [v[1], x[1], y[1], z[1]]]):
            check([[v[0], x[0], y[0], z[0], i[0]], [v[1], x[1], y[1], z[1], i[1]]])
elif sides == 6:
  for v in pairs(None, target=small):
    for x in pairs([[v[0]], [v[1]]]):
      for y in pairs([[v[0], x[0]], [v[1], x[1]]]):
        for z in pairs([[v[0], x[0], y[0]], [v[1], x[1], y[1]]]):
          for i in pairs([[v[0], x[0], y[0], z[0]], [v[1], x[1], y[1], z[1]]]):
            for j in pairs([[v[0], x[0], y[0], z[0], i[0]], [v[1], x[1], y[1], z[1], i[1]]]):
              check([[v[0], x[0], y[0], z[0], i[0], j[0]], [v[1], x[1], y[1], z[1], i[1], j[1]]])
elif sides == 7:
  for v in pairs(None, target=small):
    for x in pairs([[v[0]], [v[1]]]):
      for y in pairs([[v[0], x[0]], [v[1], x[1]]]):
        for z in pairs([[v[0], x[0], y[0]], [v[1], x[1], y[1]]]):
          for i in pairs([[v[0], x[0], y[0], z[0]], [v[1], x[1], y[1], z[1]]]):
            for j in pairs([[v[0], x[0], y[0], z[0], i[0]], [v[1], x[1], y[1], z[1], i[1]]]):
              for n in pairs([[v[0], x[0], y[0], z[0], i[0], j[0]], [v[1], x[1], y[1], z[1], i[1], j[1]]]):
                check([[v[0], x[0], y[0], z[0], i[0], j[0], n[0]], [v[1], x[1], y[1], z[1], i[1], j[1], n[1]]])
elif sides == 8:
  for v in pairs(None, target=small):
    for x in pairs([[v[0]], [v[1]]]):
      for y in pairs([[v[0], x[0]], [v[1], x[1]]]):
        for z in pairs([[v[0], x[0], y[0]], [v[1], x[1], y[1]]]):
          for i in pairs([[v[0], x[0], y[0], z[0]], [v[1], x[1], y[1], z[1]]]):
            for j in pairs([[v[0], x[0], y[0], z[0], i[0]], [v[1], x[1], y[1], z[1], i[1]]]):
              for n in pairs([[v[0], x[0], y[0], z[0], i[0], j[0]], [v[1], x[1], y[1], z[1], i[1], j[1]]]):
                for m in pairs([[v[0], x[0], y[0], z[0], i[0], j[0], n[0]], [v[1], x[1], y[1], z[1], i[1], j[1], n[1]]]):
                  check([[v[0], x[0], y[0], z[0], i[0], j[0], n[0], m[0]], [v[1], x[1], y[1], z[1], i[1], j[1], n[1], m[1]]])
print("Impossible")
