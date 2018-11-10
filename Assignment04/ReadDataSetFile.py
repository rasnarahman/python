"""CST8333: Assignment 03 – Proof of Concept Delivery
   Author: Rasna Rahman
   Date: October 10, 2018
   this class opening the .csv file and loading it in a label. It has sorting option to print the columns sorted by 3 columns."""

import pymysql
import tkinter  # import the tkinter
import csv  # import the csv
from tkinter import *
from tkinter.filedialog import askopenfilename  # import the method to open the file(Dialog Box)
import pymysql

class ReadDataSetFile:  # class ReadDataSetFile created

    def __init__(self):  # constructor
        self

    def verifyCsvFile(self, filePath):                  #.csv file verification method.
        if ".csv" not in filePath:
            return False
        else:
            return True

    # method to access the database.
    def connect_db(self):
        cnx = pymysql.connect ( user='root',password='Ottawa2018',host='localhost',database='assignment4' )
        return cnx

    # method for executing the query to insert the data to the db.

    def mysql_insert_data(self, connection,query):
        try:
            cursor = connection.cursor ()
            cursor.execute ( query )
            connection.commit ()
            cursor.close ()
        except Exception as exc:
            raise exc


    def load_data(self, sortProperty, filterProperty):                    # method to read the .csv file and load columns
        csv_file_path = askopenfilename()

        if not self.verifyCsvFile(csv_file_path):         #varufication of the .csv file
            raise Exception("Not a valid CSV file!")

        tk = tkinter.Tk()
        self.close_button = Button(tk, text="Close", width=10, command=tk.destroy).pack(side=BOTTOM)  # Button to close the window
        self.insert_button = Button ( tk,text="InsertToDB",width=10,command=lambda: self.insert_data(csv_file_path) ).pack ( side=BOTTOM )
        scrollbar = Scrollbar(tk)                       # Scrollbar to scroll the data file
        scrollbar.pack(side=RIGHT, fill=Y)
        tk.geometry("700x550")                          # size for the open window.

        lb1 = Listbox(tk, width=100)  # created the list box to hold the data

        # attach listbox to scrollbar
        lb1.config ( yscrollcommand=scrollbar.set )
        scrollbar.config ( command=lb1.yview )

        i = 0
        try:                                                  # try catch block to handle the exceptions.
            with open(csv_file_path) as dataSet:
                reader = csv.reader(dataSet, delimiter=',')


                print("Sort property: " + sortProperty)          #if -else diicission structure for sorting the columns.
                if sortProperty == "REF_DATE":
                    reader = sorted ( reader,key=lambda row: row[0])
                elif sortProperty == "COMMODITY":
                    reader = sorted ( reader,key=lambda row: row[4])
                elif sortProperty == "VALUE":
                    reader = sorted ( reader, key=lambda row: row[11])

                print("Filter property: " + filterProperty)          #if -else diicission structure for sorting the columns.
                if filterProperty == "AVAILABLE":
                    reader = filter ( lambda p: 'Food available'==p[3],reader )
                elif filterProperty == "ADUSTED_FOR_LOSSES":
                    reader = filter ( lambda p: 'Food available adjusted for losses'==p[3],reader )

                for row in reader:
                    if i == 0:                             # Skip the first row and print title
                        data = "YEAR  -  COUNTRY  -  COMMODITY  -  VECTOR  -  COORDINATE  -  VALUE  -  CATEGORIES "

                        lb1.insert(i, data)
                        i = i + 1
                        continue
                    year = row[0]
                    country = row[1]
                    commodity = row[4]
                    vector = row[9]
                    coordinate = row[10]
                    categories = row[3]
                    value = row[11]
                    data = year + " - " + country + " - " + commodity + " - " + vector + " - " + coordinate + " - " + value+" - "+ categories
                    lb1.insert(i, data)   # print the rows
                    i = i + 1
                lb1.pack(side=LEFT, fill=BOTH)
            tk.mainloop()
            dataSet.close()
        except IOError:                               # exception handling
            print("could not open the file:")



    def insert_data(self, csv_file_path):
        tk = tkinter.Tk ()
        dbconnection = self.connect_db ()
        i = 0
        try:  # try catch block to handle the exceptions.
            with open ( csv_file_path ) as dataSet:
                reader = csv.reader ( dataSet,delimiter=',' )

                for row in reader:
                    if i==0:  # Skip the first row and print title

                        i = i + 1
                        continue
                    year = row[0]
                    country = row[1]
                    commodity = row[4]
                    vector = row[9]
                    coordinate = row[10]
                    categories = row[3]
                    value = row[11]
                    query = "INSERT INTO food VALUES ( '" + year + "','" + country + "','" + commodity + "','" + vector + "','" + coordinate + "','" + categories + "','" + value + "')"
                    self.mysql_insert_data ( dbconnection,query )
                    i = i + 1
            tk.mainloop ()
            dataSet.close ()
        except IOError:  # exception handling
            print ( "could not open the file:" )