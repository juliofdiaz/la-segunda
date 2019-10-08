from config import DB_FILE
from config import INITIAL_CITIES
from util import insert_into_table
from util import check_insert_into_table
from .insert_into_countries import check_insert_into_countries


def insert_into_cities(value):
	'''
	Insert one row in Cities table
	:param value: value to be inserted in Cities table
	'''

	db_file = DB_FILE
	sql = "INSERT INTO Cities(city, country_id) VALUES(?, ?)"

	return insert_into_table(db_file, sql, value)


def check_insert_into_cities(value):
	'''
	Insert one row if it doest exist otherwise return respective row id
	:param value: value to be inserted
	:return: the id of the row that was inserted or the id of the row
	just inserted
    '''
	city, country = value
	country_id = check_insert_into_countries(country)

	db_file = DB_FILE
	sql_select = "SELECT * FROM Cities WHERE city = ? AND country_id = ?"
	sql_insert = "INSERT INTO Cities(city, country_id) VALUES(?, ?)"

	return check_insert_into_table(db_file,sql_select, sql_insert, (city,country_id))

def initial_cities_table_insert():
	'''
	Insert initial rows.
	'''

	initial_dataset = INITIAL_CITIES

	for item in initial_dataset:
		num = check_insert_into_cities(item)

if __name__ == '__main__':
	initial_cities_table_insert()
