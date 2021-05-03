from dataclasses import dataclass
from typing import List
import urllib.request
import json
import constant

@dataclass
class Person:
    def __init__(self):
        self.random_person = json.loads(urllib.request.urlopen(constant.URL).read())
    def printToConsole(self):
        print(json.dumps(self.random_person, indent=4, sort_keys=True))
    def printToFile(self, fileName):
        with open(fileName+'.json', 'w') as outfile:
            json.dump(self.random_person, outfile)
