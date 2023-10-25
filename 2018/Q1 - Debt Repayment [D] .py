def ceil(num):
  return num.is_integer() and num or int(num) + 1
  
debt, total = 10000, 0

interest, repayment = input("Please input interest and repayment percentages: ").split()
interest, repayment = float(interest)/100, float(repayment)/100

while debt != 0:
  debt = ceil((debt * interest) + debt)
  total += debt <= 5000 and debt or max(ceil(debt * repayment), 5000)
  debt -= debt <= 5000 and debt or max(ceil(debt * repayment), 5000)

print(total/100)
"""
Difficulty: D
This would have been lower in difficulty, were it not for the floating point errors that
you have to avoid. Other than that, this problem consists of applying a simple formula,
which is fairly simple.
"""
