from flask import Flask, jsonify, request
from flask import make_response
#from flask_marshmallow import Marshmallow

from persistence.DBOperations import DBOperations
from schemas.PersonSchema import PersonSchema
from models.Person import Person
import json
import pprint



app = Flask(__name__)
app.config['DEBUG'] = True
#ma = Marshmallow(app) 
#app.config



# Create a Person
@app.route("/person", methods=["GET"])
def add_product():
    person = Person()
    person.get_person()
    random_person = person
    db_operations = DBOperations()
    id = db_operations.insert(random_person.random_person)
    result = db_operations.print_by_id(id)
    #pprint.pprint(result)
    person_schema = PersonSchema()
    mm = person_schema.dump(result)
    pprint.pprint(mm)
    r = make_response(mm)
    r.mimetype = "application/json"
    return r


@app.route("/persons")
def get_persons():
    db_operations = DBOperations()
    r = make_response(db_operations.print_all())
    r.mimetype = "application/json"
    return r

# Get a Person
@app.route("/person/<id>", methods=["GET"])
def get_person(id):
    db_operations = DBOperations()
    result = db_operations.print_by_id(id)
    r = make_response(result)
    r.mimetype = "application/json"
    return r

# Delete a Person
@app.route("/person/<id>", methods=["DELETE"])
def delete_person(id):
    db_operations = DBOperations()
    result = db_operations.delete_by_id(id)
    r = make_response({"msg": "Person deleted"})
    r.mimetype = "application/json"
    return r

if __name__ == "__main__":
    app.run()
