isbn = list(input("Enter an ISBN with a missing digit: "))
isbn.reverse()
total = 0

for i, v in enumerate(isbn):
  try: total += int(v) * (i + 1)
  except ValueError:
    if v == "X":
      total += 10
    else:
      missingPos = i + 1

for i in range(1, 12):
  if (total + (i * missingPos)) % 11 == 0:
    if 10 <= i <= 11:
      print(i == 10 and "X" or 0)
    else:
      print(i)
