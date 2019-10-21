from config import DB_FILE
from config import INITIAL_STADIUMS
from util import insert_into_table
from util import check_insert_into_table

from db_setup.insert_into_cities import check_insert_into_cities
from db_setup.insert_into_countries import check_insert_into_countries


def insert_into_stadiums(value):
	'''
	Insert one row in Stadiums table
	:param value: value to be inserted in Stadiums table
	'''

	db_file = DB_FILE
	sql = """INSERT INTO Stadiums(name, city_id, country_id, capacity)
			 VALUES(?, ?, ?, ?)"""

	return insert_into_table(db_file, sql, value)


def check_insert_into_stadiums(value):
	'''
	Insert one row if it doest exist otherwise return respective row id
	:param value: value to be inserted
	:return: the id of the row that was inserted or the id of the row
	just inserted
    '''
	name, city, country, capacity = value

	city_id = check_insert_into_cities(city)
	country_id = check_insert_into_countries(country)

	db_file = DB_FILE
	#Is there a way to check only the first three elements
	sql_select = "SELECT * FROM Stadiums WHERE name = ? AND city_id = ? AND country_id = ? AND capacity = ?"
	sql_insert = "INSERT INTO Stadiums(name, city_id, country_id, capacity) VALUES(?, ?, ?, ?)"

	return check_insert_into_table(db_file,sql_select, sql_insert, (name,city_id,country_id,capacity))


def initial_stadiums_table_insert():
	'''
	Insert initial rows.
	'''

	initial_dataset = INITIAL_STADIUMS

	for item in initial_dataset:
		num = insert_into_stadiums(item)

if __name__ == '__main__':
	initial_stadiums_table_insert()
