# %%
with open(r"C:\Users\Scott\OneDrive\Desktop\rosalind_fibd.txt") as f:
    months,lifespan=[int(i) for i in f.read().split(' ')]
    num_list = []
    num_list.append(0)
    num_list.append(1)
    for i in range(1, months):
        if i < lifespan:
            num_list.append(num_list[i] + num_list[i-1])
        if i == lifespan:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-lifespan+1])
        if i > lifespan:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-lifespan])
    print (num_list[months])

# %%



