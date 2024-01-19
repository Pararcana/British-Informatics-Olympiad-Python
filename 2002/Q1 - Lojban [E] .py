denary = []
lojbanDict = {
  "no": "0", "pa": "1",
  "re": "2", "ci": "3",
  "vo": "4", "mu": "5", 
  "xa": "6", "ze": "7",
  "bi": "8", "so": "9"
}

lojban = input("Write a number in lojiban: ")

for i in range(0, len(lojban), 2):
  denary.append(lojbanDict[lojban[i:i+2]])

print("".join(denary))
"""
Difficulty: E
This one was pretty simple, the use of a dictionary and extraction of each
individual part of the string is all that is needed to solve this problem.

For fun, and a little bit of a challenge, I decided to make a one liner to
solve this problem. (It's not a serious solution due to undreadability...)

print("".join((lambda x: [{"no": "0", "pa": "1", "re": "2", "ci": "3", "vo": "4", "mu": "5", "xa": "6", "ze": "7", "bi": "8", "so": "9"}[x[i:i+2]] for i in range(0, len(x), 2)])(input("Write a number in lojiban: "))))
"""
