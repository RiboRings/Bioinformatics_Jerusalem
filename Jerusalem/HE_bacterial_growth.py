# Homework Exercise 1

# 2A

i_growth_A = 2
i_growth_B = 3

init_A = 10000
init_B = 100

lim1 = 10e8

f_growth_A = 1.5
f_growth_B = 1.8

lim2 = 10e10

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

while i_A + i_B <= lim1:
    i_A = round(init_A * i_growth_A ** day, 0)
    i_B = round(init_B * i_growth_B ** day, 0)

    typeA.append(i_A)
    typeB.append(i_B)

    day += 1

    days.append(day)

# print(days)
# print(typeA)
# print(typeB)

f_A = 0
f_B = 0
lead_time = len(days) - 1

while f_A + f_B <= lim2:
    f_A = round(i_A * f_growth_A ** (day - lead_time), 0)
    f_B = round(i_B * f_growth_B ** (day - lead_time), 0)

    typeA.append(f_A)
    typeB.append(f_B)

    day += 1

    days.append(day)

print(days)
print(typeA)
print(typeB)

results = {}

for i in days:
    results[i] = [f'A: {typeA[i-1]}; B: {typeB[i-1]}']

print(results)
