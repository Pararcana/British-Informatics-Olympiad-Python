alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ,. ")  

def formatText(string):
  for i in range(len(string)//50, 0, -1):
    string.insert(i*50, "\ \n")
  string.append("#")
  print("".join(string))

def decoder(key, ciphertext):
  ciphertext = [v for v in ciphertext if v in alpha]
  print("Message is:")
  formatText(list(ciphertext))
  final = []

  counter = key.index(ciphertext[0])
  for i in range(len(ciphertext) - 1):
    final.append(alpha[counter - 1])
    counter = 29 - (key.index(ciphertext[i]) - key.index(ciphertext[i+1]))
    if counter >= 29:
      counter -= 29
  final.append(alpha[counter - 1])
  print("Decoded message is:")
  return "".join(final)

def encoder(key, plaintext):
  plaintext = [v for v in plaintext if v in alpha]
  print("Message is:")
  formatText(list(plaintext))
  final = []
  
  counter = 0
  for char in plaintext:
    counter += alpha.index(char) + 1
    if counter >= 29:
      counter -= 29
    final.append(key[counter])
  print("Encoded message is:")
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
    formatText(list(encoder(key, input("Enter message: ").upper())))
  elif choice == 3:
    formatText(list(decoder(key, input("Enter message: ").upper())))
  choice = presentMenu()
exit()
"""
Difficulty: B
The only real challenges here are the encoding and decoding functions.
For the encoding function, you are given the steps to do it, so it is
fairly easy to implement. On the other hand, for decoding, you have to
figure out the decoding method yourself. What you have to realise, is
that it is the difference between the key position of ajacent characters
that allows you to derive the original text. As for the other tasks,
such as formatting the text in the way they asked, capitallising each 
letter and removing unknown ones are a lot easier to implement. 

For the record, I believe that their markscheme is wrong, and that
'ooanjP,gpxxltluxppqcc' decoded gives 'I WANCFRED LONELY AS ' rather than
'I WANAHRED LONELY AS ', and it is instead 'ooanjK,gpxxltluxppqcc'
that gives 'I WANAHRED LONELY AS ' (Note that P -> K). If it turns 
out I am incorrect, open an issue under the issues tab, show me
the proof and I will correct it as soon as possible.
"""
