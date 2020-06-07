import mysql.connector

def login(username, password):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="testdatabase"
        )
        mycursor = db.cursor()
        sql = "SELECT * FROM users  WHERE username = \'" + username + "\';"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()[0]
        if myresult[2] == password:
            return True
        return False
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        return "500 Internal Server Error"
