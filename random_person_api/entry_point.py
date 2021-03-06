from persistence.DBOperations import DBOperations
from models.PersonWithNationality import PersonWithNationality
from models.PersonWithGender import PersonWithGender
from models.Person import Person
from PrintOption import PrintOption
import click
from constants.constant import constant


@click.command()
@click.option(
    "--nation",
    prompt_required=False,
    help=f"Create a person with the specified nationality. Options = {constant.get('nation')}",
    type=click.Choice(constant.get("nation"), case_sensitive=False),
)
@click.option(
    "--gender",
    prompt_required=False,
    help=f"Create a person with the specified gender. Options = {constant.get('gender')}",
    type=click.Choice(constant.get("gender"), case_sensitive=False),
)
@click.option(
    "--file",
    is_flag=False,
    flag_value=None,
    prompt_required=False,
    prompt="File name to output the file to",
    help="Create a person save it to db and output to json file.",
)
def entry_point(nation, gender, file):
    if nation is None and gender is None:
        person = Person()
        person.get_person()
        random_person = person
    elif nation is not None:
        person = PersonWithNationality()
        person.get_person(nation)
        random_person = person
    elif gender is not None:
        person = PersonWithGender()
        person.get_person(gender)
        random_person = person
    db_operations = DBOperations()
    db_operations.insert(random_person.random_person)
    PrintOption.do_print(file, random_person)


if __name__ == "__main__":
    entry_point()
