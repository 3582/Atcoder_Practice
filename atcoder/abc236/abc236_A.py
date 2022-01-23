# 英小文字からなる文字列 S が与えられます。
# S の先頭から a 文字目と b 文字目を入れ替えて得られる文字列を出力してください。
S = input()
a, b = map(int, input().split())

print(S[:a-1]+S[b-1]+S[a:b-1]+S[a-1]+S[b:])