from models.Person import Person
import urllib.request
import json
from constants.constant import constant
from schemas.PersonSchema import PersonSchema
from persistence.DBOperations import DBOperations
from sqlalchemy import *


class PersonWithGender(Person):
    def __init__(self):
        pass

    def get_person(self, gender):
        self.random_person = json.loads(
            urllib.request.urlopen(constant.get("URL") + "?gender=" + gender).read()
        )
