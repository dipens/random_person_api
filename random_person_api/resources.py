from persistence.DBOperations import DBOperations
from flask import Flask
from flask import make_response


app = Flask(__name__)


@app.route("/get")
def hello_world():
    db_operations = DBOperations()
    r = make_response(db_operations.print_all())
    r.mimetype = "application/json"
    return r


if __name__ == "__main__":
    app.run()
