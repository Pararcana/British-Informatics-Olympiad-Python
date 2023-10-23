def ordered(str1, str2):
  arr1 = [ord(v) for v in str1]
  arr2 = [ord(v) for v in str2]
  return min(arr1) > max(arr2)

def isPat(str):
  if len(str) == 1:
    return True
  else:
    return any(ordered(str[:i], str[i:]) for i in range(1, len(str)))
  
str1, str2 = input("Enter two strings: ").split()
str3 = str1 + str2
print(isPat(str1) and "YES" or "NO")
print(isPat(str2) and "YES" or "NO")
print(isPat(str3) and "YES" or "NO")
