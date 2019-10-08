from config import DB_FILE
from util import create_table

def create_cities_table():
    db_file = DB_FILE
    sql_create_cities_table = """
                              CREATE TABLE Cities (
                              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              city TEXT NOT NULL,
                              country_id INTEGER NOT NULL,
                              FOREIGN KEY (country_id) REFERENCES Countries(id),
                              unique (city)
                              ); """

    create_table(db_file,sql_create_cities_table)



if __name__ == '__main__':
    create_cities_table()
