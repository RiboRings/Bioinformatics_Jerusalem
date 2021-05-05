# parsing file

from LE_func_chr17 import *

with open(r'/Users/giuliobene3000/Desktop/Programming/Python/pdf_txt/orf_exons_chr17.txt', 'r') as f:

    # This does not show the file content
    # print(f)
    # print('*' * 20)

    content = f.read()
    # print(content)

gene_names = []
exon_numbers = []
exon_sequences = []

for line in content.splitlines():

    if 'ORF Exon #' in line:

        ex_num, ex_seq = line.split(': ')

        ex_num = ex_num.replace(' ','_')
        ex_num = ex_num.replace('#', '')
        exon_numbers.append(ex_num)

        exon_sequences.append(ex_seq)

    else:
        gene = line.strip(':')
        gene_names.append(gene)


idx_initial_exon = get_index_positions(exon_numbers, 'ORF_Exon_1')

initial_exons = []

for idx in idx_initial_exon:

    initial_exons.append(exon_sequences[idx])

gene = []
gene_sequences = []

for i in range(len(idx_initial_exon) - 1):

    init = idx_initial_exon[i]
    end = idx_initial_exon[i + 1]

    gene = exon_sequences[init:end]
    gene_sequences.append(gene)

start_last_gene = idx_initial_exon[-1]
last_gene = exon_sequences[start_last_gene:]

gene_sequences.append(last_gene)

gene_data = dict(zip(gene_names, gene_sequences))
# print(gene_data)

listok = [1, 2, 3, 4, 5, 6, 7, 8]

print(listok[:-1])