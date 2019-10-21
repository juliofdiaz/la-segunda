from config import DB_FILE
from config import INITIAL_CLUBS
from util import insert_into_table
from util import check_insert_into_table

from db_setup.insert_into_cities import check_insert_into_cities
from db_setup.insert_into_countries import check_insert_into_countries
from db_setup.insert_into_stadiums import check_insert_into_stadiums


def insert_into_clubs(value):
	'''
	Insert one row in Clubs table
	:param value: value to be inserted in Clubs table
	'''

	db_file = DB_FILE
	sql = """INSERT INTO Clubs(name, full_name, dob, city_id, country_id, stadium_id)
			 VALUES(?, ?, ?, ?, ?, ?)"""

	return insert_into_table(db_file, sql, value)


def check_insert_into_clubs(value):
	'''
	Insert one row if it doest exist otherwise return respective row id
	:param value: value to be inserted
	:return: the id of the row that was inserted or the id of the row
	just inserted
    '''
	name, full_name, dob, city, country, stadium = value

	city_id = check_insert_into_cities(city)
	country_id = check_insert_into_countries(country)
	stadium_id = check_insert_into_stadiums(stadium)

	return insert_into_clubs((name,full_name,dob,city_id,country_id,stadium_id))


def initial_clubs_table_insert():
	'''
	Insert initial rows.
	'''

	initial_dataset = INITIAL_CLUBS

	for item in initial_dataset:
		num = insert_into_clubs(item)

if __name__ == '__main__':
	initial_clubs_table_insert()
