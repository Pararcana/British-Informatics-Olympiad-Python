encrypt = input("Enter a string to decrypt: ").upper()
strBits, oriString = [], []

for char in encrypt:
  strBits.append(ord(char))

for i in range(len(strBits)):
  try:
    bit = strBits[-(i+1)]-strBits[-(i+2)]
  except IndexError:
    bit = strBits[0]-64
  if bit <= 0:
    bit += 26
  oriString.append(chr(bit+64))

oriString.reverse()
decrypt = "".join(oriString)

print(decrypt)
