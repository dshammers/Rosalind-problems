with open(r"C:\Users\Scott\OneDrive\Desktop\rosalind_med.txt") as f:
    n=int(f.readline().strip())
    median_list=[int(i) for i in f.readline().strip().split()]
    k=int(f.readline().strip())


def Median(n, median_list, k):
    v = n//2
    SL, SV, SR = [], [], []
    for i in range(n):
        if median_list[i] < median_list[v]: SL.append(median_list[i])
        if median_list[i] == median_list[v]: SV.append(median_list[i])
        if median_list[i] > median_list[v]: SR.append(median_list[i])
    if k <= len(SL):
        Median(len(SL), SL, k)
    if len(SL) < k and k <=len(SL)+len(SV):
        print(median_list[v])
        return median_list[v]
    if k > len(SL)+len(SV):
        Median(len(SR), SR, k-len(SL)-len(SV))


Median(n,median_list, k)