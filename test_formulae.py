from functools import reduce
import unittest

import formulae as fx

class TestFormulae(unittest.TestCase):
    pass


class TestGenerator():
    def __init__(self):
        self.data = load_test_data()

        for test in self.generate_tests():
            setattr(TestFormulae, test.__name__, test)


    def generate_tests(self) -> '[function]':
        for label in self.data.keys():
            for values in self.data[label]:
                inputs = {'interest': 0.01, 'periods': values[0]}

                def test(self):
                    func = getattr(fx, parse_label(label))
                    result = func(**inputs)
                    expected = values[1]

                    self.assertAlmostEqual(result, expected, 2,
                            '\n\tTesting {} with input {}'
                            .format(parse_label(label), inputs))

                test.__name__ += '{}{}'.format(parse_label(label), values[0])
                yield test


def load_test_data() -> dict:
    data = {}

    with open('test_data_1_percent_discrete.data') as f:
        raw_data = f.read().split('\n')[:-1];

    labels = raw_data[0].split()[1:]

    data_parsed = parse_data(raw_data[1:])
    # i+1 because first column is n values
    data = {labels[i]: column(data_parsed, i+1) for (i,n) in enumerate(labels)}

    return data


def parse_data(raw_data: [str]) -> [float]:
    data = []
    for row in raw_data:
        row_split = row.split()
        func = lambda init, i: init + [float(i)]
        data.append(reduce(func, row_split, []))

    return data


def parse_label(label):
    return label.replace('/', 'g')


def column(array: [[float]], col) -> '(n, value)':
    return [(array[i][0], array[i][col]) for (i,n) in enumerate(array)]


if __name__ == '__main__':
    test_generator = TestGenerator()
    unittest.main()
