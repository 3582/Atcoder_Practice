N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

# 「 x 座標の差の２乗＋ y 座標の差の２乗のルート」
def cal(x1,y1,x2,y2):
    return ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))**0.5
ans = []
for i in range(N-1):
    num = l[i]
    loop = 0
    loop +=1+i
    while(loop < N):
        ans.append(cal(l[i][0],l[i][1],l[loop][0],l[loop][1]))
        loop +=1
        
print(max(ans))