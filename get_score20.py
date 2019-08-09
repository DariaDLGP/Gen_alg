import random


nums_to_90 = []
for i in range(0, 90):
    nums_to_90.append(str(i))

def gen_alg20(func):
    chromo_1, chromo_2, chromo_3, chromo_4, chromo_5, chromo_6, chromo_7, chromo_8, chromo_9, chromo_10, chromo_11, chromo_12, chromo_13, chromo_14, chromo_15, chromo_16, chromo_17, chromo_18, chromo_19, chromo_20 = func
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    result5 = []
    result6 = []
    result7 = []
    result8 = []
    result9 = []
    result10 = []
    result11 = []
    result12 = []
    result13 = []
    result14 = []
    result15 = []
    result16 = []
    result17 = []
    result18 = []
    result19 = []
    result20 = []

    for i in range(len(chromo_1)):
        chromos20 = [chromo_1,chromo_2,chromo_3, chromo_4, chromo_5, chromo_6, chromo_7, chromo_8, chromo_9, chromo_10, chromo_11, chromo_12, chromo_13, chromo_14, chromo_15, chromo_16, chromo_17, chromo_18, chromo_19, chromo_20]
        rand1 = random.choice(chromos20)
        rand2 = random.choice(chromos20)
        choices = [rand1[i], rand2[i]]
        result1.append(random.choice(choices))
        result2.append(random.choice(choices))
        result3.append(random.choice(choices))
        result4.append(random.choice(choices))
        result5.append(random.choice(choices))
        result6.append(random.choice(choices))
        result7.append(random.choice(choices))
        result8.append(random.choice(choices))
        result9.append(random.choice(choices))
        result10.append(random.choice(choices))
        result11.append(random.choice(choices))
        result12.append(random.choice(choices))
        result13.append(random.choice(choices))
        result14.append(random.choice(choices))
        result15.append(random.choice(choices))
        result16.append(random.choice(choices))
        result17.append(random.choice(choices))
        result18.append(random.choice(choices))
        result19.append(random.choice(choices))
        result20.append(random.choice(choices))

    r =  [result1,result2,result3,result4,result5,result6,result7,result8,result9,result10,result11,result12,result13,result14,result15,result16,result17,result18,result19,result20]

    for res in r:
        seen3 = set()
        res3 = []
        diffs3 = list(set(nums_to_90) - set(res))
        for idx, item in enumerate(res[:90]):
            if item not in seen3:
                seen3.add(item)
            else:
                res3.append(idx)

        for i in res3:
            for jj in diffs3:
                res[i] = jj
                diffs3.remove(jj)



    return result1,result2,result3,result4,result5,result6,result7,result8,result9,result10,result11,result12,result13,result14,result15,result16,result17,result18,result19,result20

def mutation(func):
    chromo_1, chromo_2, chromo_3, chromo_4, chromo_5, chromo_6, chromo_7, chromo_8, chromo_9, chromo_10, chromo_11, chromo_12, chromo_13, chromo_14, chromo_15, chromo_16, chromo_17, chromo_18, chromo_19, chromo_20 = func
    mut1 = chromo_1[:]
    mut2 = chromo_2[:]
    mut3 = chromo_3[:]
    mut4 = chromo_4[:]
    mut5 = chromo_5[:]
    mut6 = chromo_6[:]
    mut7 = chromo_7[:]
    mut8 = chromo_8[:]
    mut9 = chromo_9[:]
    mut10 = chromo_10[:]
    mut11 = chromo_11[:]
    mut12 = chromo_12[:]
    mut13 = chromo_13[:]
    mut14 = chromo_14[:]
    mut15 = chromo_15[:]
    mut16 = chromo_16[:]
    mut17 = chromo_17[:]
    mut18 = chromo_18[:]
    mut19 = chromo_19[:]
    mut20 = chromo_20[:]

    muts = [mut1, mut2, mut3, mut4, mut5, mut6, mut7, mut8, mut9, mut10, mut11, mut12, mut13, mut14, mut15, mut16, mut17, mut18, mut19, mut20]

    for mut in muts:
        count1 = 0
        count2 = 0
        while count1 != 15:
            count1 += 1
            index1 = random.sample(range(0, 90), 1)
            index2 = random.sample(range(0, 90), 1)
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
            count2 += 1
            index3 = random.sample(range(90, 179), 1)
            index3 = index3[0]
            numbers = ["-1", "0", "1", "2", "3", "4", "5"]
            mut[index3] = random.choice(numbers)
        count2 = 0

    return muts


def mut_gen_alg20(func):
    chromo_1, chromo_2, chromo_3, chromo_4, chromo_5, chromo_6, chromo_7, chromo_8, chromo_9, chromo_10, chromo_11, chromo_12, chromo_13, chromo_14, chromo_15, chromo_16, chromo_17, chromo_18, chromo_19, chromo_20 = func
    result1_ = []
    result2_ = []
    result3_= []
    result4_ = []
    result5_ = []
    result6_ = []
    result7_ = []
    result8_ = []
    result9_ = []
    result10_ = []
    result11_ = []
    result12_ = []
    result13_ = []
    result14_ = []
    result15_ = []
    result16_ = []
    result17_ = []
    result18_ = []
    result19_ = []
    result20_ = []
    result21_ = []
    results_ = []

    for i in range(len(chromo_1)):
        chromos20 = [chromo_1, chromo_2, chromo_3, chromo_4, chromo_5, chromo_6, chromo_7, chromo_8, chromo_9,
                     chromo_10, chromo_11, chromo_12, chromo_13, chromo_14, chromo_15, chromo_16, chromo_17, chromo_18,
                     chromo_19, chromo_20]
        rand1 = random.choice(chromos20)
        rand2 = random.choice(chromos20)
        choices = [rand1[i], rand2[i]]
        result1_.append(random.choice(choices))
        result2_.append(random.choice(choices))
        result3_.append(random.choice(choices))
        result4_.append(random.choice(choices))
        result5_.append(random.choice(choices))
        result6_.append(random.choice(choices))
        result7_.append(random.choice(choices))
        result8_.append(random.choice(choices))
        result9_.append(random.choice(choices))
        result10_.append(random.choice(choices))
        result11_.append(random.choice(choices))
        result12_.append(random.choice(choices))
        result13_.append(random.choice(choices))
        result14_.append(random.choice(choices))
        result15_.append(random.choice(choices))
        result16_.append(random.choice(choices))
        result17_.append(random.choice(choices))
        result18_.append(random.choice(choices))
        result19_.append(random.choice(choices))
        result20_.append(random.choice(choices))
        result21_.append(random.choice(choices))

    for result_ in results_:
        count = 0
        while count != 21:
            count += 1
            index3 = random.sample(range(90, 179), 1)
            index3 = index3[0]
            numbers = ["-1", "0", "1", "2", "3", "4", "5"]
            result_[index3] = random.choice(numbers)
        count = 0
    return result1_, result2_,result3_,result4_,result5_,result6_,result7_, result8_,result9_,result10_,result11_,result12_,result13_, result14_,result15_,result16_,result17_,result18_,result19_,result20_


def add_chromos20(func1, func2, func3):
    #result_1, result_2,result_3,result_4,result_5,result_6,result_7, result_8,result_9,result_10,result_11,result_12,result_13, result_14,result_15,result_16,result_17,result_18,result_19,result_20,chromo_mutation = func
    shtuki = []
    values1 = []
    for i in func1:
        shtuki.append(i)

    for i in func2:
        shtuki.append(i)

    for i in func3:
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
            message = '''{}
'''.format(string)
            f.write(message)