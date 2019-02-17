""" manage database set up """
import os
import psycopg2
from psycopg2.extras import DictCursor
from api.utils.validator import return_error

def create_tables():
    """create data tables for the api."""
    # create users query definition
    users = """
        CREATE TABLE users(
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(128) NULL,
            lastname VARCHAR(128) NULL,
            othername VARCHAR(128) NULL,
            email VARCHAR(128) NOT NULL,
            phone_number VARCHAR(150)  NULL,
            passport_url VARCHAR(256)  NULL,
            password VARCHAR(256) NOT NULL,
            is_admin  boolean NOT NULL DEFAULT TRUE
        );"""

    #create parties sql query definition
    # parties = """
    #     CREATE TABLE parties(
    #         id SERIAL PRIMARY KEY,
    #         name VARCHAR(100) NOT NULL,
    #         hq_address VARCHAR(200) NOT NULL,
    #         logo_url VARCHAR(256) NOT NULL
    #     );"""

    # #create offices sql query definition
    # offices = """
    #     CREATE TABLE offices(
    #         id SERIAL PRIMARY KEY,
    #         name VARCHAR(100) NOT NULL,
    #         office_type VARCHAR(100) NOT NULL
    #     );"""

    # # create candidates sql query definition
    # candidates = """
    #     CREATE TABLE candidates(
    #         id SERIAL PRIMARY KEY,
    #         office_id INTEGER,
    #         party_id INTEGER,
    #         candidate_id INTEGER,
    #         FOREIGN KEY(office_id) REFERENCES offices(id) ON DELETE CASCADE,
    #         FOREIGN KEY(party_id) REFERENCES parties(id) ON DELETE CASCADE,
    #         FOREIGN KEY(candidate_id) REFERENCES users(id) ON DELETE CASCADE
    #     );"""

    # # create petitions sql query definition
    # petitions = """
    #     CREATE TABLE petitions(
    #         id SERIAL PRIMARY KEY,
    #         created_on TIMESTAMP NOT NULL DEFAULT now(),
    #         created_by INTEGER,
    #         office_id INTEGER,
    #         petition_description TEXT NOT NULL,
    #         FOREIGN KEY(created_by) REFERENCES users(id) ON DELETE CASCADE,
    #         FOREIGN KEY(office_id) REFERENCES offices(id) ON DELETE CASCADE
    #     );"""

    # # create votes sql query definition
    # votes = """
    #     CREATE TABLE votes(
    #         id SERIAL PRIMARY KEY,
    #         created_on TIMESTAMP NOT NULL DEFAULT now(),
    #         created_by INTEGER,
    #         office_id INTEGER,
    #         candidate_id INTEGER,
    #         FOREIGN KEY(created_by) REFERENCES users(id) ON DELETE CASCADE,
    #         FOREIGN KEY(office_id) REFERENCES offices(id) ON DELETE CASCADE,
    #         FOREIGN KEY(candidate_id) REFERENCES users(id) ON DELETE CASCADE
    #     );"""

    return [users]



#to be used during testing database operations
def drop_data_from_tables():
    delete_user_data = '''DELETE FROM users;'''
    delete_parties_data = '''DELETE FROM parties;'''
    delete_offices_data = '''DELETE FROM offices;'''
    delete_candidates_data = '''DELETE FROM candidates;'''
    delete_petitions_data = '''DELETE FROM petitions;'''
    delete_votes_data = '''DELETE FROM votes;'''

    return [delete_user_data, delete_parties_data,delete_offices_data,\
         delete_candidates_data, delete_candidates_data,\
              delete_petitions_data, delete_votes_data]


def drop_tables_if_exists():
    # drop existing tables if there are any
    users = '''DROP TABLE IF EXISTS users CASCADE;'''
    return [users]