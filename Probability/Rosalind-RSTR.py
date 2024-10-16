# The problem is to calculate the probability that at least one string from a collection of strings of a given length
# exactly matches a specific target sequence. Each string is generated randomly, with each nucleotide having a given probability.

# The input consists of two integers n and x, where n is the number of strings, x is the GC-content of the DNA string,
# followed by a target DNA sequence of length l.

# Here's how we can solve it step-by-step:
# 1. The probability of generating a specific character 'A' or 'T' is (1 - x)/2, and the probability of generating 'C' or 'G' is x/2.
# 2. For a given target sequence, we calculate the probability of generating the entire sequence based on these probabilities.
# 3. The probability that none of the n strings match the sequence is (1 - p)^n, where p is the probability of generating the sequence.
# 4. The probability that at least one string matches the sequence is 1 - (1 - p)^n.

# Here's the Python solution:

def probability_of_matching(n: int, x: float, target: str) -> float:
    '''Calculate probabilities of individual nucleotides'''
    
    n=int(n)
    x=float(x)
    
    p_at = (1 - x) / 2  # Probability of 'A' or 'T'
    p_gc = x / 2        # Probability of 'G' or 'C'
    
    # Calculate the probability of generating the target sequence
    p = 1.0
    for nucleotide in target:
        if nucleotide in "AT":
            p *= p_at
        else:  # nucleotide in "GC"
            p *= p_gc
    
    # Probability that at least one string matches the target sequence
    return 1 - (1 - p) ** n


with open(r"C:\Users\Scott\OneDrive\Desktop\rosalind_rstr.txt") as f:
    n,x=f.readline().strip().split()
    target=f.readline().strip()


print(probability_of_matching(n,x,target))