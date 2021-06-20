from dataclasses import dataclass
from PersonSchema import PersonSchema
from typing import List
import urllib.request
import json
import constant
from sqlalchemy import Column, case
from sqlalchemy.types import (
    JSON,
    Unicode,
    Integer,
)
from DBOperations import DBOperations


@dataclass
class Person:
    __tablename__ = "person"
    PK = Column(Integer, primary_key=True)
    name = Column(JSON)
    nat = Column(Unicode(2))
    gender = Column(Unicode(10))
    registered = Column(JSON)
    picture = Column(JSON)
    phone = Column(Unicode(25))
    cell = Column(Unicode(25))
    login = Column(JSON)
    location = Column(JSON)
    id = Column(JSON)
    email = Column(Unicode(100))
    dob = Column(JSON)

    def __init__(self):
        pass

    def get_person(self):
        self.random_person = json.loads(urllib.request.urlopen(constant.URL).read())

    def print_from_db(self):
        db_operations = DBOperations()
        db_operations.print()

    def print_to_file(self, file_name):
        with open(file_name + ".json", "w") as outfile:
            json.dump(self.random_person, outfile)

    def insert_to_db(self):
        for key in self.random_person["results"][0]:
            setattr(self, key, self.random_person["results"][0][key])
        schema = PersonSchema()
        result = schema.dump(self)
        db_operations = DBOperations()
        db_operations.insert(result)
