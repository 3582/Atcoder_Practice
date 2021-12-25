L, R = map(int, input().split())
S = input()

list = []

list.append(S[:L-1])
list.append(S[L-1:R][::-1])
list.append(S[R:])

print(''.join(list))