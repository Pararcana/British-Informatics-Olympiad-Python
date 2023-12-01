digitWords = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN"]
word = input("Enter a word: ").upper()

for digit in digitWords:
  wordFilter = [v for v in word if v in digit]
  order = []
  counter = 0
  
  for v in digit:
    try:
      first = wordFilter.index(v)
      order.append(first + counter)
      wordFilter = [v for i, v in enumerate(wordFilter) if i > first]
      counter += first + 1
    except ValueError:
      break  
      
  if sorted(order) == order and len(order) == len(digit):
    print(digitWords.index(digit) + 1)
    exit()
print("NO")
"""
Difficulty: C
The key to this question, is that you need to check the order in which each letter of each
digit appears in the word. The index() and remove() methods only affect the first instance
of the item specified in the list, so it might be a good idea to use them in your code.
Remember that after each letter you use in the word, all letters to the left of it become
unavailable, as the order would not be contiguous.
"""
