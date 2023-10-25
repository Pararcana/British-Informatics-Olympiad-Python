fib, ans = [1, 2], []
total = 0

while fib[-1] < 1000000:
  fib.append(fib[-1] + fib[-2])
fib.reverse()

num = int(input("Number: "))

for i in fib:
  if i + total <= num:
    total += i
    ans.append(str(i))

print(" ".join(ans))
"""
Difficulty: E
The first step is simply to generate the fibonacci sequence up to 1,000,000.
Next, work from the back and save any number in the sequence that fits into
the input in a list. Finally, output the list.
"""
