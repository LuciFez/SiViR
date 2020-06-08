import mysql.connector

def sing_up(username, password, f_name, l_name):
    if username and f_name and l_name and len(password) > 1: # sparta in mai multe si le trimiti 409 cu motivul
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="root",
                database="testdatabase"
            )
            mycursor = db.cursor()
            mycursor.execute("INSERT INTO users(username, passwd, f_name, l_name) VALUES (%s, %s, %s, %s)", (username, password, f_name, l_name))
            db.commit()
            return "201 Created"
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return "400 Bad Request"

    else:
        return "409 Conflict"
