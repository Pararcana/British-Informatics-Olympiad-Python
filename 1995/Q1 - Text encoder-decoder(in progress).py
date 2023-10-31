#Decoder
alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ,. ')
key = list("I WANDERLOYSCUBFGHJKMPQTVXZ,.")
new = list("OOANJQ,GPXXLTLUXPPQCCUUG.BEYY OY  RKDEZGGWGGVNSKKDY..ANGPPQRSSK.STTHX FFG.SSCAAJAESSMMYSDDEEO,URSOOYYG.BH..BMMBFINQWGTT,.DSZ YQCS")
final = []

counter = key.index(new[0])
for i in range(len(new) - 1):
  final.append(alpha[counter - 1])
  counter = 29 - (key.index(new[i]) - key.index(new[i+1]))
  if counter > len(alpha) - 1:
    counter -= len(alpha)

print("".join(final))
########################################
#Encoder
alpha = list('/ABCDEFGHIJKLMNOPQRSTUVWXYZ,. ')
key = list("I WANDERLOYSCUBFGHJKMPQTVXZ,.")
new = list("I WANDERED LONELY AS A CLOUD THAT FLOATS ON HIGH OER DALE AND HILL WHEN ALL AT ONCE I SAW A CROWD, A FLOCK OF WANDRING DAFFODILS.")
final = []

counter = 0
for char in new:
  counter += alpha.index(char)
  if counter > len(key) - 1:
    counter -= 29
  final.append(key[counter])

print("".join(final))
