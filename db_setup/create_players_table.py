from config import DB_FILE
from util import create_table

def create_players_table():
    db_file = DB_FILE
    sql_create_players_table = """
                               CREATE TABLE Players (
                               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                               first_name TEXT NOT NULL,
                               last_name TEXT NOT NULL,
                               name_ob TEXT,
                               city_id TEXT,
                               citizenship TEXT,
                               date_ob TEXT,
                               foot_id TEXT,
                               height INTEGER,
                               position_id TEXT,
                               link TEXT,
                               FOREIGN KEY (city_id) REFERENCES Cities(id),
                               FOREIGN KEY (foot_id) REFERENCES Foot(id),
                               FOREIGN KEY (position_id) REFERENCES Positions(id)
                               ); """

    create_table(db_file,sql_create_players_table)



if __name__ == '__main__':
    create_players_table()
