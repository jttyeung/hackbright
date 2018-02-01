"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?
# A query object


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?
# An association table manages one to one tables. Its purpose is to separate two
# ideas into separate tables, but provide the link between them without having
# any useful extra data besides the foreign keys to each of the tables. These
# types of tables are skipped and never used directly when querying.



# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = db.session.query(Brand.name).filter(Brand.brand_id=='ram').one()
# db.session.query(Brand).get('ram').name

# Get all models with the name "Corvette" and the brand_id "che."
q2 = db.session.query(Model.name).filter(Brand.brand_id=='che').all()
# db.session.query(Model).filter((Brand.brand_id=='che') & (Model.name=='Corvette')).distinct().all()

# Get all models that are older than 1960.
q3 = db.session.query(Model.name).filter(Model.year<1960).all()

# Get all brands that were founded after 1920.
q4 = db.session.query(Brand.name).filter(Model.year>1920).distinct().all()

# Get all models with names that begin with "Cor."
q5 = db.session.query(Model.name).filter(Model.name.like('Cor%')).distinct().all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = db.session.query(Brand.name).filter( (Brand.founded==1903) & (Brand.discontinued is None) ).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = db.session.query(Brand.name).filter( (Brand.founded<1950) | (Brand.discontinued is not None) ).all()

# Get any model whose brand_id is not "for."
q8 = db.session.query(Model.name).filter(Brand.brand_id != 'for').distinct().all()




# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""
    cars = Model.query.filter(Model.year==year).all()

    for car in cars:
        print 'Model: %s\tBrand: %s\tHeadquarters: %s' % (car.name, car.brand.name, car.brand.headquarters)


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    cars = Model.query.options(db.joinedload('brand')).all()

    for car in cars:
        print 'Brand: %s\tModel: %s\tYear: %s' % (car.brand.name, car.name, car.year)


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    # brands = Brand.query.filter(Brand.name.like('%mystr%')).all()
    mystr = '%' + mystr + '%'
    brands = Brand.query.filter(Brand.name.like(mystr)).all()

    for brand in brands:
        print brand


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    models = Model.query.filter( (Model.year >= start_year) & (Model.year <= end_year) ).all()

    for model in models:
        print model

