from dataclasses import dataclass
#from Person import Person
from typing import List

@dataclass
class print_option:
    args: List[str]
    @staticmethod
    def do_print(args, person):
        if (len(args) > 2) and args[1] == 'json':
            person.print_to_file(args[2])
        else:
            person.print_to_console()