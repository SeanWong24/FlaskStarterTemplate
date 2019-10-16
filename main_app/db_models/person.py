from main_app import db, marshmallow


class Person(db.Model):
    name = db.Column(db.String(20), primary_key=True)
    age = db.Column(db.SmallInteger(), default="0", nullable=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonSchema(marshmallow.Schema):
    class Meta:
        # Fields to expose
        fields = ("name", "age")


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)
