import csv


def get_best_score():
    values = []
    indexes = []
    chromos = []
    new_chromos = []
    with open('/Users/kseniaparygina/PycharmProjects/Korobki/papka/score.csv', newline='') as f1:
        file = csv.reader(f1)
        for row in file:
            values.append(float(row[0]))

    sorted_values = sorted(values, key=float)
    sorted_values.reverse()
    sorted_values = list(set(sorted_values))
    sorted_values = sorted_values[:20]
    for sorted_value in sorted_values:
        for value in values:
            if sorted_value == value:
                indexes.append(values.index(value))

    with open('/Users/kseniaparygina/PycharmProjects/Korobki/papka/score.csv', 'w') as f2:
        for i in sorted_values:
            message = '''{}
'''.format(i)
            f2.write(message)

    with open('/Users/kseniaparygina/PycharmProjects/Korobki/papka/chromo.csv', newline='') as f3:
        file = csv.reader(f3)
        for row in file:
            chromos.append(row)
    for index in indexes:
        if chromos[index]:
            new_chromos.append(chromos[index])

    with open('/Users/kseniaparygina/PycharmProjects/Korobki/papka/chromo.csv', 'w') as f4:
        for i in new_chromos[:20]:
            i = str(i)[1:-1].replace(' ', '').replace("'", '')
            message = '''{}
'''.format(i)
            f4.write(message)
    return new_chromos[:20]