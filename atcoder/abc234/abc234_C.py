N = int(input())

# ans_int = ""+(format(N, 'b'))
# print(ans_int.replace("1","2"))

ans = int(bin(N)[2:])
print(ans*2)