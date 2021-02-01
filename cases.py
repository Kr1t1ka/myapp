import datetime as DT
import random
import string
from sqlalchemy import or_, and_

from db import User


class Cases:

    def __init__(self, db):
        self.db = db

    def create_db(self):
        self.db.create_all()

    def create_user(self, params):
        try:
            date = DT.datetime.strptime(params[3], '%d.%m.%Y').date()
        except Exception as e:
            print(f'DATA_ERROR:{e}')
        user = User(fio=params[2], date=date, gender=params[4])
        try:
            self.db.session.add(user)
            self.db.session.commit()
        except Exception as e:
            print(f'An error occurred while adding a record: {e}')

    def print_user(self):
        user = User.query.order_by(User.fio).all()
        for i in user:
            years = DT.datetime.now() - DT.datetime.strptime(str(i.date), "%Y-%m-%d")
            print(f'{i.fio} {int(int(years.days) / 365)} years')

    def random_name(self, len, letter=None):
        letters = string.ascii_lowercase
        if letter is None:
            rand_string = ''.join(random.choice(letters) for i in range(len))
        else:
            rand_string = letter + ''.join(random.choice(letters) for i in range(len))
        return rand_string

    def random_gender(self):
        sex = random.randrange(0, 9)
        if sex > 5:
            return 'men'
        else:
            return 'woman'

    def random_date(self):
        return DT.date(random.randrange(1920, 2020),
                       random.randrange(1, 12),
                       random.randrange(1, 28))

    def insert_user(self):
        for i in range(100000):
            user = User(fio=self.random_name(10), date=self.random_date(), gender=self.random_gender())
            try:
                self.db.session.add(user)
                self.db.session.commit()
            except Exception as e:
                print(f'An error occurred while adding a record: {e}')

        for i in range(100):
            user = User(fio=self.random_name(10, 'F'), date=self.random_date(), gender='men')
            try:
                self.db.session.add(user)
                self.db.session.commit()
            except Exception as e:
                print(f'An error occurred while adding a record: {e}')

    def print_f_user(self):
        time = DT.datetime.now()
        user = User.query.filter(User.gender == 'men').all()
        for i in user:
            if i.fio[0] == 'F':
                print(f'NAME:{i.fio} GENDER:{i.gender}')
        print(f'lead time:{DT.datetime.now()-time}')

