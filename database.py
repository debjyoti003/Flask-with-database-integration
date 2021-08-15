import mysql.connector

def database_connection():
    mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "J34tcadvd2@", database = "flaskapp")
    c = mydb.cursor(buffered=True)
    return c, mydb