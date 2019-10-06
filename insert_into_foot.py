from config import DB_FILE
from config import START_FOOT
from util import insert_into_table
from util import check_insert_into_table


def insert_into_foot(value):
	'''
	Insert one row in foot table
	:param value: value to be inserted in foot table
	'''

	db_file = DB_FILE
	sql = "INSERT INTO Foot(foot) VALUES(?)"

	return insert_into_table(db_file, sql, value)


def check_insert_into_foot(value):
	'''
	Insert one row if it doest exist otherwise return respective row id
	:param value: value to be inserted
	:return: the id of the row that was inserted or the id of the row
	just inserted
	'''

	db_file = DB_FILE
	sql_select = "SELECT * FROM Foot WHERE foot = ?"
	sql_insert = "INSERT INTO Foot(foot) VALUES(?)"

	return check_insert_into_table(db_file,sql_select, sql_insert, (value,))

def initial_foot_table_insert():
	'''
	Insert initial rows.
	'''

	initial_dataset = START_FOOT

	for item in initial_dataset:
		num = insert_into_foot(item)
		print("[Recorded] id:"+str(num)+"\tfoot:"+item+" INTO Foot TABLE")

if __name__ == '__main__':
	initial_foot_table_insert()
