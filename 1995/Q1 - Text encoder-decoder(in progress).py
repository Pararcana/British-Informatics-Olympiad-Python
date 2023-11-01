alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ,. ")  

def decoder(key, ciphertext):
  ciphertext = [v for v in ciphertext if v in alpha]
  final = []

  counter = key.index(ciphertext[0])
  for i in range(len(ciphertext) - 1):
    final.append(alpha[counter - 1])
    counter = 29 - (key.index(ciphertext[i]) - key.index(ciphertext[i+1]))
    if counter >= 29:
      counter -= 29
  final.append(alpha[counter - 1])

  return "".join(final)

def encoder(key, plaintext):
  plaintext = [v for v in plaintext if v in alpha]
  final = []
  
  counter = 0
  for char in plaintext:
    counter += alpha.index(char) + 1
    if counter >= 29:
      counter -= 29
    final.append(key[counter])

  return "".join(final)

def presentMenu():
  print("""
  1. Enter an encoding "key" string.
  2. Encode a section of text using the current key.
  3. Decode a section of text using the current key.
  4. Exit.
  """)
  return int(input("Select your choice: "))

def findKey(string):
  alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ,. ")
  final = []
  string = [v for v in string if v in alpha]
  for v in string:
    if v in alpha:
      final.append(v)
      alpha.remove(v)
  return final + alpha

choice = presentMenu()
while choice != 4:
  if choice == 1:
    key = findKey(input("Enter a code key: ").upper())
  elif choice == 2:
    print(encoder(key, input("Enter message: ").upper()))
  elif choice == 3:
    print(decoder(key, input("Enter message: ").upper()))
  choice = presentMenu()
exit()
