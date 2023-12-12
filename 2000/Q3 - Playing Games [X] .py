sides = int(input("Enter the number of sides: "))
dieA = sorted([int(x) for x in input("Dice 1: ").split()])
dieB = sorted([int(x) for x in input("Dice 2: ").split()])

die1 = [dieA, dieB]
dicePerms = sorted([i + j for i in die1[0] for j in die1[1]])
diceCount = [dicePerms.count(v) for v in range(2, 17)]
small, big = min(dicePerms), max(dicePerms)

def check(arr):
  testPerms = sorted([i + j for i in arr[0] for j in arr[1]])
  if dicePerms == testPerms and arr[0] not in [die1[0], die1[1]]:
    final1 = [str(x) for x in arr[0].copy()]
    final2 = [str(x) for x in arr[1].copy()]
    print("\nDice 1: " + " ".join(final1))
    print("Dice 2: " + " ".join(final2)) 
    exit()

def softCheck(arr):
  testPerms = []
  testPerms = [i + j for i in arr[0] for j in arr[1]]
  testCount = [testPerms.count(v) for v in range(2, 17)]
  return all([testCount[i] <= diceCount[i] for i in range(15)])

def prune(arr):
  arr[0].append(0)
  prune = []
  for i in range(arr[0][-1], big):
    arr[0][-1] = i
    if softCheck(arr):
      prune.append(i)
  return prune

def pairs(arr, target=None):
  if target:
    for i in range(1, big):
      for j in range(i, big):
        if i+j == target:
          yield [[i], [j]]
  else:
    x = prune(arr)
    arr[0].pop(-1)
    arr.reverse()

    y = prune(arr)
    arr[0].pop(-1)
    arr.reverse()

    for i in range(arr[0][-1], big):
      if i in x:
        for j in range(arr[1][-1], big):
          if j in y and small <= i + j <= big:
            yield (i, j)

def step(testDie, n=1):
  if n == sides:
    check(testDie)
    
  else:
    for v in pairs(testDie):
      for i in range(2):
        while len(testDie[i]) > n:
          testDie[i].pop(-1)
        testDie[i].append(v[i])
        
      step(testDie, n + 1)

for v in pairs(None, target=small):
  step(v)
print("Impossible")
"""
Difficulty: X
There are probably multiple methods to do this, but the one
I went with involved a pruned bruteforce, as to not make each
test obnoxiously long. 

The pruning algorithm involves appending a number to each test 
die and checking if the test sample space is a subset of the 
inputted dice's sample space (via the 'softCheck' function). If 
it isn't, we can prune that branch, as it will never be a solution, 
no matter the continuation.

To generate each die, I used my 'pairs' function, which would
generate some pruned numbers to bruteforce. Finally, I used a 
recursive algorithm to create the dice that would be verified 
by the checking algorithm.
"""
