

from Person import Person
import urllib.request
import json
import random
import constant

class PersonWithGender(Person):
    def __init__(self):
        pass
    def get_person(self):
        gender = ["male","female"]
        self.random_person = json.loads(urllib.request.urlopen(constant.URL+'?gender='+random.choice(gender)).read())
