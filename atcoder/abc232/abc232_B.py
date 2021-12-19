# S = str(input())
# T = str(input())
# alist = "abcdefghijklmnopqrstuvwxyz"
# strans = "Yes"
# ansnum1 = []

# for i in range(len(S)):
#     wbool = True
#     num1 = alist.index(S[i])
#     num2 = 0
#     while wbool:
#         if num1 == 25:
#             num1 = 0
#         if alist[num1] == T[i]:
#             ansnum1.append(num2)
#             wbool = False
#         num1 +=1
#         num2 +=1

# if len(set(ansnum1)) !=1:
#     strans = "No"
# print(strans)

s = input()
t = input()
ans = "Yes"
code = ((ord(s[0]) )- (ord(t[0])))% 26
for i in range(1,len(s)):
    print(ord(s[i]))
    print(ord(t[i])%26)
    if (ord(s[i]) - ord(t[i]))%26  != code:
        ans = "No"

print(ans) 