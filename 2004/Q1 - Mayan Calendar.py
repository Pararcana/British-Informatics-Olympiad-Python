weightings = [1, 20, 20*18, 20**2*18, 20**3*18]
month = [31, "leap", 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start = [13, 20, 7, 16, 3]
date = [1, 1, 2000]
mayan = [int(x) for x in input("Enter a mayan date: ").split()]
mayan = [a - b for a, b in zip(mayan, start)]
mayan.reverse()

days = 0
for i, v in enumerate(mayan):
  days += v * weightings[i]

while days >= (date[2] % 4 == 0 and 366 or 365):
  days -= date[2] % 4 == 0 and 366 or 365
  date[2] += 1

for length in month:
  if type(length) == type(0):
    if length < days:
      days -= length
      date[1] += 1
  else:
    if (date[2] % 4 == 0 and 29 or 28) < days:
      days -= date[2] % 4 == 0 and 29 or 28
      date[1] += 1

date[0] += days

date = [str(x) for x in date]
print(" ".join(date))
