import sys
sys.setrecursionlimit(10**6)
 
s = input()
l = len(s)
ans = 0
def dfs(i, f):
    print(f)  
    if i == l:
        x = list(map(int, f.split("+")))
        print(x)
        return sum(x)
    return dfs(i+1, f+s[i]) + dfs(i+1, f+"+"+s[i])

print(dfs(1, s[0]))
