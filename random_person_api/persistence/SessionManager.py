from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class SessionManager:
    def __init__(self):
        self.engine = create_engine("sqlite:///example.db")
        self.session = Session(self.engine, future=True)

    def get_session(self):
        return self.session
