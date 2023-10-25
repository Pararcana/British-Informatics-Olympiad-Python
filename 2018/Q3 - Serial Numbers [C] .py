def match(list, serial):
  return not any(item[0] == serial for item in list)

serials, exhaustedSerials, answer = [], [], []
digits = int(input("How many digits are in your serial number? "))
serials.append([input("What is the serial number? "), 0])

while len(serials) != 0:
  for i in range(digits - 1):
    currentSerial = serials[0][0]
    significantDigits = currentSerial[i:i+2]
    if i != 0 and i+2 < digits:
      surroundingDigits = [currentSerial[i-1], currentSerial[i+2]]
    else:
      surroundingDigits = i == 0 and [currentSerial[2]] or [currentSerial[-3]]

    for j in range(len(surroundingDigits)):
      middleCheck = [significantDigits[0], surroundingDigits[j], significantDigits[1]]
      if not(surroundingDigits[j] == max(middleCheck) or surroundingDigits[j] == min(middleCheck)):
        newSerial = list(currentSerial).copy()
        newSerial[i:i+2] = significantDigits[::-1]
        newSerial = "".join(newSerial)
        if match(exhaustedSerials, newSerial) and match(serials, newSerial):
          serials.append([newSerial, serials[0][1] + 1])
  exhaustedSerials.append(serials.pop(0))

for item in exhaustedSerials:
  answer.append(item[1])
print(max(answer))
"""
Difficulty: C
This wasn't too hard, as you simply needed to check the surrounding
digits of the two that you are trying to swap, and see if at least one
of the surrounding digits is between them numerically. Then, repeat
this process for every new serial you generate. It is a good idea to use
a linked list to hold the serial, and how many steps it took to generate.
"""
