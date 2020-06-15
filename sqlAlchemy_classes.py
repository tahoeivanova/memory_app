from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey, desc, and_
from mnemo_functions import cards_data_for_sql

# engine = create_engine('mysql+pymysql://u1042155_default:vjTc!DD9@localhost/u1042155_bottle_sql')
engine = create_engine('postgresql+psycopg2://progerka@localhost:5432/mnemonistka')
# engine = create_engine('postgresql://progerka@localhost:5432/mnemonistka')



Base = declarative_base()

# User
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    nickname = Column(String(50), unique=True, nullable=False)
    password = Column(LargeBinary)

    def __repr__(self):
        return f'<User.{self.nickname}>'

# Results
class NumberResults(Base):
    __tablename__ = 'number_results'
    attempt_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    win_amount = Column(Integer, default=0)
    loose_amount = Column(Integer, default=0)

    def __repr__(self):
        return f'<NumberResults.{self.user_id}, attempt: {self.attempt_id}, wins: {self.win_amount}>'

    def __str__(self):
        return f'attempts: {self.attempt_id}, wins: {self.win_amount}'

# Cards
class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False)
    value = Column(Integer)
    def __str__(self):
        return f'{self.name}'
    def __repr__(self):
        return f"{self.name}"

# Cards Results
class CardsResults(Base):
    __tablename__ = 'cards_results'
    attempt_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    win_amount = Column(Integer, default=0)
    loose_amount = Column(Integer, default=0)

    def __repr__(self):
        return f'<CardsResults.{self.user_id}, attempt: {self.attempt_id}, wins: {self.win_amount}>'
    def __str__(self):
        return f'attempts: {self.attempt_id}, wins: {self.win_amount}'

# Pi Results
class PiResults(Base):
    __tablename__ = 'pi_results'
    attempt_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    pi_signs_amount = Column(Integer, default=0)

    def __repr__(self):
        return f'<PiResults.{self.user_id}, attempt: {self.attempt_id}, pi signs: {self.pi_signs_amount}'

    def __str__(self):
        return f'You know {self.pi_signs_amount} signs after comma'



# Path
class PathName(Base):
    __tablename__ = 'path_names'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    name = Column(String(100), nullable=False, unique=True)
    path_items = relationship("PathItems", cascade="all, delete-orphan")

    def __str__(self):
        return f'{self.name}'

class PathItems(Base):
    __tablename__ = 'paths_item_names'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    path_id = Column(Integer, ForeignKey(PathName.id))
    name = Column(String, nullable=False)
    value = Column(String)

    def __str__(self):
        return f'{self.name}'



metadata = MetaData()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# add cards to the db (EXECUTED)
# cards = cards_data_for_sql()
# for card in cards:
#     card_info = Card(name=card[1], value=card[2])
#     session.add(card_info)
#     session.commit()

# UPDATE Joker's values (to 15)  (EXECUTED)
# jokers = session.query(Card).filter(Card.name.like('J%'))
# print(jokers)
# for joker in jokers:
#     joker.value = 15
#     session.commit()

# колоды карт
def cards_filter(cards_all):
    '''

    :param cards_all: 36, 52 или 54 карты
    :return: list
    '''
    if cards_all==36:
        cards = session.query(Card).filter(and_(Card.value > 5, Card.value < 15)).all()
    elif cards_all==52:
        cards = session.query(Card).filter(Card.value < 15).all()
    elif cards_all == 54:
        cards = session.query(Card).all()
    else:
        raise ValueError('В колоде может быть 36, 52 и 54 карты')
    cards_list =[]
    for card in cards:
        card = str(card)
        cards_list.append(card)

    return cards_list