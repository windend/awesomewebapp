# from sqlalchemy import Column, String, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base


# base = declarative_base()


# class actor(base):
#     __tablename__ = 'actor'
#     actor_id = Column(String(20), primary_key=True)
#     first_name = Column(String(20))


# engine = create_engine(
#     'mysql+mysqlconnector://root:123456@localhost:3306/sakila')

# DBsession = sessionmaker(bind=engine)


# session = DBsession()

# actor = session.query(actor).filter(actor.actor_id == '5').one()

# print('type:', type(actor))
# print('name:', actor.first_name)

# session.close()

def countdown(n):
    print("countdown:", n)
    while n >= 0:
        news = (yield n)
        print("n:", n)
        print("news:", news)
        if news is not None:
            n = news
        else:
            n -= 1
c = countdown(5)
for x in c:
    print("x:", x)
    if x == 5:
        c.send(3)
        c.send(2)
