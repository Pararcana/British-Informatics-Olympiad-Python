aIncre, bIncre = (int(x) for x in input("Enter two numbers: ").split())
a = aIncre + 60
b = bIncre + 60

def minutesToHours(min):
  return [(min // 60) % 24, min % 60]

while minutesToHours(a) != minutesToHours(b):
  a += 60 + aIncre
  b += 60 + bIncre

hours, minutes = minutesToHours(a)
print("{:02d}".format(hours)+":"+"{:02d}".format(minutes))
