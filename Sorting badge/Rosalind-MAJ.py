# %%
with open(r"C:\Users\Scott\OneDrive\Desktop\rosalind_maj.txt") as f:
    k,n=map(int,f.readline().strip().split())
    lol=[list(map(int,line.strip().split())) for line in f]

# %%
def find_majority_element(arr):
    count = {}
    n = len(arr)
    
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    if count[num] > len(arr) // 2:
        print (num,end=' ')
    
    else:
        print (-1,end=' ')
    

def list_iter(list_of_lists):
    for i in list_of_lists:
        find_majority_element(i)

# %%
list_iter(lol)

# %%



