# In progress!
def check(sample1, sample2):
  testPerms = sorted([i + j for i in sample1 for j in sample2])
  if dicePerms == testPerms and sample1 != dice1 and sample1 != dice2:
    final1 = [str(x) for x in sample1.copy()]
    final2 = [str(x) for x in sample2.copy()]
    print("\nDice 1: " + " ".join(final1))
    print("Dice 2: " + " ".join(final2)) 
    exit()

def middle(list1, list2, list3, list4, middle1, middle2, choice):
  x = int(list1)
  y = int(list2)
  z = x + y 
  for i in range(int(z/2)):
    d = x + i 
    f = y - i
    k = int((d+f)/2) 
    if sides % 2 == 0: 
      middle1.append([d,f])
    else:
      middle1.append([d,k,f])
  a = int(list3)
  b = int(list4)
  c = a + b
  for j in range(int(c/2)):
    g = a + j
    h = b - j
    l = int((g+h)/2)
    if sides % 2 == 0:
      if choice == 0:
        middle2.append([g,h])
      else:
        middle2.append([g,h+1])
    else:
      middle2.append([g,l,h])


def reset2(list1, list2):
  list1.clear()
  list2.clear()


def sort2(list1, list2):
  list1.sort()
  list2.sort()


# sides = int(input("Number of sides: "))
# dice1 = input("\nDice 1: ")
# dice2 = input("Dice 2: ") 
sides = 8
# dice1 = "1 2 3 4 5 6 7 8"
# dice2 = "1 2 3 4 5 6 7 8"
dice1 = "7 5 3 1 1 3 5 7"
dice2 = "1 1 8 8 6 6 4 4"
dice1 = sorted([int(x) for x in dice1.split(" ")])
dice2 = sorted([int(x) for x in dice2.split(" ")])
dicePerms = sorted([i + j for i in dice1 for j in dice2])

smallSolutions, bigSolutions, check2, possibilities, test1, test2, test3, test4, test5, test6 = [], [], [], [], [], [], [], [], [], []
middleList1, middleList2, middleList3, middleList4, middleList5, middleList6 = [], [], [], [], [], []
finish = False 

small = int(dice1[0]) + int(dice2[0]) 
big = int(dice1[sides-1]) + int(dice2[sides-1]) 

for i in range(int(small/2)):
  x = i + 1
  y = small - (i + 1)
  smallSolutions.append([x,y])
for i in range(int(big/2)):
  x = i + 1
  y = big - (i + 1)
  bigSolutions.append([x,y]) 

for x in range(len(smallSolutions)):
  for y in range(len(bigSolutions)):
      possibilities.append([smallSolutions[x][0],bigSolutions[y][0]])
      possibilities.append([smallSolutions[x][1],bigSolutions[y][1]]) 
for i in range(len(possibilities)):
  possibilities[i].sort() 

for iter in range(2):
  if sides == 1:
    for i in range(int(small/2)):
      x = i + 1
      y = small - (i + 1)
      check(sides, [x], [y])
  else:
    for e in range(int(len(possibilities)/2)):
      if sides == 2: 
        check([possibilities[e*2][0], possibilities[e*2][1]], [possibilities[(e*2)+1][0], possibilities[(e*2)+1][1]])
      elif sides == 3:
        middle1 = int((possibilities[e*2][0] + possibilities[e*2][1])/2)
        middle2 = int((possibilities[(e*2)+1][0] + possibilities[(e*2)+1][1])/2)
        test1 = [possibilities[e*2][0], middle1, possibilities[e*2][1]]
        test2 = [possibilities[(e*2)+1][0], middle2, possibilities[(e*2)+1][1]]
        sort2(test1, test2)
        check(test1, test2) 
      else:
        middle(possibilities[e*2][0], possibilities[e*2][1], possibilities[(e*2)+1][0], possibilities[(e*2)+1][1], middleList1, middleList2, 0)
        for zi in range(len(middleList1)):
          for yj in range(len(middleList2)):
            if sides != 5:
              test1.append([possibilities[e*2][0], middleList1[zi][0], middleList1[zi][1], possibilities[e*2][1]])
              test2.append([possibilities[(e*2)+1][0], middleList2[yj][0], middleList2[yj][1], possibilities[(e*2)+1][1]])
            else: 
              test1.append([int(possibilities[e*2][0]), int(middleList1[zi][0]), int(middleList1[zi][1]), int(middleList1[zi][2]), int(possibilities[e*2][1])])
              test2.append([int(possibilities[(e*2)+1][0]), int(middleList2[yj][0]), int(middleList2[yj][1]), int(middleList2[yj][2]), int(possibilities[(e*2)+1][1])])
            sort2(test1[0], test2[0])
            if sides == 4 or sides == 5:
              check(test1[0], test2[0])
            else:
              middle(test1[0][1], test1[0][2], test2[0][1], test2[0][2], middleList3, middleList4, iter)
              for xi in range(len(middleList3)):
                for wj in range(len(middleList4)):
                  for k in range(4):
                    test3.append(test1[0][k])
                    test4.append(test2[0][k])
                  test3.append(middleList3[xi][0])
                  test3.append(middleList3[xi][1])
                  test4.append(middleList4[wj][0])
                  test4.append(middleList4[wj][1]) 
                  if sides == 7:
                    test3.append(middleList3[xi][2])
                    test4.append(middleList4[wj][2]) 
                  sort2(test3, test4)
                  if sides == 6 or sides == 7:
                    check(test3, test4)
                  else:
                    middle(test3[2], test3[3], test4[2], test4[3], middleList5, middleList6, 0) 
                    for vi in range(len(middleList5)):
                      for uj in range(len(middleList6)):
                        for l in range(6):
                          test5.append(test3[l])
                          test6.append(test4[l]) 
                        test5.append(middleList5[vi][0])
                        test5.append(middleList5[vi][1])
                        test6.append(middleList6[uj][0])
                        test6.append(middleList6[uj][1]) 
                        sort2(test5, test6)
                        check(test5, test6)
                        reset2(test5, test6)
                    reset2(middleList5, middleList6)
                  reset2(test3, test4)
              reset2(middleList3, middleList4)
            reset2(test1, test2)
        reset2(middleList1, middleList2) 

print("\nImpossible\n")
