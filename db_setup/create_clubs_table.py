from config import DB_FILE
from util import create_table


def create_clubs_table():
    db_file = DB_FILE
    sql_create_clubs_table = """
                              CREATE TABLE Clubs (
                              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              name TEXT NOT NULL,
                              full_name TEXT,
                              dob TEXT,
                              city_id INTEGER,
                              country_id INTEGER,
                              stadium_id INTEGER,
                              FOREIGN KEY (city_id) REFERENCES Cities(id),
                              FOREIGN KEY (country_id) REFERENCES Countries(id),
                              FOREIGN KEY (stadium_id) REFERENCES Stadiums(id)
                              ); """

    create_table(db_file,sql_create_clubs_table)



if __name__ == '__main__':
    create_clubs_table()
