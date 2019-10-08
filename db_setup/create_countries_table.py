from config import DB_FILE
from util import create_table

def create_countries_table():
    db_file = DB_FILE
    sql_create_countries_table = """
                                 CREATE TABLE Countries (
                                 id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                 country TEXT NOT NULL,
                                 unique (country)
                                 ); """

    create_table(db_file,sql_create_countries_table)



if __name__ == '__main__':
    create_countries_table()
