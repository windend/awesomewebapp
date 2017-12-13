from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()


class Users(base):
    __tablename__ = 'Users'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


engine = create_engine(
    'mysql+mysqlconnector://root:123456@localhost:3306/awesome')

DBsession = sessionmaker(bind=engine)


session = DBsession()

Users = session.query(Users).filter(Users.id == '5').one()

print('type:', type(Users))
print('name:', Users.first_name)

session.close()
