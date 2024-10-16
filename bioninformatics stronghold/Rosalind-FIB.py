# %%
months=5
offspring=3
prev_pop=0
current_pop=1
for i in range(1,months):
    change_pop=current_pop+prev_pop*offspring
    prev_pop=current_pop
    current_pop=change_pop
    print (i,current_pop)

# %%



