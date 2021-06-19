from Person import Person
import urllib.request
import json
import random
import constant

class PersonWithNationality(Person):
    def __init__(self):
        pass

    def get_person(self, nation):
        self.random_person = json.loads(
            urllib.request.urlopen(constant.URL + "?nat=" + nation).read()
        )
        print(self.random_person['results'][0])
