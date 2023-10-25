colours = list(input("Input an array of squares: ").upper())
coloursTemp = []

for _ in range(len(colours) - 1):
  for i in range(len(colours) - 1):
    if colours[i] == colours[i + 1]:
      coloursTemp.append(colours[i])
    else:
      coloursTemp.append(next(iter({"R", "G", "B"}.difference([colours[i], colours[i + 1]]))))
  colours = coloursTemp.copy()
  coloursTemp.clear()
  
print(colours[0])
"""
Difficulty: E
This was a very simple and fun puzzle to implement with only a couple of steps. You need to compare 
two values to find the next one, and repeat this process until you are left with only one value.
"""
