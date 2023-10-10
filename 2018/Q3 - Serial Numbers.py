def match(list, serial):
  return not any(item[0] == serial for item in list)

serials, exhaustedSerials, answer = [], [], []
digits = int(input("How many digits are in your serial number? "))
serials.append([input("What is the serial number? "), 0])

while len(serials) != 0:
  for i in range(digits - 1):
    currentSerial = serials[0][0]
    sigDigits = currentSerial[i:i+2]
    if i != 0 and i+2 < digits:
      surDigits = [currentSerial[i-1], currentSerial[i+2]]
    else:
      surDigits = i == 0 and [currentSerial[2]] or [currentSerial[-3]]
    swappable = False
    for j in range(len(surDigits)):
      middleCheck = [sigDigits[0], surDigits[j], sigDigits[1]]
      if not(surDigits[j] == max(middleCheck) or surDigits[j] == min(middleCheck)):
        swappable = True
    newSerial = list(currentSerial).copy()
    newSerial[i:i+2] = sigDigits[::-1]
    newSerial = "".join(newSerial)
    if swappable and match(exhaustedSerials, newSerial) and match(serials, newSerial): 
      serials.append([newSerial, serials[0][1] + 1])
  exhaustedSerials.append(serials.pop(0))

for item in exhaustedSerials:
  answer.append(item[1])
print(max(answer))
