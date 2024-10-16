# Let's solve the Rosalind REVP problem (Finding Reverse Palindromes).
# We'll break down the problem step by step.

# Problem:
# A DNA string is given, and the goal is to find all reverse palindromes in the string 
# between lengths 4 and 12.

# Steps:
# 1. Read the input DNA sequence.
# 2. For each substring of length 4 to 12, check if it is a reverse palindrome.
#    A reverse palindrome is a string that equals its reverse complement.
# 3. The reverse complement of a DNA sequence can be found by reversing the string and replacing
#    A with T, T with A, C with G, and G with C.

# Let's implement the solution now.

# Reverse complement dictionary for nucleotides
complement = str.maketrans("ATGC", "TACG")

def reverse_complement(seq):
    return seq.translate(complement)[::-1]

def find_reverse_palindromes(dna):
    palindromes = []
    
    # Loop through all possible substring lengths from 4 to 12
    for length in range(4, 13):
        for i in range(len(dna) - length + 1):
            sub_seq = dna[i:i + length]
            # Check if the substring is a reverse palindrome
            if sub_seq == reverse_complement(sub_seq):
                palindromes.append((i + 1, length))
    
    return palindromes

import sys

sys.path.append('callable_scripts')

import fasta_parser

dna_dict=fasta_parser.parse_fasta(r"C:\Users\Scott\OneDrive\Desktop\rosalind_revp.txt")

dna_seq=list(dna_dict.values())[0]

for i,j in find_reverse_palindromes(dna_seq):
    print (i,j)