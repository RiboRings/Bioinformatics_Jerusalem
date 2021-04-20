# Homework Exercise 1

# 2B

i_growth_A = 2
i_growth_B = 3

init_A = 10000
init_B = 100

lim1 = 10e8

f_growth_A = 1.5
f_growth_B = 1.8

lim2 = 10e10

limV = 10e6
perc_surv = 0.6
mrate_A = 0.1
mrate_B = 0.01

'''
number of bacteria during each day of the experiment?
days till growth stops?
proportion at end of experiment?
'''

days = []
day = 0
typeA = []
typeB = []
i_A = 0
i_B = 0

imm_A = 0
imm_B = 0
typeA_immune = []
typeB_immune = []

while i_A + i_B <= limV:
    i_A = round(init_A * i_growth_A ** day, 0)
    i_B = round(init_B * i_growth_B ** day, 0)

    typeA.append(i_A)
    typeB.append(i_B)
    typeA_immune.append(imm_A)
    typeB_immune.append(imm_B)

    days.append(day)

    day += 1

v_A = 0
v_B = 0
lead_time = len(days) - 1

while v_A + v_B <= lim1:
    v_A = round(i_A * (i_growth_A * perc_surv) ** (day - lead_time), 0)
    v_B = round(i_B * (i_growth_B * perc_surv) ** (day - lead_time), 0)
    imm_A = round(v_A * mrate_A, 0)
    imm_B = round(v_B * mrate_B, 0)

    typeA.append(v_A)
    typeB.append(v_B)
    typeA_immune.append(imm_A)
    typeB_immune.append(imm_B)

    days.append(day)

    day += 1

f_A = 0
f_B = 0

while f_A + f_B <= lim2:
    f_A = round(v_A * (f_growth_A * perc_surv) ** (day - lead_time), 0)
    f_B = round(v_B * (f_growth_B * perc_surv) ** (day - lead_time), 0)
    imm_A = round(f_A * mrate_A, 0)
    imm_B = round(f_B * mrate_B, 0)

    typeA.append(f_A)
    typeB.append(f_B)
    typeA_immune.append(imm_A)
    typeB_immune.append(imm_B)

    days.append(day)

    day += 1

print(f'number of days: {days}\n')
print(f'strain A: {typeA}\n')
print(f'strain B: {typeB}\n')
print(f'immune strain A: {typeA_immune}\n')
print(f'immune strain B: {typeB_immune}\n')

totalBac = typeA[-1] + typeB[-1] + typeA_immune[-1] + typeB_immune[-1]
perc_typeA = round(typeA[-1] / totalBac, 3)
perc_typeB = round(typeB[-1] / totalBac, 3)
perc_typeA_immune = round(typeA_immune[-1] / totalBac, 3)
perc_typeB_immune = round(typeB_immune[-1] / totalBac, 3)

results = {'A': perc_typeA, 'B': perc_typeB,
           'immune A': perc_typeA_immune, 'immune B': perc_typeB_immune}
print('Results: {}'.format(results))