a = int(input())
A = []
for _ in range(a):
    A.append(str(input()))

x = list(set(A))
ansnum = []

for num in range(len(x)):
    ansnum.append(A.count(x[num]))

print(x[ansnum.index(max(ansnum))])