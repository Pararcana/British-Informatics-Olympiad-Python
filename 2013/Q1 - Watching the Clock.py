aIncre, bIncre = (int(x) + 60 for x in input("Enter two numbers: ").split())
a, b = aIncre, bIncre

def minutesToHours(min):
  return [(min // 60) % 24, min % 60]

while minutesToHours(a) != minutesToHours(b):
  a += aIncre
  b += bIncre

hours, minutes = minutesToHours(a)
print("{:02d}".format(hours)+":"+"{:02d}".format(minutes))
