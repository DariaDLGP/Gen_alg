import csv


def parser(file):
    boxes = []
    box = {}
    data = {}
    count = 0

    with open(file) as csv_boxes:
        rd = csv.reader(csv_boxes, delimiter=',')
        for row in rd:
            if len(row) == 10:
                row.remove('')
                data['SKU'] = row[0]
                data['Quantity'] = row[1]
                data['Length'] = row[2]
                data['Width'] = row[3]
                data['Height'] = row[4]
                data['Square'] = int(data.get('Length')) * int(data.get('Width'))
                data['Volume'] = int(data.get('Square')) * int(data.get('Height'))
                box[str(count)] = data
                boxes.append(box)
                box = {}
                data = {}
                count += 1

    for i in range(len(boxes)):
        if int(boxes[i].get('{}'.format(i)).get('Quantity')) > 1:
            for j in range(1, int(boxes[i].get('{}'.format(i)).get('Quantity'))):
                boxes.append(dict.fromkeys(['{}'.format(len(boxes))], boxes[i].get('{}'.format(i))))

    return boxes
