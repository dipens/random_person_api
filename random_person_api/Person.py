from dataclasses import dataclass
from typing import List
import urllib.request
import json
import constant

@dataclass
class Person:
    def __init__(self):
        pass
    def get_person(self):
        self.random_person = json.loads(urllib.request.urlopen(constant.URL).read())
    def print_to_console(self):
        print(json.dumps(self.random_person, indent=4, sort_keys=True))
    def print_to_file(self, file_name):
        print('BBB')
        with open(file_name+'.json', 'w') as outfile:
            json.dump(self.random_person, outfile)
