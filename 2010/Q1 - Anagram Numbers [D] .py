num = int(input("Enter a number: "))
ans = []

for i in range(2, 10):
  if sorted(str(num)) == sorted(str(num*i)):
    ans.append(str(i))

if ans:
  print(" ".join(ans))
else:
  print("NO")
"""
Difficulty: D
Really not that difficult, the thing you should remember with anagrams, is that
you can sort them and see if they give the same result.
"""
