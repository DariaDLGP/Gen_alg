import csv
import subprocess
import os
import random


nums_to_90 = []
for i in range(0, 90):
    nums_to_90.append(str(i))

def make():
    os.chdir('/Users/kseniaparygina/PycharmProjects/Korobki/papka/')
    subprocess.run(['make'])

def start_layout():
    os.chdir('/Users/kseniaparygina/PycharmProjects/Korobki/papka/')
    subprocess.run(['./layout'])

def len_check(path):
    with open(os.path.join(path), newline='') as f:
        file = csv.reader(f)
        count = 0
        for row in file:
            count += 1
    return count

#-------------------------------------------------------------------

#---------------------------------------------------------------------------------------

def get_chromos():
    values = []
    indexes = []
    with open('/Users/kseniaparygina/PycharmProjects/Korobki/papka/chromo.csv', newline='') as f1:
        file = csv.reader(f1)
        for row in file:
            values.append(row)
    for i in range(len(values)):
        indexes.append(i)
    #ОБЕ ХРОМОСОМЫ МОГУТ БЫТЬ ОДИНАКОВЫМИ, ИСПРАВЛЕНО

    random_index = random.choice(indexes)
    chromo_1 = values[random_index]
    indexes.remove(random_index)
    chromo_2 = values[random.choice(indexes)]

    return chromo_1, chromo_2


def gen_alg6(func):
    chromo_1, chromo_2 = func
    result_1 = []
    result_2 = []
    result_3 = []
    result_4 = []
    result_5 = []
    result_6 = []
    mut1 = chromo_1[:]
    mut2 = chromo_1[:]
    mut3 = chromo_1[:]
    mut4 = chromo_2[:]
    mut5 = chromo_2[:]
    mut6 = chromo_2[:]
    muts = [mut1, mut2, mut3, mut4, mut5, mut6]

    for i in range(len(chromo_1)):
        choices = [chromo_1[i],chromo_2[i]]
        result_1.append(random.choice(choices))
        result_2.append(random.choice(choices))
        result_3.append(random.choice(choices))
        result_4.append(random.choice(choices))
        result_5.append(random.choice(choices))
        result_6.append(random.choice(choices))

    r = [result_1, result_2, result_3, result_4, result_5, result_6, mut1, mut2, mut3, mut4, mut5, mut6]

#мутация
    for mut in muts:
        count1 = 0
        count2 = 0
        while count1 != 15:
            count1 +=1
            index1 = random.sample(range(0,90),1)
            index2 = random.sample(range(0, 90),1)
            new_el1 = mut[index1[0]]
            new_el2 = mut[index2[0]]
            if isinstance(new_el1, list):
                new_el1 = str(new_el1[0])
                mut[index2[0]] = new_el1
            else:
                mut[index2[0]] = new_el1

            if isinstance(new_el2, list):
                new_el2 = str(new_el2[0])
                mut[index1[0]] = new_el2
            else:
                mut[index1[0]] = new_el2

        count1 = 0
        while count2 != 21:
            count2 +=1
            index3 = random.sample(range(90,179),1)
            index3 = index3[0]
            numbers = ["-1", "0", "1", "2", "3", "4", "5"]
            mut[index3] = random.choice(numbers)
        count2 = 0

    for res in r:
        seen = set()
        result = []
        diffs = list(set(nums_to_90) - set(res))
        for idx, item in enumerate(res[:90]):
            if item not in seen:
                seen.add(item)
            else:
                result.append(idx)

        for i in result:
            for j in diffs:
                res[i] = j
            diffs.remove(j)
        print(len(res))

    return r

def mut_gen(func):
    chromo_1, chromo_2 = func
    Mresult_1 = []
    Mresult_2 = []
    Mresult_3 = []
    Mresult_4 = []
    Mresult_5 = []
    Mresult_6 = []
    Mresults = [Mresult_1, Mresult_2, Mresult_3, Mresult_4, Mresult_5, Mresult_6]
    for i in range(len(chromo_1)):
        choices = [chromo_1[i],chromo_2[i]]
        Mresult_1.append(random.choice(choices))
        Mresult_2.append(random.choice(choices))
        Mresult_3.append(random.choice(choices))
        Mresult_4.append(random.choice(choices))
        Mresult_5.append(random.choice(choices))
        Mresult_6.append(random.choice(choices))
    for result in Mresults:
        count = 0
        while count != 21:
            count += 1
            index3 = random.sample(range(90, 179), 1)
            index3 = index3[0]
            numbers = ["-1", "0", "1", "2", "3", "4", "5"]
            result[index3] = random.choice(numbers)
        count = 0

    for res in Mresults:
        seen2 = set()
        result2 = []
        diffs2 = list(set(nums_to_90) - set(res[:90]))
        for idx, item in enumerate(res[:90]):
            if item not in seen2:
                seen2.add(item)
            else:
                result2.append(idx)

        for i in result2:
            for jj in diffs2:
                res[i] = jj
            diffs2.remove(jj)


    return Mresult_1, Mresult_2, Mresult_3, Mresult_4, Mresult_5, Mresult_6

def add_chromos6(func1, func2):
    #result_1, result_2,result_3,result_4,result_5,result_6, Mresult_1, Mresult_2, Mresult_3, Mresult_4, Mresult_5, Mresult_6, mut1, mut2, mut3, mut4, mut5, mut6 = func
    shtuki = []
    values1 = []
    for i in func1:
        shtuki.append(i)

    for i in func2:
        shtuki.append(i)

    for shtuka in shtuki:
        chrom = ''
        for i in shtuka:
            chrom += ',' + i
        chrom = chrom[1:]
        values1.append(chrom)
        chrom = ''

    with open('/Users/kseniaparygina/PycharmProjects/Korobki/papka/chromo.csv', 'a') as f:
        for string in values1:
            message = '''
{}'''.format(string)
            f.write(message)


