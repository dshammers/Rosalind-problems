# %%
import sys
import math
sys.path.append('callable_scripts')

from fasta_parser import parse_fasta

seq_dict=parse_fasta(r'c:\Users\Scott\OneDrive\Desktop\rosalind_pmch.txt')

target_seq=list(seq_dict.values())[0]

def count_perfect_matchings(rna_sequence):

    num_A=rna_sequence.count('A')
    num_C=rna_sequence.count('C')
    num_G=rna_sequence.count('G')
    num_U=rna_sequence.count('U')

    if num_C != num_G or num_A != num_U:
        raise ValueError ('invalid RNA sequence: Mismatched number of base pairs.')

    return math.factorial(num_A) * math.factorial(num_C)




# %%
count_perfect_matchings(target_seq)

# %%



