from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()


class actor(base):
    __tablename__ = 'actor'
    actor_id = Column(String(20), primary_key=True)
    first_name = Column(String(20))


engine = create_engine(
    'mysql+mysqlconnector://root:123456@localhost:3306/sakila')

DBsession = sessionmaker(bind=engine)


session = DBsession()

actor = session.query(actor).filter(actor.actor_id == '5').one()

print('type:', type(actor))
print('name:', actor.first_name)

session.close()
