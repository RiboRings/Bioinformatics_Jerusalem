 # functions
 
import random

def create_random_RNA():

    RNAstr = 'AUG'
    tmpr_list = [1, 2, 3, 4]

    while True:

        rchoice = random.choice(tmpr_list)

        if 'UAA' in RNAstr or 'UAG' in RNAstr or 'UGA' in RNAstr:
            break

        elif rchoice == 1:
            RNAstr += 'A'

        elif rchoice == 2:
            RNAstr += 'C'

        elif rchoice == 3:
            RNAstr += 'G'

        else:
            RNAstr += 'U'
        
    return RNAstr
