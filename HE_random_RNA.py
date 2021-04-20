# main

import random
from HE_func_random_RNA import *

RNAstr_list = []
length_list = []
gc_content = []

for rep in range(1000):

    RNAstr = create_random_RNA()

    RNAstr_list.append(RNAstr)
    length_list.append(len(RNAstr))

    gc_con = (RNAstr.count('G') + RNAstr.count('C')) / len(RNAstr)
    gc_content.append(gc_con)
    
average_length = round(sum(length_list) / len(length_list), 1)
print(f'Average Length: {average_length} nucleotides\n')

average_gc_content= round(sum(gc_content) / len(gc_content), 3)
print(f'Average GC Content: {average_gc_content}%\n')

experimental_function = dict(zip(gc_content, length_list))
export_data = []

for x, y in experimental_function.items():

    # print(f'{round(x, 3)}% : {y} nucleotides\n')
    export_data.append(f'{x}, {y}')

f = open('/Users/giuliobene3000/Desktop/Programming/Python/pdf_txt/n_nucleotides_vs_gc_content_data.txt', 'w')
f.write('\n'.join(export_data))
f.close()

print('Average length is directly proportional to average gc content. Refer to the Excel file "ex_python".')

