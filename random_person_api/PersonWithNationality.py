from Person import Person
import urllib.request
import json
import random
import constant
from PersonSchema import PersonSchema
from DBOperations import DBOperations


class PersonWithNationality(Person):
    def __init__(self):
        pass

    def get_person(self, nation):
        self.random_person = json.loads(
            urllib.request.urlopen(constant.URL + "?nat=" + nation).read()
        )
