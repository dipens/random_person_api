from dataclasses import dataclass
from Person import Person
from typing import List

@dataclass
class PrintOption:
    args: List[str]
    def doPrint(self, Person):
        if (len(self.args) > 2) and self.args[1] == 'json':
            Person.printToFile(self.args[2])
        elif self.args[1] == 'create':
            Person.printToConsole()
        else:
            print("ERR: Please specify the correct arguments")