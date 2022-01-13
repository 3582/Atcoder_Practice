a=input()

def func(i,ans,sum):
    if i == 3:
        if sum == 7:
            print(ans + "=7")
            exit()
    else:
        func(i+1, ans + "+" + a[i+1],sum + int(a[i+1]))
        func(i+1, ans + "-" + a[i+1],sum - int(a[i+1]))

func(0,a[0],int(a[0]))