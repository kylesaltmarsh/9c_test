import yaml
import sys
from math import floor

# class to import test yaml files and calculate the test scores

# sample yaml file:

# weight: 88
# max_finger_strength: 35
# max_pull_up: 60
# max_core: l_sit_20
# max_bar_hang_mapping: 90

class Test9C:
    def __init__(self, test_yaml):
        self.test_yaml = test_yaml
        self.test_scores = {}

        self.max_finger_and_pull_strength_mapping = {
            "100": 1,
            "110": 2,
            "120": 3,
            "130": 4,
            "140": 5,
            "150": 6,
            "160": 7,
            "170": 7.5,
            "180": 8,
            "190": 8.5,
            "200": 9,
            "210": 9.5,
            "220": 10
        }

        self.max_core_strength_mapping = {
            "l_sit_bn_10": 1,
            "l_sit_bn_20": 2,
            "l_sit_bn_30": 3,
            "l_sit_10": 4,
            "l_sit_20": 5,
            "l_sit_30": 6,
            "front_lever_5": 7,
            "front_lever_7.5": 7.5,
            "front_lever_10": 8,
            "front_lever_15": 8.5,
            "front_lever_20": 9,
            "front_lever_25": 9.5,
            "front_lever_30": 10
        }

        self.max_bar_hang_mapping = {
            "30": 1,
            "60": 2,
            "90": 3,
            "120": 4,
            "150": 5,
            "180": 6,
            "210": 7,
            "240": 8,
            "270": 8.5,
            "300": 9,
            "330": 9.5,
            "360": 10
        }
        
        self.total_score_mapping= {
            "40": "9c",
            "39": "9b+",
            "38": "9b",
            "37": "9b",
            "36": "9a+",
            "35": "9a+",
            "34": "9a",
            "33": "9a",
            "32": "8c+",
            "31": "8c+",
            "30": "8c",
            "29": "8c",
            "28": "8b+",
            "27": "8b+",
            "26": "8b",
            "25": "8b",
            "24": "8a+",
            "23": "8a+",
            "22": "8a",
            "21": "8a",
            "20": "7c+",
            "19": "7c+",
            "18": "7c",
            "17": "7c",
            "16": "7b+",
            "15": "7b+",
            "14": "7b",
            "13": "7b",
            "12": "7a+",
            "11": "7a+",
            "10": "7a",
            "9": "7a",
            "8": "6c+",
            "7": "6c+",
            "6": "6c",
            "5": "6c",
            "4": "6b+",
            "3": "6b",
            "2": "6a+",
            "1": "6a"
            }

        self.aus_grade_mapping= {
            "9c": 39,
            "9b+": 38,
            "9b": 37,
            "9a+": 36,
            "9a": 35,
            "8c+": 34,
            "8c": 33,
            "8b+": 32,
            "8b": 31,
            "8a+": 30,
            "8a": 29,
            "7c+": 28,
            "7c": 27,
            "7b+": 26,
            "7b": 25,
            "7a+": 24,
            "7a": 23,
            "6c+": 22,
            "6c": 21,
            "6b+": 21,
            "6b": 20,
            "6a+": 19,
            "6a": 19
            }

    def load_test_yaml(self):
        with open(self.test_yaml, 'r') as stream:
            try:
                self.test_yaml = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                sys.exit(1)

    def calculate_test_scores(self):
        self.test_scores['max_finger_strength'] = 100*(1 + self.test_yaml['max_finger_strength']/self.test_yaml['weight'])
        self.test_scores['max_finger_strength_score'] = self.max_finger_and_pull_strength_mapping[str(int(floor(self.test_scores['max_finger_strength'] * (10 ** -1)) / (10 ** -1)))]

        self.test_scores['max_pull_up'] = 100*(1 + self.test_yaml['max_pull_up']/self.test_yaml['weight'])
        self.test_scores['max_pull_up_score'] = self.max_finger_and_pull_strength_mapping[str(int(floor(self.test_scores['max_pull_up'] * (10 ** -1)) / (10 ** -1)))]

        self.test_scores['max_bar_hang'] = self.test_yaml['max_bar_hang']
        self.test_scores['max_bar_hang_score'] = self.max_bar_hang_mapping[str(int(30 * floor(self.test_scores['max_bar_hang'] / 30)))]

        self.test_scores['max_core'] = self.test_yaml['max_core']
        self.test_scores['max_core_score'] = self.max_core_strength_mapping[self.test_scores['max_core']]

        self.test_scores['total'] = self.test_scores['max_finger_strength_score'] + self.test_scores['max_pull_up_score'] + self.test_scores['max_bar_hang_score'] + self.test_scores['max_core_score']
        self.test_scores['total_score'] = self.total_score_mapping[str(floor(self.test_scores['total']))]
        self.test_scores['total_score_aus'] = self.aus_grade_mapping[self.test_scores['total_score']]

    def save_test_scores(self):
        with open('results/14_12_22.yaml', 'w') as outfile:
            yaml.dump(self.test_scores, outfile, default_flow_style=False)

    def print_test_scores(self):
        print(self.test_scores['total'])
        print(self.test_scores['total_score'])


if __name__ == "__main__":
    test9c = Test9C('data/14_12_22.yaml')
    test9c.load_test_yaml()
    test9c.calculate_test_scores()
    test9c.save_test_scores()
    test9c.print_test_scores()