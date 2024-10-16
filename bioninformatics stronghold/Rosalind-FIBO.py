# %%
def fib_seq(num):
    start=[0,1,1]
    if num==0:
        print (0)
    elif num==1:
        print (1)
    else:
        for i in range(3,num+1):
            fib_num=start[i-1]+start[i-2]
            start.append(fib_num)
        print (fib_num)


# %%
fib_seq(22)


