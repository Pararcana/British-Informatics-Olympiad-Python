def genKey(word, reverse=False):
  alpha = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")
  word = list(dict.fromkeys(word).keys())
  word += filter(lambda x: x not in word, alpha)
  return word[::-1] if reverse else word

def playfair(text, mode):
  ans = []
  for bigram in text:
    r1, c1 = divmod(grid1.index(bigram[0]), 5)
    r2, c2 = divmod(grid2.index(bigram[1]), 5)
    if r1 == r2:
      c1 += mode
      c2 += mode
    ans.append(grid1[r2*5 + c1%5])
    ans.append(grid2[r1*5 + c2%5])
  return ans[:-1] if mode == -1 and ans[-1] == "X" else ans

grid1 = genKey(input("Enter keyword 1: ").upper())
grid2 = genKey(input("Enter keyword 2: ").upper(), reverse=True)

for i in range(5):
  print(*grid1[i*5:(i+1)*5], "\t", *grid2[i*5:(i+1)*5])

while (action := input("What do you want to do? ").upper()) != "Q":
  if action == "E":
    text = input("Enter text to be encoded: ").upper()
    text = text if len(text) % 2 == 0 else text + "X"
    text = [text[i:i+2] for i in range(0, len(text), 2)]
    print("".join(playfair(text, 1)))

  if action == "D":
    text = input("Enter text to be decoded: ").upper()
    text = [text[i:i+2] for i in range(0, len(text), 2)]
    print("".join(playfair(text, -1)))

"""
Difficulty: A
This isn't a full playfair cipher, as this question doesn't
include shifting when the columns are the same and inserting
an X when the position of the bigrams are the same.

But all in all, it is a fairly simple implementation question.
All the steps you need to do are provided in the question. For
decryption, the only thing you need to change is that, if the
bigram is in the same row, shift left rather than right.
"""
