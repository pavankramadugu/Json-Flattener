from flattener import FlatTheData
import unittest
import pandas


class TestFlatTheData(unittest.TestCase):

    def test_json(self):
        dic = {
            'a': 1,
            'b': 2,
            'c': [{'d': [2, 3, 4], 'e': [{'f': 1, 'g': 2}]}]
        }
        expected = {'a': 1, 'b': 2, 'c_0_d_0': 2, 'c_0_d_1': 3, 'c_0_d_2': 4,
                    'c_0_e_0_f': 1, 'c_0_e_0_g': 2}
        actual = FlatTheData().get_flattened_data(dic)
        self.assertEqual(expected, actual)

    def test_list(self):
        array = [
            {
                "a": 1,
                "b": 2,
                "c_d": 3,
                "c_e": 4
            },
            {
                "a": 0.5,
                "c_d": 3.2
            },
            {
                "a": 0.8,
                "b": 1.8
            }
        ]
        expected = [{'a': 1, 'b': 2, 'c_d': 3, 'c_e': 4}, {'a': 0.5, 'c_d': 3.2}, {'a': 0.8, 'b': 1.8}]

        actual = [FlatTheData().get_flattened_data(d) for d in array]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
