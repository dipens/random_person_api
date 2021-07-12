from persistence.DBOperations import DBOperations
from flask import Flask


app = Flask(__name__)

@app.route("/get")
def hello_world():
    db_operations = DBOperations()
    return db_operations.print_all()


if __name__ == "__main__":
    app.run()