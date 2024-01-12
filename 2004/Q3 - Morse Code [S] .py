fromMorse = [
  ".-", "-...", "-.-.", "-..", ".", "..-.", 
  "--.", "....", "..", ".---", "-.-", ".-..", 
  "--", "-.", "---",  ".--.", "--.-", ".-.", 
  "...", "-", "..-", "...-", ".--", "-..-", 
  "-.--", "--.."
]
toMorse =  {chr(i+65): v for i, v in enumerate(fromMorse)}

morse = input("Enter a word: ").upper()
length = len(morse)
morse = "".join(toMorse[v] for v in morse)
perms = []

def findMatch(target):
  target = "".join(target)
  remainder = morse[len(target):]
  return [v for v in fromMorse if v == remainder[:len(v)]]

def findString(target, n=0):
  if n == length and "".join(target) == morse:
    perms.append(target)
    
  elif n < length:
    for v in findMatch(target):
      target = target[:n]
      findString(target+[v], n+1)

findString([])
print(len(perms))

"""
Difficulty: S
With this question, I decided to use recursion.
At this point, I had just sat, and solved the
2024 BIO's Q3, so I used a method similar to that
one, where you slowly build up each possibility,
and prune braches to optimise for time.

This is a very well-known question, with quite a
few variations. When looking online, you can find
a lot of different methods on how to solve it. 
You can find other guides that will walk you this.
"""
