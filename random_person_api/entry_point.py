from person_with_nationality import person_with_nationality
from person_with_gender import person_with_gender
from person import person
from print_option import print_option
import sys

def entry_point():
    if sys.argv[1] == 'create':
        random_person = person()
    elif sys.argv[1] == 'create_random_nationality':
        random_person = person_with_nationality()
    elif sys.argv[1] == 'create_random_gender':
        random_person = person_with_gender()
    print_option.do_print(sys.argv, random_person)

entry_point()