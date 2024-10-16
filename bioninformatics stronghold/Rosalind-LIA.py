# %%
from math import factorial as fc

def gen_prob(num_trials,num_sucess,ind_prob):
    prob_fc=(fc(num_trials)/(fc(num_sucess)*fc(num_trials-num_sucess))) * (ind_prob**num_sucess) * (1-ind_prob)**(num_trials-num_sucess)
    return prob_fc
    
def sum_prob(num_trials,num_sucess,ind_prob):
    prob=0
    for i in range(num_sucess,(2**num_trials)+1):
        prob+=gen_prob((2**num_trials),i,ind_prob)
        
    return round(prob,3)

# %%
sum_prob(5,9,0.25)


