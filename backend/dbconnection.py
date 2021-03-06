import mysql.connector
from mysql.connector import Error
from findpreferences import check_matches
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
                query = ("SELECT username, password, email, phone_number, register_date FROM users WHERE id = '" + str(id) + "'")
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
                response['register_date'] = str(fetch[0][4])
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
                    check_matches(title, description, category)
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
                query = ("SELECT title, user_id, description, category, location, post_time, active  FROM ads WHERE id = '" + str(id) + "'")
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
                response['post_time'] = str(fetch[0][5])
                response['active'] = fetch[0][6]
                return json.dumps(response)
            except:
                response = {}
                response['status'] = 'False'
                return json.dumps(response)


def get_ad_by_location_category(location, category):
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
                query = ("SELECT title, user_id, description, category, location, post_time  FROM ads WHERE location  LIKE '" + str(location) + "' AND category = '" + str(category) + "' ")
                cursor.execute(query)
                fetch = cursor.fetchall()

                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                response = []
                #print(fetch)
                for i in range(len(fetch)):
                    response_entry = {}
                    response_entry['status'] = 'True'
                    response_entry['title'] = fetch[i][0]
                    response_entry['user_id'] = fetch[i][1]
                    response_entry['description'] = fetch[i][2]
                    response_entry['category'] = fetch[i][3]
                    response_entry['location'] = fetch[i][4]
                    response_entry['post_time'] = str(fetch[i][5])
                    response_entry['id'] = get_ad_id(str(fetch[i][0]))
                    response.append(response_entry)
                return json.dumps(response)
            except:
                response = {}
                response['status'] = 'False'
                return json.dumps(response)


def trigger_ad_activation(id, status):
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
                query = ("UPDATE ads SET active = '"+ str(status) +"' WHERE id = '"+ str(id) +"' ")
                cursor.execute(query)
                #fetch = cursor.fetchall()
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

def get_preference_id(user_id, category, preference):
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
            query = ("SELECT id FROM user_preferences WHERE user_id = '" + str(user_id) + "' AND category = '" + str(category) + "' AND keyword = '" + str(preference) + "'")
            cursor.execute(query)
            fetch = cursor.fetchall()
            id = fetch[0][0]
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return id

def add_preference(user_id, category, preference):
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
                    query = ("INSERT INTO user_preferences (user_id, category, keyword) VALUES ('"+str(user_id)+"', '"+str(category)+"','"+str(preference)+"')")
                    cursor.execute(query)
                    connection.commit()
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")
                    response = {}
                    response['status'] = 'True'
                    response['id'] = get_preference_id(user_id, category, preference)
                    return json.dumps(response)
                except:
                    response = {}
                    response['status'] = 'False'
                    return json.dumps(response)

def get_preferences(user_id):
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
                query = ("SELECT id, category, keyword FROM user_preferences WHERE user_id = '" + str(user_id) + "'")
                cursor.execute(query)
                fetch = cursor.fetchall()

                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                response_ar = []
                for i in range(len(fetch)):
                    response = {}
                    response['status'] = 'True'
                    response['id'] = fetch[i][0]
                    response['category'] = fetch[i][1]
                    response['keyword'] = fetch[i][2]
                    response_ar.append(response)

                return json.dumps(response_ar)
            except:
                response = {}
                response['status'] = 'False'
                return json.dumps(response)


def remove_preference(id):
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
                query = ("DELETE FROM user_preferences WHERE id = '" + str(id) + "'")
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




