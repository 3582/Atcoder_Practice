N = list(map(int, input().split()))

a = -1
b = -1
c = -1
for x in range(N[0]+1):
    for y in range(N[0]+1-x):
        if x*10000 + y*5000 + (N[0]-x-y)*1000 == N[1]:
            c = (N[0]-x-y)
            a = x
            b = y

print(a,b,c)