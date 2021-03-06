#!/usr/local/bin/python3

# Lab Exercise 1

import sys
sys.path.append(
    '/Users/giuliobene3000/Desktop/Programming/Python/Bioinformatics')

from strucs import *
from DNA_toolkit import *

my_sequence = 'ATGGGTGCGAGAGCGTCAGTATTAAGCGGGGGAGAATTAGATCGATGGGAAAAAATTCGGTTAAGGCCAGGGGGAAAGAAA\
AAATATAAATAAAACATATAGTATGGGCAAGCAGGGAGCTAGAACGATTCGCAGTTAATCCTGGCCTGTTAGAAACATCAGA\
AGGCTGTAGACAAATACTGGGACAGCTACAACCATCCCTTCAGACAGGATCAGAAGAACTTAGATCATTATATAATACAGTAGC\
AACCCTCTATTGTGTGCATCAAAGGATAGAGATAAAAGACACCAAGGAAGCT'

print(gc_content(my_sequence))

print(translateseq(my_sequence))
