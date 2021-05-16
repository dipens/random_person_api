

from person import person
import urllib.request
import json
import random
import constant

class person_with_gender(person):
    def __init__(self):
        gender = ["male","female"]
        self.random_person = json.loads(urllib.request.urlopen(constant.URL+'?gender='+random.choice(gender)).read())
