# %%
def get_protein_fasta(file_path):
    import requests
    list_file=sorted(open(file_path,'r').read().splitlines())
    prot_dict={}
    for i in list_file:
        prot_file=requests.get(r'http://www.uniprot.org/uniprot/'+i[:6]+'.fasta')
        protein_fasta=prot_file.text.splitlines()
        if protein_fasta:
            del(protein_fasta[0])
            protein_fasta=''.join(protein_fasta)
            prot_dict[i]=protein_fasta

    return prot_dict

# %%
def find_glyc_seq(prot_dict):
        import re
        for i in prot_dict.keys():
            x=re.finditer('(?=N[^P][ST][^P])',prot_dict[i])
            y=[1+match.start() for match in x]
            if y:
                print (i)
                print (*y)

# %%
x=get_protein_fasta(r"C:\Users\Scott\OneDrive\Desktop\rosalind_mprt.txt")

# %%
find_glyc_seq(x)

# %%



