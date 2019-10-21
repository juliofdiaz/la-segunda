from config import DB_FILE
from util import create_table


def create_stadiums_table():
    db_file = DB_FILE
    sql_create_stadiums_table = """
                              CREATE TABLE Stadiums (
                              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              name TEXT NOT NULL,
                              city_id INTEGER,
                              country_id INTEGER,
                              capacity INTEGER,
                              FOREIGN KEY (city_id) REFERENCES Cities(id),
                              FOREIGN KEY (country_id) REFERENCES Countries(id)
                              ); """

    create_table(db_file,sql_create_stadiums_table)



if __name__ == '__main__':
    create_stadiums_table()
