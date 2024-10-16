# %%
from Bio import SeqIO
k=r"C:\Users\Scott\OneDrive\Desktop\rosalind_grph.txt"
for record in SeqIO.parse(k,'fasta'):
    [print(record.id,i.id) for i in SeqIO.parse(k,'fasta') if record.seq[-3:]==i.seq[:3] and record.id!=i.id]

# %%



