import mysql.connector
from mysql.connector import Error
import json



def check_user(username, password):
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
                query = ("SELECT username, password FROM users WHERE username = '" + str(username) + "'")
                cursor.execute(query)
                fetch = cursor.fetchall()
                Dbpassword = fetch[0][1]
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                response = {}
                if Dbpassword == password:
                    response['id'] = get_id(username)
                    response['status'] = 'True'
                else:
                    response['status'] = 'False'
                return json.dumps(response)
            except:
                response = {}
                response['status'] = 'False'
                return json.dumps(response)

def get_id(username):
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
            query = ("SELECT id FROM users WHERE username = '" + str(username) + "'")
            cursor.execute(query)
            fetch = cursor.fetchall()
            id = fetch[0][0]
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return id

def register_user(username, password, email, phone_number):
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
            #query = ("SELECT username, password FROM users WHERE username = '" + str(username) + "'")
            try:
                query = ("INSERT INTO users (username, password, email, phone_number) VALUES ('"+username+"', '"+password+"','"+email+"','"+phone_number+"')")
                cursor.execute(query)
                connection.commit()
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                response = {}
                response['status'] = 'True'
                return json.dumps(response)
            except:
                response = {}
                response['status'] = 'False'
                return json.dumps(response)


def get_all_info(id):
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
                query = ("SELECT username, password, email, phone_number FROM users WHERE id = '" + str(id) + "'")
                cursor.execute(query)
                fetch = cursor.fetchall()

                Dbpassword = fetch[0][1]
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                response = {}
                response['status'] = 'True'
                response['username'] = fetch[0][0]
                response['email'] = fetch[0][2]
                response['phone_number'] = fetch[0][3]
                return json.dumps(response)
            except:
                response = {}
                response['status'] = 'False'
                return json.dumps(response)

def register_ad(title, userid, description, category, location):
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
                #query = ("SELECT username, password FROM users WHERE username = '" + str(username) + "'")
                try:
                    query = ("INSERT INTO ads (title, user_id, description, category, location) VALUES ('"+title+"', '"+userid+"','"+description+"','"+category+"','"+location+"')")
                    cursor.execute(query)
                    connection.commit()
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")
                    response = {}
                    response['id'] = get_ad_id(title)
                    response['status'] = 'True'
                    return json.dumps(response)
                except:
                    response = {}
                    response['status'] = 'False'
                    return json.dumps(response)




def get_ad_id(title):
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
            query = ("SELECT id FROM ads WHERE title = '" + str(title) + "'")
            cursor.execute(query)
            fetch = cursor.fetchall()
            id = fetch[0][0]
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return id


def get_ad_info(id):
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
                query = ("SELECT title, user_id, description, category, location  FROM ads WHERE id = '" + str(id) + "'")
                cursor.execute(query)
                fetch = cursor.fetchall()

                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                response = {}
                response['status'] = 'True'
                response['title'] = fetch[0][0]
                response['user_id'] = fetch[0][1]
                response['description'] = fetch[0][2]
                response['category'] = fetch[0][3]
                response['location'] = fetch[0][4]
                return json.dumps(response)
            except:
                response = {}
                response['status'] = 'False'
                return json.dumps(response)

print(get_ad_info(3))

