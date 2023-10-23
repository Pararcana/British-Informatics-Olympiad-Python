def ordered(str1, str2):
  arr1 = [ord(v) for v in str1]
  arr2 = [ord(v) for v in str2]
  return min(arr1) > max(arr2)

def isPat(str):
  if len(str) == 1:
    return True
  else:
    for i in range(1, len(str)):
      if ordered(str[:i], str[i:]) and isPat(str[:i][::-1]) and isPat(str[i:][::-1]):
        return True
    return False
  
strs = input("Enter two strings: ").split()
strs.append(strs[0] + strs[1])

for v in strs:
  print(isPat(v) and "YES" or "NO")
