# %%
with open(r"C:\Users\Scott\OneDrive\Desktop\rosalind_par3.txt") as f:
    n=int(f.readline().strip())
    partition_list=[int(i) for i in f.readline().strip().split()]

# %%
def three_way_partition(arr):
    pivot=arr[0]
    lt, i, gt = 0, 0, len(arr) - 1
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1
    
    return arr

# %%
three_way_partition(partition_list)
print (*partition_list)


