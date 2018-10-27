import pymysql
import csv  # import the csv

def connect_db():
    cnx = pymysql.connect( user='root',password='Ottawa2018',host='localhost',database='exercise4')
    return  cnx


def mysql_insert_data(connection, query):
    try:
        cursor = connection.cursor ()
        cursor.execute ( query )
        connection.commit()
        cursor.close ()
    except Exception as exc:
        raise exc


def load_data():                    # method to read the .csv file and load columns
    csv_file_path = "c:\projectData.csv"
    i = 0
    try:
        dbconnection = connect_db ()
        with open(csv_file_path) as dataSet:
            reader = csv.reader(dataSet, delimiter=',')
            for row in reader:
                if i == 0:                             # Skip the first row and print title
                    i = i + 1
                    continue
                year = row[0]
                commodity = row[4]
                value = row[11]
                query = "INSERT INTO food VALUES ( '" + year +"','" + commodity + "','" + value + "')"
                mysql_insert_data(dbconnection, query)
                i = i + 1
        dataSet.close()
        dbconnection.close ()
    except IOError:                               # exception handling
        print("could not open the file:")

load_data()




