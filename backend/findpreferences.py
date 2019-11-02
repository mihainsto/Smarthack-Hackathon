import mysql.connector
from mysql.connector import Error
import json



def find_preferences(user_id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='codeleones',
                                             user='user',
                                             password='@pass')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor(buffered=True)
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            try:
                query = ("SELECT keyword FROM user_preferences WHERE user_id = '" + str(user_id) + "'")
                cursor.execute(query)
                fetch = cursor.fetchall()
                #print(fetch)
                preferences = []
                for i in range(len(fetch)):
                	preferences.append(fetch[i][0])
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                return preferences
            except:
            	response = {}
                response['status'] = 'False'
            	return json.dumps(response)


            	

