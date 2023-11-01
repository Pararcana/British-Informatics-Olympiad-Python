password = input("Input a password: ").upper()
repeat = False

for i in range(len(password)):
  for j in range(1, int(len(password)/2) + 1):
    if i+2*j <= len(password) and password[i:i+j] == password[i+j:i+2*j]:
      repeat = True

print(repeat and "Rejected" or "Accepted")
"""
Difficulty: E
A nested for loop will help you to cover all possible combinations of
ajacent characters, and you simply need to check if any ajacent
characters are equal to complete the question.
"""
