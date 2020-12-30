
# boxes = "warehouse_test.txt"
boxes = "warehouse.txt"


class Box:

    twos_threes = {2: 0,
                   3: 0}

    def __init__(self, ident):
        self.ident = ident

    def id_counts(self) -> dict:
        counts_dict = {}
        for element in self.ident:
            if element not in counts_dict:
                counts_dict[element] = 1
            else:
                counts_dict[element] += 1
        return counts_dict

    def tally_counts(self):
        two = False
        three = False
        for element, count in self.id_counts().items():
            if count == 2 and two is False:
                self.twos_threes[count] += 1
                two = True
            elif count == 3 and three is False:
                self.twos_threes[count] += 1
                three = True


def get_file_data(filename: str) -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file]


def main():
    box_data = get_file_data(boxes)
    for box in box_data:
        box_obj = Box(box)
        box_obj.id_counts()
        box_obj.tally_counts()

    twos = Box.twos_threes[2]
    threes = Box.twos_threes[3]
    checksum = twos * threes

    print("The checksum product is {0}".format(checksum))


if __name__ == '__main__':
    main()
