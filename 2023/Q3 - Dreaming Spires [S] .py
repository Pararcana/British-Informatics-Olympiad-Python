start = input("Enter the initial state: ").split()
end = input("Enter the end state: ").split()

start = [list(v) if v[0] != "0" else [] for v in start]
end = [list(v) if v[0] != "0" else [] for v in end]

def fitness(arr):
  global end
  total = 0
  testArr = [v.copy() for v in arr]
  goal = [v.copy() for v in end]
  for i in range(4):
    while len(testArr[i]) != len(goal[i]):
      if len(testArr[i]) > len(goal[i]):
        goal[i].append("0")
      else:
        testArr[i].append("0")

  base = []
  for i in range(4):
    order = True
    for j in range(len(testArr[i])):
      if testArr[i][j] != goal[i][j] and goal[i][j] != "0":
        base.append(goal[i][j])
        break

  for i in range(4): # Fitness function
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
