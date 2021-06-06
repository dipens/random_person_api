from PersonWithNationality import PersonWithNationality
from PersonWithGender import PersonWithGender
from Person import Person
from PrintOption import PrintOption
import sys

def entry_point():
    if sys.argv[1] == 'create':
        person = Person()
        person.get_person()
        random_person = person
    elif sys.argv[1] == 'create_random_nationality':
        person = PersonWithNationality()
        person.get_person()
        random_person = person
    elif sys.argv[1] == 'create_random_gender':
        person = PersonWithGender()
        person.get_person()
        random_person = person
    PrintOption.do_print(sys.argv, random_person)

entry_point()