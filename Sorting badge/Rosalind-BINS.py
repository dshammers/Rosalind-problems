# %%
f=open(r"C:\Users\Scott\OneDrive\Desktop\rosalind_bins.txt")
g=f.read().split()
g=list(map(int,g))
f.close()

sorted_list=g[2:g[0]+2]
test_list=g[g[0]+2:]

def binary_search(arr,n):

    low,high=0,len(arr)-1

    while low <= high:

        mid=(high+low)//2

        if n == arr[mid]:
            print (mid+1)
            break
            
        if n < arr[mid]:
            high=mid-1
        
        if n > arr[mid]:
            low=mid+1
        
        if low > high:
            print (-1)

        
def test_numbers(sorted_list,test_list):
    for i in test_list:
        binary_search(sorted_list,i)

# %%
test_numbers(sorted_list,test_list)

# %%



