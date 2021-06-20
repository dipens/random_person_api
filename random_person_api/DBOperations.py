from PersonSchema import PersonSchema
from sqlalchemy import *
import pprint


class DBOperations:
    def __init__(self):
        self.engine = create_engine("sqlite:///example.db")
        self.metadata = MetaData()
        self.person_table = Table(
            "person",
            self.metadata,
            Column("PK", Integer, primary_key=True),
            Column("name", JSON),
            Column("nat", String(2)),
            Column("gender", String(10)),
            Column("gender", JSON),
            Column("registered", JSON),
            Column("picture", String(50)),
            Column("cell", String(25)),
            Column("phone", String(25)),
            Column("login", JSON),
            Column("location", JSON),
            Column("id", JSON),
            Column("email", String(100)),
            Column("dob", JSON),
        )
        pass

    def insert(self, random_person):
        print(random_person)
        for key in random_person["results"][0]:
            setattr(self, key, random_person["results"][0][key])
        schema = PersonSchema()
        result = schema.dump(self)
        self.metadata.create_all(self.engine)
        stmt = self.person_table.insert().values(result)
        self.engine.execute(stmt)

    def print(self):
        result = self.engine.execute(select(self.person_table))
        for row in result:
            pprint.pprint(row)
