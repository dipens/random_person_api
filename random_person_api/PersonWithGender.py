from Person import Person
import urllib.request
import json
import constant
from PersonSchema import PersonSchema
from DBOperations import DBOperations
from sqlalchemy import *


class PersonWithGender(Person):
    def __init__(self):
        pass

    def get_person(self, gender):
        self.random_person = json.loads(
            urllib.request.urlopen(constant.URL + "?gender=" + gender).read()
        )
