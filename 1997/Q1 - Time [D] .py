words = (
  "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
  "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", 
  "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three", 
  "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", "half"
)

hours = int(input("Hours: "))
minutes = int(input("Minutes: "))

half = "to" if minutes > 30 else "past"
if minutes > 30:
  hours += hours == 12 and -11 or 1
  minutes = 60 - minutes
special = minutes not in (15, 30, 45) and "minutes " or ""

if minutes == 0:
  print(f"{words[hours]} o'clock")
else:
  print(f"{words[minutes]} {special}{half} {words[hours]}")
"""
Difficulty: D
All in all, not that hard, and the only tedious part was writing out each number as a word, which
you could've skipped using the num2words library. You also had to recognise special cases, such as 15
and 30 being referred to as 'quarter' and 'half' respectively. There was also the added difficulty
of recognising whether it was closer to, or past the hour and implementing that in the program.
"""
