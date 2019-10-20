from config import DB_FILE
from util import create_table


def create_transfers_table():
    db_file = DB_FILE
    sql_create_transfers_table = """
                              CREATE TABLE Transfers (
                              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              season TEXT,
                              out_club TEXT NOT NULL,
                              in_club TEXT NOT NULL,
                              date TEXT,
                              FOREIGN KEY (player_id) REFERENCES Players(id),
                              FOREIGN KEY (out_club) REFERENCES Clubs(id),
                              FOREIGN KEY (in_club) REFERENCES Clubs(id)
                              ); """

    create_table(db_file,sql_create_transfers_table)



if __name__ == '__main__':
    create_transfers_table()
