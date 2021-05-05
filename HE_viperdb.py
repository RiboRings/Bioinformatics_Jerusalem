import csv

with open('/Users/giuliobene3000/Desktop/Programming/Python/pdf_txt/viperdb.csv', 'r') as viperdb_file:
    viperdb = csv.DictReader(viperdb_file)

    '''for line in viperdb:
        print(line)'''

# A - find the record with the highest outer radius for each genus

    genus_list = []
    outer_radius_list = []
    genome = []
    SASA = []

    for line in viperdb:
        genus_list.append(line['Genus'])
        outer_radius_list.append(line['Outer Radius'])

        genome.append(line['Genome'])
        SASA.append(line['Outside SASA'])

    outer_radius_list = [int(x) for x in outer_radius_list]
    # genus_list = filter(lambda x: x != 'N/A', genus_list)

    genus_radius_dict = list(zip(genus_list, outer_radius_list))
    genus_set = {genus for genus in genus_list}

    
    outer_radius_maxima = []

    for genus in genus_set:

        tmpr_list = []

        for species, radius in genus_radius_dict:

            if species == genus:
                    tmpr_list.append(radius)

            else:
                continue

        outer_radius_maxima.append(max(tmpr_list))
    
    outer_radius_maxima = dict(zip(genus_set, outer_radius_maxima))
    print(f'Maximal outer Radii for each Genus: {outer_radius_maxima}\n')

# B - find average surface area of the capsid for the categories ssDNA, dsDNA, ssRNA, dsRNA

    ssDNA = []
    dsDNA = []
    ssRNA = []
    dsRNA = []

    SASA = [int(x) for x in filter(lambda y: y != 'N/A', SASA)]

    genome_surface_dict = list(zip(genome, SASA))

    for genome, surface in genome_surface_dict:

        if 'ssDNA' in genome:
            ssDNA.append(surface)

        elif 'dsDNA' in genome:
            dsDNA.append(surface)
        
        elif 'ssRNA' in genome:
            ssRNA.append(surface)

        else:
            dsRNA.append(surface)

    print(f'Surface Area of the Capsid for ssDNA: {max(ssDNA):,} Square Amstrong\n')
    print(f'Surface Area of the Capsid for dsDNA: {max(dsDNA):,} Square Amstrong \n')
    print(f'Surface Area of the Capsid for ssRNA: {max(ssRNA):,} Square Amstrong\n')
    print(f'Surface Area of the Capsid for dsRNA: {max(dsRNA):,} Square Amstrong\n')

    '''for element in genus:
        ex[genus] = filter(lambda x: x == genus)'''
