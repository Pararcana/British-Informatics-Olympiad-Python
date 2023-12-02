left = [1, 0]
right = [0, 1]

promenade = input("Enter a string of left or right: ")

for dir in promenade:
  if dir == "L":
    left = [left[0]+right[0], left[1]+right[1]]
  else:
    right = [left[0]+right[0], left[1]+right[1]]

print(left[0] + right[0], "/", left[1] + right[1])
"""
Difficulty: E
The only challenge is understanding the question. Implementing
the solution is formulaic and simple.
"""
