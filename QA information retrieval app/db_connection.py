import mysql.connector
from mysql.connector import Error

def connect():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='rdf',
                                             user='root',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            return connection
            
    except Error as e:
        print("Error while connecting to MySQL", e)