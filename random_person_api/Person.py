from dataclasses import dataclass
from random_person_api.PersonSchema import PersonSchema
from typing import List
import urllib.request
import json
import constant
from sqlalchemy import Column, case
from sqlalchemy.types import (
    JSON,
    DateTime,
    Unicode,
    Integer,
    TypeDecorator,
    TypeEngine,
    Boolean,
    String,
    Numeric,
)


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
        self.name = 'AAA'
        schema = PersonSchema()
        result = schema.dump(self)
        print(result)

    def print_to_console(self):
        print(json.dumps(self.random_person, indent=4, sort_keys=True))

    def print_to_file(self, file_name):
        with open(file_name + ".json", "w") as outfile:
            json.dump(self.random_person, outfile)
