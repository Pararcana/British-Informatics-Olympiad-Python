digitWords = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN"]

def lowest(arr, lb):
  arr = [v for v in arr if v > lb]
  try:
    return min(arr)
  except ValueError:
    return None

word = list(input("Enter a word: ").upper())

for digit in digitWords:
  if set(digit).issubset(word):
    significantChars = [v for v in word if v in digit]

    order, digitOccurences = [], []
    for num in digit:
      for index, char in enumerate(significantChars):
        if char == num:
          digitOccurences.append(index)
      order.append(digitOccurences.copy())
      digitOccurences.clear()

    lb = -1
    for i in range(len(digit)):
      low = lowest(order[i].copy(), lb)
      if low is None or low <= lb:
        print("NO")
        exit()
      lb = low

    print(digitWords.index(digit) + 1)
    exit()

print("NO")
