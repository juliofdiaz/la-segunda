import re
import sqlite3
import pandas as pd
from sqlite3 import Error

def month_num(month):
    """ Get a numberical value for the month string """
    switcher={
        "Jan":"01",
        "Feb":"02",
        "Mar":"03",
        "Apr":"04",
        "May":"05",
        "Jun":"06",
        "Jul":"07",
        "Aug":"08",
        "Sep":"09",
        "Oct":"10",
        "Nov":"11",
        "Dec":"12"
        }
    return switcher.get(month,"??")


def fmt_day(day):
    """ Format number to have leading 0 if single digit"""
    if len(day) == 1:
        return "0"+day
    else:
        return day


def format_time(time_string):
    """ Make date string python friendly"""
    temp = time_string.split(" (")[0]
    temp_2 = re.split(' |, ',temp)
    if len(temp_2) == 3:
        return temp_2[2]+"-"+month_num(temp_2[0])+"-"+fmt_day(temp_2[1])+" 00:00:00"
    else:
        return "-"


def format_name(name_string):
    """ Splits full name into first name and last name"""
    return (name_string[:name_string.rfind(" ")],name_string[name_string.rfind(" "):])


def format_height(height_string):
    numerals = [int(s) for s in re.findall(r'\b\d+\b', height_string)]
    #return int(height_string.split(" ")[0].replace(',',''))
    return str(numerals[0]) + str(numerals[1])

def create_connection(db_file):
    """
    create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(db_file, sql_create_table):
    database = db_file

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create players table
        try:
            c = conn.cursor()
            c.execute(sql_create_table)
        except Error as e:
            print(e)
    else:
        print("Error! cannot create the database connection.")


def insert_into_table(db_file, sql_insert_data, value):
    database = db_file

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        cur = conn.cursor()
        data = cur.execute(sql_insert_data, value)
        print("[Recorded] value:"+str(value)+" AT id:"+str(cur.lastrowid) )
        return cur.lastrowid


def check_insert_into_table(db_file, sql_select, sql_insert, value):
    connection = create_connection(db_file)

    cursor = connection.cursor()
    cursor.execute(sql_select, value)
    data = cursor.fetchone()

    if data is None:
        row = insert_into_table(db_file, sql_insert,value)
        return row
    else:
        value, row = value,data[0]
        print("[Found] value:"+str(value)+" AT id:"+str(row))
        return row


def select_from_table(db_file, sql_select):
    database = db_file

    # create a database connection
    conn = create_connection(database)
    with conn:

        cur = conn.cursor()
        cur.execute( sql_select )

        rows = cur.fetchall()
        return pd.DataFrame(rows)
