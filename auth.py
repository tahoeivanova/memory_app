from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, desc

engine = create_engine('postgresql://progerka@localhost:5432/mnemonistka')
# engine = create_engine('mysql://u1042155_default:vjTc!DD9@localhost/u1042155_bottle_sql')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    nickname = Column(String(50), unique=True, nullable=False)
    password = Column(String(80))

    def __repr__(self):
        return f'<User.{self.nickname}>'

# класс digit_results

class DigitResults(Base):
    __tablename__ = 'number_memory_results'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    win_amount = Column(Integer, default=0)
    loose_amount = Column(Integer, default=0)

    def __repr__(self):
        return f'<DigitResults.{self.user_id}, attempt: {self.id}, wins: {self.win_amount}>'


metadata = MetaData()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
