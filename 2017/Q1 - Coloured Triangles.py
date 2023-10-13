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
