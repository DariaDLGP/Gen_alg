import random


nums_to_90 = []
for i in range(0, 90):
    nums_to_90.append(str(i))


def gen_alg_20(func):
    vals = []
    for i in range(20):
        chromo_1, chromo_2, chromo_3, chromo_4, chromo_5, chromo_6, chromo_7, chromo_8, chromo_9, chromo_10, chromo_11, chromo_12, chromo_13, chromo_14, chromo_15, chromo_16, chromo_17, chromo_18, chromo_19, chromo_20 = func

        chromos20 = [chromo_1, chromo_2, chromo_3, chromo_4, chromo_5, chromo_6, chromo_7, chromo_8, chromo_9, chromo_10,
                     chromo_11, chromo_12, chromo_13, chromo_14, chromo_15, chromo_16, chromo_17, chromo_18, chromo_19,
                     chromo_20]

        rand1 = random.choice(chromos20)
        rand2 = random.choice(chromos20)

        a = rand1
        b = rand2
        c = []
        index_a = 0
        index_b = 0
        while len(c) < 90:
            from_a = random.randint(0, 1) == 0
            if from_a:
                if a[index_a] not in c:
                    c.append(a[index_a])
                index_a += 1

            else:
                if b[index_b] not in c:
                    c.append(b[index_b])
                index_b += 1
        for i in range(90, 180):
            choices = [rand1[i], rand2[i]]
            c.append(random.choice(choices))
            # print(*c)
        # print(f"The array is :{str(c)}")
        # print(f"And this {'correct' if check_correct(c) else 'INCORRECT'}")
        vals.append(c)

    return vals


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
        while count1 != 21:
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
        while count2 != 15:
            count2 += 1
            index3 = random.sample(range(90, 179), 1)
            index3 = index3[0]
            numbers = ["-1", "0", "1", "2", "3", "4", "5"]
            mut[index3] = random.choice(numbers)
        count2 = 0

    return muts


def mut_gen_alg20(func):
    vals2 = []
    for i in range(20):
        chromo_1, chromo_2, chromo_3, chromo_4, chromo_5, chromo_6, chromo_7, chromo_8, chromo_9, chromo_10, chromo_11, chromo_12, chromo_13, chromo_14, chromo_15, chromo_16, chromo_17, chromo_18, chromo_19, chromo_20 = func

        chromos20 = [chromo_1, chromo_2, chromo_3, chromo_4, chromo_5, chromo_6, chromo_7, chromo_8, chromo_9,
                     chromo_10,
                     chromo_11, chromo_12, chromo_13, chromo_14, chromo_15, chromo_16, chromo_17, chromo_18, chromo_19,
                     chromo_20]

        rand1 = random.choice(chromos20)
        rand2 = random.choice(chromos20)

        a1 = rand1
        b1 = rand2
        c1 = []
        index_a1 = 0
        index_b1 = 0
        while len(c1) < 90:
            from_a = random.randint(0, 1) == 0
            if from_a:
                if a1[index_a1] not in c1:
                    c1.append(a1[index_a1])
                index_a1 += 1

            else:
                if b1[index_b1] not in c1:
                    c1.append(b1[index_b1])
                index_b1 += 1
        for i in range(90, 180):
            choices = [rand1[i], rand2[i]]
            c1.append(random.choice(choices))
            # print(*c)
        # print(f"The array is :{str(c)}")
        # print(f"And this {'correct' if check_correct(c) else 'INCORRECT'}")
        vals2.append(c1)

    for result_ in vals2:
        count = 0
        while count != 15:
            count += 1
            index3 = random.sample(range(90, 179), 1)
            index3 = index3[0]
            numbers = ["-1", "0", "1", "2", "3", "4", "5"]
            result_[index3] = random.choice(numbers)
        count = 0
    return vals2


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