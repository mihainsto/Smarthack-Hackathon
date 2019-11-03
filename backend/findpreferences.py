import mysql.connector
from mysql.connector import Error
from phone_service import send_sms
import json
import requests


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




def check_matches(title, description, category):
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
            #try:
                print('check Called')
                print(title, description, category)
                query = ("SELECT user_preferences.*, `users`.`phone_number` FROM `user_preferences` LEFT JOIN `users` ON `users`.id = `user_preferences`.`user_id` WHERE category = '"+category+"' ")
                cursor.execute(query)
                fetch = cursor.fetchall()
                #print(fetch)
                preferences = []
                print(fetch)
                for i in range(len(fetch)):
                    keyword = fetch[i][3]
                    phone_number = fetch[i][4]
                    old_title = title
                    title = title.replace(' ','_')
                    description = description.replace(' ','_')
                    keyword = keyword.replace(' ','_') 

                    text = title
                    response = requests.get("http://23.100.11.91/simget/"+text+"/"+keyword)
                    if response.json()['stauts'] == 'True':
                        print('call')
                        print(phone_number)
                        send_sms(phone_number,'Hei, s-ar putea sa te intereseze urmatorul anunt tocmai postat:' + old_title)
                        continue

                    text = description
                    response = requests.get("http://23.100.11.91/simget/"+text+"/"+keyword)
                    if response.json()['stauts'] == 'True':
                        print('call')
                        print(phone_number)
                        send_sms(phone_number,'Hei, s-ar putea sa te intereseze urmatorul anunt tocmai postat:' + old_title)
                        continue


                
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                return preferences
            #except:
                #response = {}
                #response['status'] = 'False'
                #return json.dumps(response)


#check_matches(12, '2', 'Bucuresti')
#print(find_preferences('300'))

#check_matches('Donez', 'Donez combina frigorifica', '2')  	

