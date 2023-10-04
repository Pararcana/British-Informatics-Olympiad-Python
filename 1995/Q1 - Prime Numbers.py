def factorial(num):
  total = 1
  for i in range(1, num + 1):
    total *= i
  return total
  
arr = []
limit = int(input("Maximum number to test? "))
for i in range(1, limit):
  arr.append(int((factorial(i)%(i+1))/i)*(i-1)+2)

print(set(arr))
print(str(len(set(arr))) + " prime numbers.")
