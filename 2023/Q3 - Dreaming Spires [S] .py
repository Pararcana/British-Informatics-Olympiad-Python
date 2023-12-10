start = input("Enter the initial state: ").split()
end = input("Enter the end state: ").split()
start = [list(v) if v[0] != "0" else [] for v in start]
end = [list(v) if v[0] != "0" else [] for v in end]

def format(arr, end):
  arr = [v.copy() for v in arr]
  end = [v.copy() for v in end]
  for i in range(4):
    while len(arr[i]) != len(end[i]):
      if len(arr[i]) > len(end[i]):
        end[i].append("0")
      else:
        arr[i].append("0")
  return arr, end

def findBases(arr, goal):
  base = []
  for i in range(4):
    for j in range(len(arr[i])):
      if arr[i][j] != goal[i][j] and goal[i][j] != "0":
        base.append(goal[i][j])
        break
  return base

def fitness(arr):
  global end
  total = 0
  testArr, goal = format(arr, end)
  base = findBases(testArr, goal)

  for i in range(4):
    order = True
    for j in range(len(testArr[i])):
      if testArr[i][j] == goal[i][j] and order:
        total += 250
      else:
        order = False
        if any([v in testArr[i] for v in base]):
          total -= 100
        else:
          total += 5 * (4 - j)
        if testArr[i][0] == "0":
          total += 5
  return total
      
def step():
  global start
  perms = {}
  for i in range(4):
    for j in range(4):
      if j != i:
        try:
          test = [v.copy() for v in start]
          test[j].append(test[i].pop(-1))
          perms.update({fitness(test): test})
        except IndexError:
          pass
  start = perms[max(perms.keys())]

counter = 0
while start != end:
  step()
  counter += 1
print(counter)
"""
Difficulty: S
The maximum number of permutations in each step is 12. This
means that you can search each individual move in a position,
which I evaluate with my fitness function and pick the best 
one. Repeat until you reach the desired position.

For my fitness function, I add points if the balls are in their
correct positions, deduct points if other balls are stacked on
top of a "important" ball (one that needs to be at the bottom of
a stack before the rest can be added on top) and incentivise 
stacking low.
"""
