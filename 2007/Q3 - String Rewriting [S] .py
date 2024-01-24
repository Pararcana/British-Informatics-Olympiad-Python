string = input("Enter a string: ").upper()
repeat, limit = [int(x) for x in input("Enter s and p: ").split()]
strings = {"A": "A", "B": "B", "C": 2 ** repeat}
logs_2 = [2**i for i in range(32)]
counter = [0, 0, 0, 0, 0]
total = 0

def rewrite(string): 
  return "".join([{"A": "B", "B": "AB"}[v] for v in string])

def excess(num):
  flips = 0
  while num > 1:
    num -= max(filter(lambda x: x <= num, logs_2))
    flips += 1
  
  num = bool(num)
  if flips % 2 != 0:
    num = not num  
  return num

if "A" in string or "B" in string:
  for _ in range(repeat):
    strings["A"] = rewrite(strings["A"])

  if "B" in string:
    strings["B"] = rewrite(strings["A"])

def AB(letter):
  global total
  string = strings[letter][:limit - total]
  counter[0] += string.count("A")
  counter[1] += string.count("B")
  total += len(string)

def CD(letter):
  global total
  string = min(strings["C"], limit - total)
  total += string
  counter[2] += string // 2
  counter[3] += string // 2
  if string % 2 != 0:
    counter[2 if excess(string // 2) == letter else 3] += 1

for v in string:
  if v in "AB":
    AB(v)
  elif v in "CD":
    CD(v == "D")
  else:
    e = min(strings["C"], limit - total)
    counter[4] += e
    total += e

print(*counter)

"""
Difficulty: S
This question was fairly easy to understand and implement, the only problem is time.
You cannot simulate the entire string up to 29 steps. (At least in python.)
Instead, you can do each letter of the string individually. We also need to know 
what happens to the numbers of each character if we cut the string at a certain point.

A and B [A -> B; B -> AB]:
We can approximate the length of the string (l) after n steps with the formula: l = n log n.
The maximum length of the string (Letter: B; Steps: 29) is 1346269, and can be simulated
within the allowed two seconds, so I did that. We can simply cut the string off when it gets
too long and count the number of As and Bs in the remainder.

C and D [C -> CD; D -> DC]:
The length of this string can be found with the formula: l = 2^n. The number of Cs and Ds
can be modelled by l = (2^n)/2. The difficulty here comes from cutting the string off.
If you cut the string off and have an even remainder, there will be an equal number of Cs
and Ds. Else, there will be an extra C or D. Also, the string takes too long to simulate.
(If you use a faster language, you can probably simulate it.)

What I noticed when simulating it for smaller numbers was (for C):
Notice a pattern?

CD

CD DC

CD DC DC CD

CD DC DC CD DC CD CD DC

CD DC DC CD DC CD CD DC DC CD CD DC CD DC DC CD

(Note that D follows the same pattern, but the position of CDs and DCs are swapped.)
Now, let me replace all the CDs with 0, and all the DCs with 1.

0

0 1

0 1 1 0

0 1 1 0 1 0 0 1

0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0

The pattern is that you can determine the next step by looking at the current step,
inverting all the bits, and appending it to the current step.

Next, I just did the inverse of that to find whether the bit at a certain position is 0 or 1.
This allows us to save time by not generating the entire list. (See "excess" function.)

E [E -> EE]:
The length of this string is also l = 2^n. But, it is all composed of Es. This means that
we can take the minimum of the number of characters left and 2^n.
"""
