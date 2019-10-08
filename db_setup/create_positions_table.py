from config import DB_FILE
from util import create_table

def create_positions_table():
    db_file = DB_FILE
    sql_create_positions_table = """
                                 CREATE TABLE Positions (
                                 id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                 position TEXT NOT NULL,
                                 unique (position)
                                 ); """

    create_table(db_file,sql_create_positions_table)



if __name__ == '__main__':
    create_positions_table()
