# %%
with open(r"C:\Users\Scott\OneDrive\Desktop\rosalind_inv.txt") as f:
    n=int(f.readline().strip())
    inversion_list=[int(i) for i in f.readline().strip().split()]

# %%
def merge_count_split_inv(arr):
    """
    This function performs the merge step of merge sort,
    and counts the split inversions, where one element is in the left half
    and the other is in the right half of the array.
    """
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = merge_count_split_inv(arr[:mid])
    right, right_inv = merge_count_split_inv(arr[mid:])
    
    merged = []
    i = j = 0
    split_inv = 0

    # Merge step with inversion counting
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            split_inv += len(left) - i  # Count inversions
            j += 1
    
    # Add remaining elements from left and right
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, left_inv + right_inv + split_inv

def count_inversions(arr):
    """
    This function returns the number of inversions in the array.
    """
    _, inv_count = merge_count_split_inv(arr)
    return inv_count

# %%
count_inversions(inversion_list)

# %%



