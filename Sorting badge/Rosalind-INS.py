# %%
f=open(r"C:\Users\Scott\OneDrive\Desktop\rosalind_ins.txt")
g=f.read().split()
f.close()
g=[int(i) for i in g]
del(g[0])

# %%
def iteration_sort(arr):
    n=len(arr)
    count=0
    if n<=1:
        return
    
    for i in range(1,n):
        key=arr[i]
        j=i-1

        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
            count+=1
        arr[j+1]=key

    print (count)


# %%
iteration_sort(g)


