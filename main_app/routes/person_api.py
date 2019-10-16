from flask import request
from main_app import app
from main_app.db_models.person import *


@app.route("/api/person", methods=["GET"])
def get_all_persons():
    return persons_schema.jsonify(Person.query.all())


@app.route("/api/person/add", methods=["POST"])
def add_person():
    name = request.args.get("name")
    age = request.args.get("age")
    person = Person(name, age)

    db.session.add(person)
    db.session.commit()

    return person_schema.jsonify(person)


@app.route("/api/person/delete", methods=["DELETE"])
def delete_person():
    name = request.args.get("name")
    person = Person.query.filter_by(name=name).first()
    if person is not None:
        db.session.delete(person)
        db.session.commit()

    return person_schema.jsonify(person)
