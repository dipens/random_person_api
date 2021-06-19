from Person import Person
import urllib.request
import json
import random
import constant
from PersonSchema import PersonSchema
import pprint

class PersonWithNationality(Person):
    def __init__(self):
        pass

    def get_person(self, nation):
        self.random_person = json.loads(
            urllib.request.urlopen(constant.URL + "?nat=" + nation).read()
        )
        for key in self.random_person['results'][0]:
            setattr(self, key, self.random_person['results'][0][key])
        schema = PersonSchema()
        result = schema.dump(self)
