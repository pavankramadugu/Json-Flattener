import json
import pandas as pd


class FlatTheData:
    def __init__(self):
        self.separator = "_"

    @staticmethod
    def get_key(previous_key, separator, new_key):
        if previous_key:
            return u"{}{}{}".format(previous_key, separator, new_key)
        else:
            return new_key

    def get_flattened_data(self, nested_data):
        assert isinstance(nested_data, dict), "Provide a Json Object"

        if len(nested_data) == 0:
            return {}

        flattened_data = dict()

        def flatten(dataset, key):

            if not dataset:
                flattened_data[key] = dataset

            elif isinstance(dataset, dict):
                for data_key in dataset:
                    flatten(
                        dataset[data_key],
                        self.get_key(
                            key,
                            self.separator,
                            data_key))
            elif isinstance(dataset, list):
                for index, item in enumerate(dataset):
                    flatten(
                        item,
                        self.get_key(
                            key,
                            self.separator,
                            index))
            else:
                flattened_data[key] = dataset

        flatten(nested_data, None)

        return flattened_data


if __name__ == '__main__':
    dataset_file = open('Sample2.json', 'r')
    data = json.loads(dataset_file.read())

    flattened_data_list = [FlatTheData().get_flattened_data(d) for d in data]

    print(flattened_data_list)
