import sys
from random_person_api import random_person_api

if len(sys.argv) > 2:
    random_person_api(sys.argv[1], sys.argv[2])
else:
    random_person_api(sys.argv[1])