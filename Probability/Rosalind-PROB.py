with open(r"C:\Users\Scott\OneDrive\Desktop\rosalind_prob.txt") as f:
    base_str=f.readline().strip()
    list_of_prob=[float(i) for i in f.readline().strip().split()]


import math


def random_str_prob(s,arr):
    result=[]
    for gc_content in arr:
        prob=1
        for base in s:
            if base in 'GC':
                prob *= gc_content/2
            else:
                prob *= (1-gc_content)/2

        result.append(math.log10(prob))
    print (*result)

random_str_prob(base_str,list_of_prob)

