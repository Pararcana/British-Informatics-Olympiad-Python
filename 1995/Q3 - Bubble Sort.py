num = None
arr = []

while num != -999:
  num = int(input("Enter a number: "))
  arr.append(num)
  
arr.remove(-999)
arr.sort()
print(arr)
