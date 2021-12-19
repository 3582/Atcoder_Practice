N = int(input())
A = list(map(int, input().split()))
b = True
ans = 0
while(b):
    for num in range(len(A)):
        if(A[num]%2 == 0):
            A[num] = A[num]/2
        else:
            b = False
            break
    if(b):    
        ans +=1
print(ans)