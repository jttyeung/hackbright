"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Brand(db.Model):
    """Car brand."""

    __tablename__ = "brands"

    brand_id = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    founded = db.Column(db.Integer, nullable=True)
    headquarters = db.Column(db.String(50), nullable=True)
    discontinued = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        """Shows info about the brand"""

        return "<Brand id=%s name=%s>" % (self.brand_id, self.name)


class Model(db.Model):
    """Car model."""

    __tablename__ = "models"

    model_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    brand_id = db.Column(db.String(5), db.ForeignKey(Brand.brand_id), nullable=False)
    name = db.Column(db.String(50), nullable=False)

    brand = db.relationship('Brand', backref='model')

    def __repr__(self):
        """Shows info about the model"""

        return "<Model id=%s name=%s year=%s>" % (self.model_id, self.name, self.year)


# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
