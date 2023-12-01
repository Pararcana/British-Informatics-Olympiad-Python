rivers = [[1], [3], [9]]

for river in rivers:
  while river[-1] < 25000:
    sumDigits = sum([int(x) for x in str(river[-1])])
    river.append(river[-1] + sumDigits)

k = int(input("Enter a river: "))
nums = [1, 3, 9]

while True:
  for i, river in enumerate(rivers):
    if k in river:
      print(f"Meets river {nums[i]} at {k}.")
      exit()
  k += sum([int(x) for x in str(k)])
"""
Difficulty: E
This problem can be split into two parts: generating the rivers
and finding where they meet, which involves searching each river
and incrementing 'k' if necessary.
"""
