'''
>>> import sqlalchemy
>>> sqlalchemy.__version__
1.1.0

When using the ORM, the configurational process starts by describing the database
tables we’ll be dealing with, and then by defining our own classes which will be
mapped to those tables. In modern SQLAlchemy, these two tasks are usually performed
 together, using a system known as Declarative, which allows us to create classes
 that include directives to describe the actual database table they will be mapped to.
http://www.sqlalchemy.org/
http://docs.sqlalchemy.org/en/rel_1_1/orm/tutorial.html
'''


from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    '''
    The User class defines a __repr__() method, but note that is optional; we only implement it in this tutorial so that our examples show nicely formatted User objects.
    '''
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name,
        self.fullname,
        self.password)

'''
>>> User.__table__
Table('users', MetaData(bind=None),
            Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
            Column('name', String(), table=<users>),
            Column('fullname', String(), table=<users>),
            Column('password', String(), table=<users>), schema=None)
'''


Base.metadata.create_all(engine)
