num = int(input("Enter a number: "))
ans = []

for i in range(2, 10):
  if sorted(str(num)) == sorted(str(num*i)):
    ans.append(str(i))

if ans:
  print(" ".join(ans))
else:
  print("NO")
