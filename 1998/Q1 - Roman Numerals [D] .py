num = "{:04d}".format(int(input("Please input a number: ")))
ans = []
roman = [
["M", ""],
["C", "D", "M", ""],
["X", "L", "C", ""],
["I", "V", "X", ""]
]
cast = [[-1], [0], [0,0], [0,0,0], [0,1], [1], [1,0], [1,0,0], [1,0,0,0], [0,2]]
for i, n in enumerate(num):
    for j in range(len(cast[int(n)])):
        ans.append(roman[i][cast[int(n)][j]])
    
print("".join(ans))
"""
Difficulty: D
This question is only as hard as you make it, and there are multiple ways to approach
this question, the easiest of which would simply to convert units, tens, hundreds and 
thousands seperately into roman numeral form, then concatenate the result. Leetcode also 
has this question (#12) with every single test case if you want to check your solution.
"""
