from dataclasses import dataclass
from typing import List
import sqlite3


@dataclass
class PrintOption:
    args: List[str]

    @staticmethod
    def do_print(file, person):
        if file is not None:
            person.print_to_file(file)
        else:
            person.print_to_console()
