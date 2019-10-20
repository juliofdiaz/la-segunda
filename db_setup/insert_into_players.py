from config import DB_FILE
from config import INITIAL_PLAYERS
from util import insert_into_table
from util import check_insert_into_table

from db_setup.insert_into_cities import check_insert_into_cities
from db_setup.insert_into_foot import check_insert_into_foot
from db_setup.insert_into_positions import check_insert_into_positions
from db_setup.insert_into_countries import check_insert_into_countries


def check_multi_foreign(values):
	id_list = []
	for v in values:
		print(v)
		id = check_insert_into_countries(v)
		id_list.append(id)

	result = ""
	for id in id_list:
		result = str(id)+","+result
	return result[:-1]

def insert_into_players(value):
	'''
	Insert one row in Cities table
	:param value: value to be inserted in Cities table
	'''

	db_file = DB_FILE
	sql = """INSERT INTO Players(first_name, last_name, name_ob, city_id,
	                             citizenship, date_ob, foot_id, height,
								 position_id, link)
			 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

	return insert_into_table(db_file, sql, value)


def check_insert_into_players(value):
	'''
	Insert one row if it doest exist otherwise return respective row id
	:param value: value to be inserted
	:return: the id of the row that was inserted or the id of the row
	just inserted
    '''
	first_name, last_name, name_ob, city, citizenship, date_ob, foot, height, position, link = value

	city_id = check_insert_into_cities(city)
	foot_id = check_insert_into_foot(foot)
	position_id = check_insert_into_positions(position)

	#db_file = DB_FILE
	#sql_select = "SELECT * FROM Cities WHERE first_name = ? AND last_name_id = ?"
	#sql_insert = "INSERT INTO Cities(city, country_id) VALUES(?, ?)"

	return insert_into_players((first_name,last_name,name_ob,city_id,check_multi_foreign(citizenship),date_ob,foot_id,height,position_id, link))


def initial_players_table_insert():
	'''
	Insert initial rows.
	'''

	initial_dataset = INITIAL_PLAYERS

	for item in initial_dataset:
		num = insert_into_players(item)

if __name__ == '__main__':
	initial_players_table_insert()
