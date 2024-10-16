# %%
with open(r"C:\Users\Scott\OneDrive\Desktop\rosalind_iev.txt") as f:
    f=f.read().split(' ')
    num_list=[int(i) for i in f]
    tot_pop=sum(num_list)
    probability=(num_list[0]+num_list[1]+num_list[2]+num_list[3]*0.75+num_list[4]*0.5)*2
    print(probability)

# %%



