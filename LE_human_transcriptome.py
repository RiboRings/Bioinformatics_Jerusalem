# Lab Exercise 4.2

import csv
import gzip
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import GC

# A, B and C

with gzip.open('/Users/giuliobene3000/Desktop/Programming/Python/pdf_txt/GRCh38_latest_rna.fna.gz', 'rt') as human_transcriptome:

    IDs = []
    sequences = []
    lengths = []

    for record in SeqIO.parse(human_transcriptome, 'fasta'):

        IDs.append(record.id)
        sequences.append(record.seq)
        lengths.append(len(record.seq))
    
    length_longest_transcript = max(lengths)
    idx = lengths.index(length_longest_transcript)

    longest_transcript = IDs[idx]
    GC_longest_transcript = GC(sequences[idx])

    print(f'Longest transcript in humans: {longest_transcript}, with a length of {length_longest_transcript} nucleotides.')
    print(f'GC content: {round(GC_longest_transcript, 3)}%')
    print('*' * 20)

# From NCBI RefSeq at: https://www.ncbi.nlm.nih.gov/nuccore/NM_001267550.2?report=genbank&log$=seqview

with open('/Users/giuliobene3000/Desktop/Programming/Python/pdf_txt/titin_sequence.gb', 'r') as titin_file:

    titin_record, = SeqIO.parse(titin_file, 'genbank')
    
    titin_sequence = titin_record.seq

# print(titin_record.seq)
    
exons = []
exon_GC_contents = []

for feature in titin_record.features:

    if feature.type == 'exon':

        exons.append((int(feature.location.start), int(feature.location.end)))

    else:
        continue

exon_lengths = []

for exon in exons:

    exon_length = exon[1] - exon[0]
    exon_lengths.append(exon_length) 

length_longest_exon = max(exon_lengths)
idx = exon_lengths.index(length_longest_exon)

longest_exon = exons[idx]
print(f'The longest exon in {titin_record.id} is {longest_exon}, with a length of {length_longest_exon} nucleotides.')
print('*' * 20)

# D

for start, end in exons:

    tmpr_seq = titin_sequence[start - 1:end - 1]
    tmpr_GC_content = round((tmpr_seq.count('G') + tmpr_seq.count('C')) / (end - start), 3) * 100
    exon_GC_contents.append(tmpr_GC_content)

highest_GC_content = max(exon_GC_contents)
idx = exon_GC_contents.index(highest_GC_content)

max_GC_exon = exons[idx]
print(f'Among a total of {len(exons)} exons, the one with the highest GC content ({round(highest_GC_content, 3)}%) is {max_GC_exon}.')

# E

aa_sequence = titin_sequence.translate()
frequency_dict = {}

for aa in set(aa_sequence):

    tmpr_count = aa_sequence.count(aa)
    frequency_dict[aa] = round(tmpr_count / len(aa_sequence), 4)

print('Aminoacid Frequencies in Titin Sequence:')
print(frequency_dict)

# close to 1 --- correct!
# print(sum(frequency_dict.values()))
