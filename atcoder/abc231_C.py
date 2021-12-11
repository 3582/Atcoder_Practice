N, Q = map(int, input().split())
A = list(map(int, input().split()))
X  = []
Q_r = list(range(Q))
N_r = list(range(N))
for _ in Q_r:
    X.append(int(input()))

for x_num in Q_r:
    ans = []
    for num in N_r:
        if(A[num] >= X[x_num]):
            ans.append(A[num])
    
    print(len(ans))