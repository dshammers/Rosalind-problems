# %%
def pair_id_with_seq(f):
    id_list=[]
    seq_list=[]
    seq=''
    for i in f:
        line=i.strip('\n')
        if line.startswith('>'):
            if seq:
                seq_list.append(seq)
                seq=''
            id_list.append(line)
        else:
            seq+=line
    seq_list.append(seq)
    named_seq=dict(zip(id_list,seq_list))
    return named_seq

# %%
def highest_gc_percent(dict):
    largest_fraction_id=''
    gc_fraction=0
    for key,value in dict.items():
        current_fraction=(value.count('G') + value.count('C'))/len(value)
        if current_fraction > gc_fraction:
            largest_fraction_id=key
            gc_fraction=current_fraction
    return largest_fraction_id,gc_fraction*100

# %%
with open(r"C:\Users\Scott\OneDrive\Desktop\rosalind_gc.txt",'r') as f:
    f=f.readlines()
    labeled_seq=pair_id_with_seq(f)
    fraction_id,gc_percentage=highest_gc_percent(labeled_seq)
    print (fraction_id)
    print (gc_percentage)

# %%



