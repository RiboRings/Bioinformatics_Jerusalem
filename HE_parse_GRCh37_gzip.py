import os
import gzip
import csv
import json
from collections import defaultdict

DIR = r'/Users/giuliobene3000/Desktop/Programming/Python/pdf_txt'

# File taken from:
# ftp://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_29/GRCh37_mapping/gencode.v29lift37.annotation.gtf.gz

f = gzip.open(os.path.join(DIR, 'gencode.v29lift37.annotation.gtf.gz'), 'rt')
csv_reader = csv.reader(f, delimiter='\t')

for _ in range(5):
    next(csv_reader)

def parse_extra_fields(raw_extra_fields):

    extra_fields = {}

    for raw_extra_field in raw_extra_fields[:-1].split(';'):
        key, raw_value = raw_extra_field.strip().split(' ')
        value = raw_value.strip('"')
        extra_fields[key] = value

    return extra_fields

# A dictionary from chromosome name to a list of genes.
# Each gene is a tuple of 4 elements: gene_name (str), gene_type (str), start (int) and end (int).
genes_per_chromosome = defaultdict(list)
# A dictionary from gene name to a list of exons.
# Each exon is a (start, end) tuple.
exons_per_gene = defaultdict(list)

# We first explore the GENCODE database to see what annotation types and gene types are available within this dataset.
all_annotation_types = set()
all_gene_types = set()

for a_chr, _, a_type, a_start, a_end, _, _, _, raw_extra_fields in csv_reader:

    all_annotation_types.add(a_type)

    if a_type == 'gene':
        extra_fields = parse_extra_fields(raw_extra_fields)
        all_gene_types.add(extra_fields['gene_type'])
        genes_per_chromosome[a_chr].append((extra_fields['gene_name'], extra_fields['gene_type'], int(a_start), int(a_end)))

    elif a_type == 'exon':
        exons_per_gene[extra_fields['gene_name']].append((int(a_start), int(a_end)))

f.close()

print('All annotation types: ' + ', '.join(sorted(all_annotation_types)))
print('*' * 50)
print('All gene types: ' + ', '.join(sorted(all_gene_types)))
print('*' * 50)
print('Extracted %d genes in %d chromosomes and %d exons in %d genes.' % (sum(map(len, genes_per_chromosome.values())), len(genes_per_chromosome), sum(map(len, exons_per_gene.values())), len(exons_per_gene)))