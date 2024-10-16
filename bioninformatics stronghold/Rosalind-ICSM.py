# %%
def pair_id_with_seq(filepath):
    f=open(filepath)
    g=f.readlines()
    id_list=[]
    seq_list=[]
    seq=''
    for i in g:
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
    f.close()
    return named_seq

# %%
filepath=r"C:\Users\Scott\OneDrive\Desktop\rosalind_lcsm.txt"

seq_list=list(pair_id_with_seq(filepath).values())

# %%
longest_string=''
test_seq=min(seq_list,key=len)
for i in range(len(test_seq)+1):
    for j in range(len(test_seq[i:])+1):
        if len(test_seq[i:j+1]) > len(longest_string) and all(test_seq[i:j+1] in seq for seq in seq_list):
            longest_string=test_seq[i:j+1]

print (longest_string)


