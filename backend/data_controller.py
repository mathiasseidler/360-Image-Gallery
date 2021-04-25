import sqlite3
from sqlite3.dbapi2 import connect
import os
import hashlib
import pandas as pd

HASH_ITERATIONS = 100_000

DEFAULT_DB_PATH = '../data/database.sqlite3'

USERS_CREATE_TABLE_SQL = """
        CREATE TABLE users (
        id integer PRIMARY KEY,
        name text NOT NULL UNIQUE,
        password_hash_pbkdf2_hmac text NOT NULL,
        password_salt_pbkdf2_hmac test NOT NULL)"""

PROJECTS_CREATE_TABLE_SQL = """
        CREATE TABLE projects (
        id integer PRIMARY KEY,
        name text NOT NULL UNIQUE,
        date DATE,
        description text,
        user_id integer,
        FOREIGN KEY (user_id) REFERENCES users (id)
        )"""

IMAGES_CREATE_TABLE_SQL = """
        CREATE TABLE images (
        id integer PRIMARY KEY,
        project_id integer,
        file_name text NOT NULL,
        FOREIGN KEY (project_id) REFERENCES projects (id)
        )"""

class Image360DataController(object):
    def __init__(self) -> None:
        super().__init__()
        self._connection = self.get_data_base_connection()

    def get_data_base_connection(self, path: str = DEFAULT_DB_PATH):
        connection = sqlite3.connect(path)
        return connection


    def create_tables(self):
        cur = self._connection.cursor()
        try:
            cur.execute(USERS_CREATE_TABLE_SQL)
            cur.execute(PROJECTS_CREATE_TABLE_SQL)
            cur.execute(IMAGES_CREATE_TABLE_SQL)
        except:
            pass
        self._connection.commit()


    def create_new_user(self, user_name: str, password: str):
        salt = os.urandom(32)  # A new salt for this user
        key = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), salt, HASH_ITERATIONS)
        sql = """
            INSERT INTO users (name, password_hash_pbkdf2_hmac, password_salt_pbkdf2_hmac)
            VALUES (?, ?, ?)"""
        cursor = self._connection.cursor()
        cursor.execute(sql, (user_name, key, salt))
        self._connection.commit()
        return cursor.lastrowid


    def create_new_project(self, project_name: str, date: str, description: str, created_by_userid: int):
        sql = """
            INSERT INTO projects (name, date, description, user_id)
            VALUES (?, ?, ?, ?)"""
        cursor = self._connection.cursor()
        cursor.execute(sql, (project_name, date, description, created_by_userid))
        self._connection.commit()


    def add_image(self, project_id: int, file_name: str):
        sql = """
            INSERT INTO images (project_id, file_name)
            VALUES (?, ?, ?)"""
        cursor = self._connection.cursor()
        cursor.execute(sql, (project_id, file_name))
        self._connection.commit()


    def get_users_df(self):
        return pd.read_sql_query("SELECT * from users", self._connection)


    def get_user(self, user_name):
        cur = self._connection.cursor()
        cur.execute("SELECT * FROM users WHERE name=(?)", (user_name,))
        self._connection.commit()
        return cur.fetchall()


    def get_project_by_userid(self, user_id: int):
        cur = self._connection.cursor()
        cur.execute("SELECT * FROM projects WHERE user_id=(?)", (user_id,))
        self._connection.commit()
        return cur.fetchall()


    def get_projects_df(self):
        return pd.read_sql_query("SELECT * FROM projects", self._connection)

    def get_images(self, project_id: int):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM images WHERE project_id=(?)", project_id)
        return cursor.fetchall()

if __name__ == "__main__":
    data_ctrl = Image360DataController()
    connection = data_ctrl.create_tables()
    # cursor = connection.cursor()
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    # print(cursor.fetchall())

    data_ctrl.create_new_user('zhenru', 'labrat')
    data_ctrl.create_new_project('Sukabumi', '2019-01-03', 'test', 1)

    users_df = data_ctrl.get_users_df()
    user = users_df[users_df.name == 'zhenru']
    key = hashlib.pbkdf2_hmac(
        'sha256', 'labrat'.encode('utf-8'), user.password_salt_pbkdf2_hmac.item(), HASH_ITERATIONS)
    if key == user.password_hash_pbkdf2_hmac.item():
        print('correct password')
    else:
        print('wrong password')
    
    print(data_ctrl.get_projects_df())
    print(data_ctrl.get_project_by_userid(1))
