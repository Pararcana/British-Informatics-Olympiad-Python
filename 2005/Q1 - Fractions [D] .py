i, f = 0, float(input("Decimal: "))

while True:
  i += 1
  fraction = i/f
  if fraction.is_integer():
    print(str(i) + "/" + str(int(i/f)))
    break
  # Python's maths sucks; for example, 401/0.2005 gives 1999.999999... rather than 2000, which gives a false negative.
  elif str(fraction).split(".")[1][0:12] == "9" * 12: # Checks if the decimal is reoccuring.
    print(str(i) + "/" + str(int(i/f) + 1))
    break
"""
Difficulty: D
The only hard part with doing this without the use of libraries is finding the method. With the use of libraries, you
could import decimal and used the is_integer_ratio function built into python to find the fraction. However, this runs
into a floating point division error in certain cases. The decimal library seems to fix this. Alternatively, you could
simply use the fractions library to convert it.
"""
