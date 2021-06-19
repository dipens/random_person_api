from Person import Person
import urllib.request
import json
import random
import constant
from PersonSchema import PersonSchema


class PersonWithGender(Person):
    def __init__(self):
        pass

    def get_person(self, gender):
        self.random_person = json.loads(
            urllib.request.urlopen(constant.URL + "?gender=" + gender).read()
        )
        for key in self.random_person['results'][0]:
            setattr(self, key, self.random_person['results'][0][key])
        schema = PersonSchema()
        result = schema.dump(self)
