# %%
from Bio import AlignIO,motifs
msa=AlignIO.read(r"C:\Users\Scott\OneDrive\Desktop\rosalind_cons.txt",'fasta')
msa=AlignIO.MultipleSeqAlignment(msa)
mot=motifs.create(msa)
print(mot.consensus)


