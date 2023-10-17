f, i = float(input("Decimal: ")), 0

while True:
  i += 1
  if (i/f).is_integer():
    print(str(i) + "/" + str(int(i/f)))
    break
