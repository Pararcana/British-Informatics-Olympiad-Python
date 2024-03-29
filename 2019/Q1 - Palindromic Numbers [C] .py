def makePalindrome(n):
  mid = len(n) % 2 != 0 and n[(len(n) - 1)//2] or ""
  palindrome = n[0:len(n)//2] + mid + n[(len(n)//2)-1::-1]
  return int(palindrome)

target = str(int(input("Enter a number: ")) + 1)
num = makePalindrome(target)

if len(target) == 1:
  print(target)
else:
  while num < int(target):
    sNum = str(num)
    num = makePalindrome(str(int(sNum[0:(len(sNum)+1)//2])+1) + sNum[(len(sNum)+1)//2:])
  print(num)
"""
Difficulty: C
The range of inputs is to great to bruteforce a solution, so you need to be smart and
only check the palindromes, which you might find hard to do. I'd recommend that you
split the palindromes that you check into odd and even.
"""
