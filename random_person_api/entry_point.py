from PersonWithNationality import PersonWithNationality
from PersonWithGender import PersonWithGender
from Person import Person
from PrintOption import PrintOption
import click
import constant


@click.command()
@click.option(
    "--nation",
    prompt_required=False,
    help="Create a person with the specified nationality. Options = AU,BR,CA,CH,DE,DK,ES,FI,FR,GB,IE,IR,NO,NL,NZ,TR,US",
    type=click.Choice(constant.nation, case_sensitive=False),
)
@click.option(
    "--gender",
    prompt_required=False,
    help="Create a person with the specified gender. Options=male,female",
    type=click.Choice(constant.gender, case_sensitive=False),
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
    PrintOption.do_print(file, random_person)


if __name__ == "__main__":
    entry_point()
