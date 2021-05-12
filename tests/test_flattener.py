from flattener import FlatTheData
import unittest
import json


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
        file = open('../Sample2.json')
        array = json.loads(file.read())
        expected = [{'id': 1, 'values_0_a': 1, 'values_0_b': 2, 'values_0_c_d': 3, 'values_0_c_f': 4, 'values_1_a': 0.5,
                     'values_1_c_b': 3.2, 'values_2_a': 0.8, 'values_2_b': 1.8},
                    {'id': 2, 'values_0_a': 1, 'values_0_b': 2, 'values_0_c_d': 3, 'values_0_c_e': 4, 'values_1_a': 0.5,
                     'values_1_c_d': 3.2, 'values_2_a': 0.8, 'values_2_b': 1.8}]

        actual = [FlatTheData().get_flattened_data(d) for d in array]
        file.close()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
