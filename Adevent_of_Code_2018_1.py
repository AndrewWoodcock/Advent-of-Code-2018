
data = "frequency.txt"


class Frequency:

    def __init__(self, freq: int):
        self.freq = freq

    def update_freq(self, val: int):
        self.freq += val


def get_file_data(filename):
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file]


def take_input(freqs: list, frequency: Frequency):
    for element in freqs:
        frequency.update_freq(element)


def main():
    freqs = get_file_data(data)
    dev_frequency = Frequency(0)
    take_input(freqs, dev_frequency)
    print("The new frequency is {0}".format(dev_frequency.freq))


if __name__ == '__main__':
    main()

