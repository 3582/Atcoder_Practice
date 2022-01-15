# どの桁も 0 でない 3 桁の整数 abc が与えられるので、abc+bca+cab を求めてください。
a=input()
print(int(a[0]+a[1]+a[2])+int(a[1]+a[2]+a[0])+int(a[2]+a[0]+a[1]))