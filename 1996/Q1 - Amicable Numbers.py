num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
factors1, factors2 = [], []

def factoriser(arr, num):
  for i in range(num):
    if num%(i+1) == 0 and i+1 != num:
      arr.append(i+1)

factoriser(factors1, num1)
factoriser(factors2, num2)

if (sum(factors1) == num2) and (sum(factors2) == num1) and num1 != num2:
  print("Amicable numbers.")
else:
  print("Not amicable.")

"""
Difficulty: E
This one was fairly easy to do, the only real challenge here is making a function to find the factors of each input, the rest is elementary.
"""
