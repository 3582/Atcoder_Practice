# 高橋君は、毎日 s_num 時 0 分に部屋の電気をつけ、毎日 T 時 0 分に消します。
s_num,t_num,x_num = map(int, input().split())
light = "No"
t_num += 0.5
if s_num < x_num:
    if x_num < t_num:
        light = "Yes"


print(light)