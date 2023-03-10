import datetime as dt

from sqlalchemy import create_engine, Column, Integer, VARCHAR, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class ToDo(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    task = Column(VARCHAR, default='Unemployed')
    deadline = Column(DATE, default=dt.datetime.today())

    def initialize(self):
        """
        Creates a database if it doesn't exist
        :return:
        """
        Base.metadata.create_all(engine)
        session.commit()
        return 'Database initialized!'

    def __repr__(self):
        """
        :return: string representation of the object
        :return:
        """
        return f'{self.task}'


def main():
    Base.metadata.create_all(engine)
    session.commit()


if __name__ == '__main__':
    main()
