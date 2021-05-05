# Lab Exercise 4.1

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Bio.Alphabet was removed in 2020
# from Bio.Alphabet import Alphabet

with open('/Users/giuliobene3000/Desktop/Programming/Python/pdf_txt/hgb.txt', 'r') as fasta_file:

    # seqIO.parse returns an iterator of records
    # in this case there is only one sequence in the FASTA file
    for record in SeqIO.parse(fasta_file, 'fasta'):
        print('ID: ' + record.id)
        print('Description: ' + record.description)
        print('DNA Sequence:')
        print(record.seq)
        print('*' * 20)
        DNA_seq  = record.seq

# my_DNA = Seq('ACTGTTGCAACCAGT')
# my_RNA = Seq('ACUUUGCACCAUACACACCCGU')
# my_pep = Seq('XYWMLIF')

# print(my_DNA, len(my_DNA), type(my_DNA))
# print(my_RNA, len(my_RNA), type(my_RNA))
# print(my_pep, len(my_pep), type(my_pep))

RNA_seq = DNA_seq.transcribe()
print('RNA Sequence:')
print(RNA_seq)
print('*' * 20)

records = SeqRecord(RNA_seq, id='MG657341', description='Homo sapiens hemoglobin subunit beta (HBB) gene, complete cds.')

with open('/Users/giuliobene3000/Desktop/Programming/Python/pdf_txt/hgb_RNA.txt', 'w') as output_fasta:

    SeqIO.write(records, output_fasta, 'fasta')
