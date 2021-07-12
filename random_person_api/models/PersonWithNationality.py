from models.Person import Person
import urllib.request
import json
from constants.constant import constant


class PersonWithNationality(Person):
    def __init__(self):
        pass

    def get_person(self, nation):
        self.random_person = json.loads(
            urllib.request.urlopen(constant.get("URL") + "?nat=" + nation).read()
        )
