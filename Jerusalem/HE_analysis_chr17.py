from LE_func_chr17 import *
from LE_parse_chr17 import *
from LE_study_chr17 import *

import sys
sys.path.append('/Users/giuliobene3000/Desktop/Programming/Python/Bioinformatics')

from DNA_toolkit import translateseq

recovered_genes = []

for gene_idx in range(len(gene_sequences) - 1):

    current_gene = ''.join(gene_sequences[gene_idx])
    recovered_genes.append(current_gene)

recovered_genes_dict = dict(zip(gene_names, recovered_genes))

recovered_proteins = []

for gene in recovered_genes:

    current_protein = translateseq(gene)
    current_protein = ''.join(current_protein)
    recovered_proteins.append(current_protein)

recovered_proteins_dict = dict(zip(gene_names, recovered_proteins))

genes_of_interest = []

for x, y in recovered_genes_dict.items():

    if 'GCGCGCGCGC' in y:
        genes_of_interest.append(x)

    else:
        continue

print(f"[H] + Genes containing 'GCGCGCGCGC': {genes_of_interest}\n")

genes_of_interest2 = []

for x, y in recovered_proteins_dict.items():

    if 'RKRKRK' in y:
        genes_of_interest2.append(x)

    else:
        continue

print(f"[I] + Genes containing 'RKRKRK': {genes_of_interest2}\n")

