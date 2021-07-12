import persistence.DBOperations
from flask import Flask


app = Flask(__name__)

@app.route("/get")
def hello_world():
    db_operations = persistence.DBOperations()