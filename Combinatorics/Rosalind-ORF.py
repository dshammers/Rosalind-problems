
# parse fasta to obtain the sequences

import sys

sys.path.append(r"C:\Users\Scott\OneDrive\Documents\Python Scripts\callable_scripts")

import fasta_parser

dna_dict=fasta_parser.parse_fasta(r"C:\Users\Scott\OneDrive\Desktop\rosalind_orf.txt")

dna_seqs=list(dna_dict.values())

dna=dna_seqs[0]

#dictionary for translating between DNA codons and amino acids

dna_codon_table_one_letter = {
    'TTT': 'F', 'TTC': 'F',  # Phenylalanine
    'TTA': 'L', 'TTG': 'L',  # Leucine
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',  # Leucine
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I',  # Isoleucine
    'ATG': 'M',  # Methionine (Start codon)
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',  # Valine
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',  # Serine
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',  # Proline
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',  # Threonine
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',  # Alanine
    'TAT': 'Y', 'TAC': 'Y',  # Tyrosine
    'TAA': '*', 'TAG': '*',  # Stop codons
    'CAT': 'H', 'CAC': 'H',  # Histidine
    'CAA': 'Q', 'CAG': 'Q',  # Glutamine
    'AAT': 'N', 'AAC': 'N',  # Asparagine
    'AAA': 'K', 'AAG': 'K',  # Lysine
    'GAT': 'D', 'GAC': 'D',  # Aspartic acid
    'GAA': 'E', 'GAG': 'E',  # Glutamic acid
    'TGT': 'C', 'TGC': 'C',  # Cysteine
    'TGA': '*',  # Stop codon
    'TGG': 'W',  # Tryptophan
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',  # Arginine
    'AGT': 'S', 'AGC': 'S',  # Serine
    'AGA': 'R', 'AGG': 'R',  # Arginine
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'   # Glycine
}

#dictionary to obtain the reverse complement of the intital DNA string
rev_comp_dict={'A':'T','T':'A','C':'G','G':'C'}

#START OF FUNCTIONS


def rev_comp(str):

    '''Creates the reverse complement of a given DNA sequence'''
    
    rev_comp_dna=''

    for i in reversed(str):
        rev_comp_dna+=rev_comp_dict[i]

    return rev_comp_dna



def orf_finder(str):
    '''finds all possible Open Reading Frames from an input sequence'''
    
    first=[] #first reading frame
    second=[] #second reading frame, shifted one amino acid
    third=[] #third reading frame, shifted two amino acids

    count=1

    #sorts through each codon and puts it in the appropriate ORF
    for i in range(len(str)-2):    
        if count==1:
            first.append(str[i:i+3])
            count+=1

        elif count==2:
            second.append(str[i:i+3])
            count+=1
        
        elif count==3:
            third.append(str[i:i+3])
            count=1
    combined=[first,second,third]# list of lists containing each ORF

    return combined


def dna_translator(list):
    '''takes the lists from orf_finder() and translates them into amino acid sequences using the DNA codon table on line 18'''

    protein=''
    for i in list:
        protein+=dna_codon_table_one_letter[i]
    
    return protein




def extract_sequences(protein_str):
    ''' finds the amino acid sequences capable of being expressed as proteins. 
        Sequences go from the starting amino acid, 'M', to the stop signal, '*' '''
    
    sequences = []
    starts = []  # A list to track all starting positions of 'M'

    # Iterate through the string to find sequences that start with 'M' and end with '*'
    for i, char in enumerate(protein_str):
        if char == 'M':
            starts.append(i)  # Add each occurrence of 'M' to the list
        elif char == '*':
            # For each start position, extract the substring until this '*'
            for start in starts:
                sequences.append(protein_str[start:i])
            starts = []  # Reset after finding a valid sequence

    if len(sequences) > 0:
        return sequences #outputs a list of strings



def finalize_list():
    '''removes any None values and duplicate entries'''
    expressed_prot=[]
    
    for i in list_of_protein:
        x=extract_sequences(i) #looks for all expressable proteins in each Open Reading Frame (ORF)
    
        if x:   #excludes None values
            for j in x:   #pulls each element out of the list returned by extract_sequences()
                if j not in expressed_prot:   #prevents duplicate entries
                    expressed_prot.append(j)
    
    return expressed_prot #prints the list elements for easy copying into the Rosalind website answer box




#begin processing the DNA sequences extracted from the fasta file

if __name__=='__main__':   
    import sys

    sys.path.append(r"C:\Users\Scott\OneDrive\Documents\Python Scripts\callable_scripts")

    import fasta_parser

    dna_dict=fasta_parser.parse_fasta(r"C:\Users\Scott\OneDrive\Desktop\rosalind_orf.txt")
    dna_seqs=list(dna_dict.values())
    dna=dna_seqs[0]

    rev_dna=rev_comp(dna)

    fwd_seq1,fwd_seq2,fwd_seq3=orf_finder(dna)
    rev_seq1,rev_seq2,rev_seq3=orf_finder(rev_dna)

    list_of_orf=[fwd_seq1,fwd_seq2,fwd_seq3,rev_seq1,rev_seq2,rev_seq3]

    list_of_protein=[dna_translator(i) for i in list_of_orf]

    print(*finalize_list())