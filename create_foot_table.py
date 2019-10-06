from config import DB_FILE
from util import create_table

def create_foot_table():
    db_file = DB_FILE
    sql_create_foot_table = """
                            CREATE TABLE Foot (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            foot TEXT  NOT NULL,
                            unique (foot)
                            ); """

    create_table(db_file, sql_create_foot_table)

if __name__ == '__main__':
    create_foot_table()
