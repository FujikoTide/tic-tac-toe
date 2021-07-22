import numpy.lib.format

big_board = """
               ||               ||               
               ||               ||               
               ||               ||               
               ||               ||               
               ||               ||               
===============||===============||===============
               ||               ||               
               ||               ||               
               ||               ||               
               ||               ||               
               ||               ||               
===============||===============||===============
               ||               ||               
               ||               ||               
               ||               ||               
               ||               ||               
               ||               ||               
"""


bigger_collision = {
    0: True,
    16: True,
    17: True,
    33: True,
    34: True,
    50: True,
    66: True,
    67: True,
    83: True,
    84: True,
    100: True,
    116: True,
    117: True,
    133: True,
    134: True,
    150: True,
    166: True,
    167: True,
    183: True,
    184: True,
    200: True,
    216: True,
    217: True,
    233: True,
    234: True,
    250: True,
    251: True,
    252: True,
    253: True,
    254: True,
    255: True,
    256: True,
    257: True,
    258: True,
    259: True,
    260: True,
    261: True,
    262: True,
    263: True,
    264: True,
    265: True,
    266: True,
    267: True,
    268: True,
    269: True,
    270: True,
    271: True,
    272: True,
    273: True,
    274: True,
    275: True,
    276: True,
    277: True,
    278: True,
    279: True,
    280: True,
    281: True,
    282: True,
    283: True,
    284: True,
    285: True,
    286: True,
    287: True,
    288: True,
    289: True,
    290: True,
    291: True,
    292: True,
    293: True,
    294: True,
    295: True,
    296: True,
    297: True,
    298: True,
    299: True,
    300: True,
    316: True,
    317: True,
    333: True,
    334: True,
    350: True,
    366: True,
    367: True,
    383: True,
    384: True,
    400: True,
    416: True,
    417: True,
    433: True,
    434: True,
    450: True,
    466: True,
    467: True,
    483: True,
    484: True,
    500: True,
    516: True,
    517: True,
    533: True,
    534: True,
    550: True,
    551: True,
    552: True,
    553: True,
    554: True,
    555: True,
    556: True,
    557: True,
    558: True,
    559: True,
    560: True,
    561: True,
    562: True,
    563: True,
    564: True,
    565: True,
    566: True,
    567: True,
    568: True,
    569: True,
    570: True,
    571: True,
    572: True,
    573: True,
    574: True,
    575: True,
    576: True,
    577: True,
    578: True,
    579: True,
    580: True,
    581: True,
    582: True,
    583: True,
    584: True,
    585: True,
    586: True,
    587: True,
    588: True,
    589: True,
    590: True,
    591: True,
    592: True,
    593: True,
    594: True,
    595: True,
    596: True,
    597: True,
    598: True,
    599: True,
    600: True,
    616: True,
    617: True,
    633: True,
    634: True,
    650: True,
    666: True,
    667: True,
    683: True,
    684: True,
    700: True,
    716: True,
    717: True,
    733: True,
    734: True,
    750: True,
    766: True,
    767: True,
    783: True,
    784: True,
    800: True,
    816: True,
    817: True,
    833: True,
    834: True,
}

o_matrix = [
    [4, 5, 6, 7, 8, 9, 10, 11, 12],
    [53, 54, 62, 63],
    [103, 104, 112, 113],
    [153, 154, 162, 163],
    [204, 205, 206, 207, 208, 209, 210, 211, 212]
]

x_matrix = [
    [3, 4, 12, 13],
    [55, 56, 60, 61],
    [107, 108, 109],
    [155, 156, 160, 161],
    [203, 204, 212, 213]
]


pos_transform = [0, 17, 34, 300, 317, 334, 600, 617, 634]

center = [108, 125, 142, 408, 425, 442, 708, 725, 742]


def welcome():
    print("Welcome to Tic Tac Toe!!!")


class DisplayBoard:
    player = ""
    position = {}
    o_position = {}
    x_position = {}
    positions = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

    def __init__(self):
        self.player = DisplayBoard.player
        self.position = DisplayBoard.position
        self.o_position = DisplayBoard.o_position
        self.x_position = DisplayBoard.x_position
        self.positions = DisplayBoard.positions

    def mark_position(self, player: str, position: int) -> dict:
        d = []
        marker = []
        if player == 'x':
            matrix = x_matrix
        elif player == 'o':
            matrix = o_matrix

        for n in range(len(matrix)):
            a = numpy.array(matrix[n])
            b = pos_transform[position - 1]

            d.append(a + b)

        for n in d:
            for m in n:
                marker.append(m)

        pos_dict = {n: True for n in marker}
        return pos_dict

    def update_position(self, new_position: dict) -> dict:
        self.position.update(new_position)
        return self.position

    def print_board(self, board: dict):
        self.update_board()
        line = ""
        for k, v in enumerate(big_board):
            if k % 50 == 0:
                line += '\n'
            else:
                if bigger_collision.get(k):
                    line += '#'
                else:
                    if k in center and self.positions.get(center.index(k) + 1) == '':
                        line += str(center.index(k) + 1)
                    elif k in board:
                        line += 'X'
                    else:
                        line += ' '

        print(line)

    def update_board(self):
        for n in range(1, len(self.positions) + 1):
            if self.positions[n]:
                self.update_position(self.mark_position(self.positions.get(n), n))




