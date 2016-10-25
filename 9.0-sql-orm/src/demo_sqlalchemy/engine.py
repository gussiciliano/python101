'''
Created on Jul 28, 2016

@author: zehemz
'''

import sqlalchemy

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


if __name__ == '__main__':
    ## version
    print('Version:' + str(sqlalchemy.__version__))
    ##engine, inmemory
    engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
    
    
    metadata = MetaData()
    users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String))
    
    addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String, nullable=False))