from config import DB_FILE
from config import START_POSITIONS
from util import insert_into_table
from util import check_insert_into_table


def insert_into_positions(value):
	'''
	Insert one row in foot table
	:param value: value to be inserted in foot table
	'''

	db_file = DB_FILE
	sql = "INSERT INTO Positions(position, area) VALUES(?, ?)"

	return insert_into_table(db_file, sql, value)


def check_insert_into_positions(value):
	'''
	Insert one row if it doest exist otherwise return respective row id
	:param value: value to be inserted
	:return: the id of the row that was inserted or the id of the row
	just inserted
	'''

	db_file = DB_FILE
	sql_select = "SELECT * FROM Positions WHERE position = ?"
	sql_insert = "INSERT INTO Positions(position, area) VALUES(?, ?)"

	return check_insert_into_table(db_file,sql_select, sql_insert, value)

def initial_foot_table_insert():
	'''
	Insert initial rows.
	'''

	initial_dataset = START_POSITIONS

	for item in initial_dataset:
		num = insert_into_positions(item)
		#print("[Recorded] id:"+str(num)+"\tposition:"+item+" INTO Positions TABLE")

if __name__ == '__main__':
	initial_foot_table_insert()
