# %%
import icecream as ic

import sys

sys.path.append('callable_scripts')

from fasta_parser import parse_fasta

seq_dict=parse_fasta(r"C:\Users\Scott\OneDrive\Desktop\rosalind_sseq.txt")

target_seqs=list(seq_dict.values())

seq_to_idx=min(target_seqs,key=len)
seq_to_itr=max(target_seqs,key=len)


def find_idx_of_small_in_large(idx_str,itr_str):
    
    '''find indices of each codon in the shorter string in the longer string'''
    idx=0
    
    for nuc in range(len(itr_str)-1):
        if idx >= len(idx_str):
            break
        
        elif itr_str[nuc]==idx_str[idx]:
            print (nuc+1,end=' ')
            idx+=1
            

# %%
find_idx_of_small_in_large(seq_to_idx,seq_to_itr)


