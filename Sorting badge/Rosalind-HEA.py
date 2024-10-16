# %% [markdown]
# # source: https://github.com/zonghui0228/Rosalind-Solutions/blob/master/code/rosalind_hea.py

# %%
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1 # left = 2*i + 1 
    r = 2 * i + 2 # right = 2*i + 2 

    # If left child is larger than root 
    if l < n and arr[l] > arr[largest]:
        largest = l 
  
    # If right child is larger than largest so far 
    if r < n and arr[r] > arr[largest]:
        largest = r
  
    # If largest is not root 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def buildHeap(arr, n): 
    startIdx = n // 2 - 1
    for i in range(startIdx, -1, -1): 
        heapify(arr, n, i)


# %%
f=open(r).read().split()
f=[int(i) for i in f]
n=f[0]
bulk=f[1:]

# %%
buildHeap(bulk,n)

# %%
print (*bulk)

# %%



