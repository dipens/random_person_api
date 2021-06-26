from SessionManager import SessionManager
from PersonSchema import PersonSchema
from sqlalchemy import *
import pprint


class DBOperations:
    def __init__(self):
        self.session = SessionManager().getSession()
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
        for key in random_person["results"][0]:
            setattr(self, key, random_person["results"][0][key])
        schema = PersonSchema()
        result = schema.dump(self)
        stmt = self.person_table.insert().values(result)
        result = self.session.execute(stmt)
        self.session.commit()

    def print(self):
        result = self.session.execute(select(self.person_table))
        for row in result:
            pprint.pprint(row)
