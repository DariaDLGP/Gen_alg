from parser_csv_input import parser


def make_chromo(square, height):
    squares = ''
    heights = ''
    for i in square:
        squares += ',' + i
    for i in height:
        heights += ',' + i
    for i in range(len(square)):
        squares += ',' + '-1'
    for i in range(len(height)):
        heights += ',' + '-1'
    squares = squares[1:]
    heights = heights[1:]

    f_out = open('/Users/kseniaparygina/PycharmProjects/Korobki/papka/chromo.csv', 'w')
    message = '''{}
{}'''.format(squares, heights)
    f_out.write(message)
    f_out.close()

def sort_by_height(boxes):
    box = {}
    sorted_boxes = []
    for i, j in enumerate(boxes):
        box_height = int(j.get('{}'.format(list(boxes[i].keys())[0])).get('Height'))
        box[list(boxes[i].keys())[0]] = box_height
    box = sorted(box.items(), key=lambda item: -item[1])
    for i in box:
        sorted_boxes.append(i[0])
    return sorted_boxes

def sort_by_square(boxes):
    box = {}
    sorted_boxes = []
    for i, j in enumerate(boxes):
        box_height = int(j.get('{}'.format(list(boxes[i].keys())[0])).get('Square'))
        box[list(boxes[i].keys())[0]] = box_height
    box = sorted(box.items(), key=lambda item: -item[1])
    for i in box:
        sorted_boxes.append(i[0])
    return sorted_boxes


if __name__ == "__main__":
    make_chromo(sort_by_square(parser('1.csv')), sort_by_height(parser('1.csv')))


