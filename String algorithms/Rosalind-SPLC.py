# %%
import sys
sys.path.append('callable_scripts')

import fasta_parser
from DNA_functions import dna_codon_table_one_letter

dna_dict=fasta_parser.parse_fasta(r"C:\Users\Scott\OneDrive\Desktop\rosalind_splc.txt")

longest_seq=max(dna_dict.values(),key=len)

intron_seqs=list(dna_dict.values())


def find_introns(intron_seqs):
    '''finds the given introns within the longest DNA sequence'''
    introns=[]

    for i in intron_seqs:
        if len(i) < len(longest_seq):
            introns.append(i)
    
    return introns

# %%
def remove_introns(introns,longest_seq):
    '''removes the introns from the longest DNA sequence, leaving only exons'''
    for intron in introns:
        longest_seq=longest_seq.replace(intron,'')
    
    return longest_seq


def dna_translator(str):
    '''takes the lists from orf_finder() and translates them into amino acid sequences using the DNA codon table on line 18'''

    protein=''
    for i in range(0,len(str)-2,3):
        codon=str[i:i+3]
        amino_acid=dna_codon_table_one_letter[codon]
        if amino_acid!='*':
            protein+=amino_acid
    
    return protein

# %%
x=find_introns(intron_seqs)
y=remove_introns(x,longest_seq)
print(dna_translator(y))

# %%



