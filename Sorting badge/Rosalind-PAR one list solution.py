# %%
with open(r"C:\Users\Scott\OneDrive\Desktop\rosalind_par.txt") as f:
    n=int(f.readline().strip())
    partition_list=[int(i) for i in f.readline().strip().split()]

# %%
def two_way_partition(arr):

    target=arr[0]
    searching=placing=0

    while searching <= len(arr)-2:
        searching+=1
        if arr[searching] <= target:
            arr[placing+1],arr[searching]=arr[searching],arr[placing+1]
            placing+=1
          
    arr[0],arr[placing]=arr[placing],arr[0]
   


