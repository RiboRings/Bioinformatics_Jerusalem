# main file

from LE_parse_chr17 import *
from LE_func_chr17 import *

# B

gene_count = len(gene_names)
exon_count = len(exon_numbers)
mean_exon_per_gene = round(exon_count /gene_count, 1)

print(f'[B1] + Number of Genes: {gene_count}\n')
print(f'[B2] + Number of Exons: {exon_count}\n')
print(f'[B3] + Average Number of Exons per Gene: {mean_exon_per_gene}\n')

# C

exons_per_gene = []

for i in range(len(gene_sequences) - 1):

    num = len(gene_sequences[i])
    exons_per_gene.append(num)

gene_count_per_exon_number = []

for rep in range(1, max(exons_per_gene) + 1):

    tmpr_element = exons_per_gene.count(rep)
    gene_count_per_exon_number.append(tmpr_element)

gene_count_per_exon_number = dict(zip(range(1, max(exons_per_gene) + 1), gene_count_per_exon_number))

gene_count_per_exon_number = remove_null_values(gene_count_per_exon_number)

print(f'[C] + Number of Genes per Number of Exons (# exons: # genes): {gene_count_per_exon_number}\n')

# D

len_five_biggest_genes = sorted(exons_per_gene)[-5:]

five_biggest_genes = []

for length in len_five_biggest_genes:

    tmpr_idx = exons_per_gene.index(length)

    five_biggest_genes.append(gene_names[tmpr_idx])

print(f'[D] + Five biggest Genes: {five_biggest_genes}\n')

# E

mono_idx = get_index_positions(exons_per_gene, 1)

monoexon_genes = []

for idx in mono_idx:

    monoexon_genes.append(gene_names[idx])

print(f'[E] + Genes with one ORF Exon: {monoexon_genes}\n')

# how to write a new txt file
f = open('/Users/giuliobene3000/Desktop/Programming/Python/pdf_txt/genes_with_single_orf_exon.txt', 'w')
f.write('\n'.join(monoexon_genes))
f.close()

# F

length_exons = []

for exon in exon_sequences:

    length_exons.append(len(exon))

average_exon_length = round(sum(length_exons) / len(exon_sequences), 1)
print(f'[F] + Average Exon Length: {average_exon_length}\n')

# G

five_shortest_exons = sorted(exon_sequences, key=len)[:5]
print(f'[G] + Five shortest exons: {five_shortest_exons}\n')