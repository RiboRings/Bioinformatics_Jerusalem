def find_extrema(frequency_dict):

    frequency_list = list(frequency_dict.values())
    name_list = list(frequency_dict.keys())

    max1 = max(frequency_list)
    min1 = min(frequency_list)

    max_diff = 100000000000
    min_diff = 100000000000

    max2 = 0
    min2 = 0

    for entry in frequency_dict.values():

        if max1 - entry < max_diff:

            max2 = entry
            max_diff = max1 - max2

        else:
            continue

        if entry - min1 < min_diff:

            min2 = entry
            min_diff = min2 - min1

        else:
            continue


    extrema = [min1, min2, max2, max1]
    ex_names = []

    for ex in extrema:

        idx = frequency_list.index(ex)
        ex_names.append(name_list[idx])

    extrema_dict = dict(zip(ex_names, extrema))

    return extrema_dict