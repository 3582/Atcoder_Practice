N, Q = map(int, input().split())
a = list(map(int, input().split()))
xk = [map(int, input().split()) for _ in range(Q)]
x, k = [list(i) for i in zip(*xk)]

for i in range(Q):
    result = x[i] in a
    if result:
        count = 0
        for j in range(len(a)):
            if a[j] == x[i]:
                count += 1
                ans = j+1
            if count == k[i]:
                print(ans)
                break
        if count != k[i]:
            print(-1)
    else:
        print(-1)