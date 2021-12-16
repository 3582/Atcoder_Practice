A=[]
for _ in range(4):
    A.append(int(input()))
ans = 0

for a in range(A[0] + 1):
    for b in range(A[1] + 1):
        for c in range(A[2] + 1):
            if(a*500 + b*100 + c*50) == A[3]:
                ans +=1
print(ans)