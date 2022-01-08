# 関数 f を f(x)=(x*x)+(2*x)+3 と定義します
# 整数 t が入力されるので、 f(f(f(t)+t)+f(f(t))) を求めてください。
# f(f(f(t)+t)+f(f(t)))
def cal(num):
    return (num*num)+(2*num)+3
    
t = int(input())
print(cal(cal(cal(t)+t)+cal(cal(t))))
