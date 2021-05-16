

from person import person
import urllib.request
import json
import random
import constant

class person_with_nationality(person):
    def __init__(self):
        nationality = ["AU", "BR", "CA", "CH", "DE", "DK", "ES", "FI", "FR", "GB", "IE", "IR", "NO", "NL", "NZ", "TR", "US"]
        self.random_person = json.loads(urllib.request.urlopen(constant.URL+'?nat='+random.choice(nationality)).read())
