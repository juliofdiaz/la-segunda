import sqlite3
from sqlite3 import Error
from util import select_from_table 
 
 
 
def select_from_foot():
    db_file = r"liga2.db"
    sql = "SELECT * FROM Foot"
    selected = select_from_table(db_file, sql)
    selected.columns = ["id","foot"] 
    return selected
 
if __name__ == '__main__':
    rows = select_from_foot()

    sset = rows.loc[rows['foot'] == "right"]
    print(sset)
