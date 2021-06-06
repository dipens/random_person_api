from dataclasses import dataclass
#from Person import Person
from typing import List

@dataclass
class PrintOption:
    args: List[str]
    @staticmethod
    def do_print(args, person):
        print(len(args))
        if (len(args) > 2):
            person.print_to_file(args[2])
        else:
            person.print_to_console()