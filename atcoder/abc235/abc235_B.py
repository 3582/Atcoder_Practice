N = int(input())
x = list(map(int, input().split()))
ans = x[0]
for i in range(N):
    if i != N-1:
        if x[i] < x[i+1]:
            ans = x[i+1]
        else:
            print(ans)
            exit()
print(ans)