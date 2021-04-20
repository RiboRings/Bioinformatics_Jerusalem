# how to study a json file before opening it

from LE_func_herpesvirus import find_extrema
import json

import sys
sys.path.append(
    '/Users/giuliobene3000/Desktop/Programming/Python/Bioinformatics')
from strucs import Aminoacids

with open(r'/Users/giuliobene3000/Desktop/Programming/Python/pdf_txt/herpesvirus_genome.json', 'r') as f:
    data = json.load(f)

# parse the data

print(type(data))
print(len(data), '\n')

for key, value in data.items():
    print(key, type(value))

print('\n')

for key, value in data.items():
    if key != 'coding_regions':
        print(f'{key}, {value}')

print('\n')

coding_regions = data['coding_regions']
print(f'type of coding_regions: {type(coding_regions)}')
print(f'length of coding_regions: {len(coding_regions)}', '\n')

for cod_reg in coding_regions:
    print(f'type: {type(cod_reg)}, length: {len(cod_reg)}')

print('\n')

for key, value in coding_regions[0].items():
    print(key, type(value))

print('\n')

for key, value in coding_regions[0].items():
    if key != 'intervals':
        print(f'{key}, {value}')

print('\n')

coding_region = coding_regions[0]

interval, = coding_region['intervals']  # Here I don't save intervals, but what's inside
print(type(interval), len(interval))

for key, value in interval.items():
    print(key, type(value))

print(interval)

print('\n')

# A: aminoacid frequency in the entire proteome

proteome = []

for coding_region in coding_regions:

    tmpr_seq = coding_region['translation']
    proteome.append(tmpr_seq)

uni_proteome = ''.join(proteome)
aa_frequency = []

for aa in Aminoacids:
    aa_count = uni_proteome.count(aa)
    tmpr_freq = round(aa_count / len(uni_proteome), 3)
    
    aa_frequency.append(tmpr_freq)

aa_frequency = dict(zip(Aminoacids, aa_frequency))
print(f'Aminoacid Frequency: {aa_frequency}')

# B: aminoacid frequency in envelope, membrane and capsid

product_list = [cod_reg['product'] for cod_reg in coding_regions]
translation_list = [cod_reg['translation'] for cod_reg in coding_regions]

envelope = []
membrane = []
capsid = []
other = []

for idx, product in enumerate(product_list):

    if 'membrane' in product:
        membrane.append(translation_list[idx])
    
    elif 'capsid' in product:
        capsid.append(translation_list[idx])

    elif 'envelope' in product:
        envelope.append(translation_list[idx])

    else:
        other.append(translation_list[idx])

uni_envelope = ''.join(envelope)
uni_membrane = ''.join(membrane)
uni_capsid = ''.join(capsid)

env_frequency = []
mem_frequency = []
cap_frequency = []

for aa in Aminoacids:

    envelope_count = uni_envelope.count(aa)
    membrane_count = uni_membrane.count(aa)
    capsid_count = uni_capsid.count(aa)

    tmpr_env_freq = round(envelope_count / len(uni_envelope), 3)
    tmpr_mem_freq = round(membrane_count / len(uni_membrane), 3)
    tmpr_cap_freq = round(capsid_count / len(uni_capsid), 3)

    env_frequency.append(tmpr_env_freq)
    mem_frequency.append(tmpr_mem_freq)
    cap_frequency.append(tmpr_cap_freq)

env_frequency = dict(zip(Aminoacids, env_frequency))
mem_frequency = dict(zip(Aminoacids, mem_frequency))
cap_frequency = dict(zip(Aminoacids, cap_frequency))

env_extrema = find_extrema(env_frequency)
mem_extrema = find_extrema(mem_frequency)
cap_extrema = find_extrema(cap_frequency)

print(cap_extrema)