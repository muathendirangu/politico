import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import current_app as app
from werkzeug.security import generate_password_hash
from api.utils.validator import return_error
from api.database.db_manage import create_tables, drop_data_from_tables,\
    drop_tables_if_exists

class DatabaseSetup:
    def __init__(self):
        self.dbname=os.getenv("DATABASE_POLITICO")
        self.user=os.getenv("DATABASE_USERNAME")
        self.password=os.getenv("DATABASE_PASSWORD")
        self.host=os.getenv("DATABASE_HOST")
        self.port=os.getenv("DATABASE_PORT")
        self.connection = psycopg2.connect(dbname=self.dbname,\
                user=self.user,host=self.host,\
                     password=self.password, port=self.port)
        self.cursor = self.connection.cursor()

    def drop_data_from_tables(self):
        tables = drop_data_from_tables()
        for table in tables:
            self.cursor.execute(table)
        self.connection.commit()
        self.connection.close()

    def drop_tables_if_exists(self):
        tables = drop_tables_if_exists()
        for table in tables:
            self.cursor.execute(table)
        self.connection.commit()
        self.connection.close()

    def create_all_tables(self):
        tables = create_tables()
        for table in tables:
            self.cursor.execute(table)
        self.connection.commit()
        self.connection.close()

    def create_admin_if_does_not_exist(self):
        self.cursor.execute('''SELECT * FROM users WHERE email='ndirangu@gmail.com';''')
        user=self.cursor.fetchone()
        if user is not None:
            pass
        else:
            create_admin= '''INSERT INTO users(\
                    email, password, is_admin, firstname, lastname, othername,\
                        passport_url, phone_number) VALUES \
                            ('muathe.ndirangu@gmail.com', '{}', 'True',\
                                'muathe', 'ndirangu','charles', \
                                    'https://mypassport.com','+2342343');'''.format(generate_password_hash('ndirangu'))

        self.cursor.execute(create_admin)
        self.connection.commit()
        self.cursor.close()
