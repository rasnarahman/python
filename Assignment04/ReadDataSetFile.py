"""CST8333: Assignment 03 – Proof of Concept Delivery
   Author: Rasna Rahman
   Date: October 10, 2018
   this class opening the .csv file and loading it in a label. It has sorting option to print the columns sorted by 3 columns."""

import csv  # import the csv
import tkinter  # import the tkinter
from tkinter import *
import tkinter.ttk as ttk

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

    def mysql_select_data(self,connection,query):
        try:
            cursor = connection.cursor ()
            cursor.execute ( query )
            data = cursor.fetchall ()
            cursor.close ()
            return data
        except Exception as exc:
            raise exc


    def load_data(self, sortProperty, filterProperty):      # method to read the .csv file and load columns
        csv_file_path = askopenfilename()

        if not self.verifyCsvFile(csv_file_path):         #varufication of the .csv file
            raise Exception("Not a valid CSV file!")

        tk = tkinter.Tk()
        tk.title("Python - Import CSV File To Tkinter Table")
        width = 700
        height = 600
        screen_width = tk.winfo_screenwidth ()
        screen_height = tk.winfo_screenheight ()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        tk.geometry ( "%dx%d+%d+%d" % (width,height,x,y) )
        tk.resizable ( 0,0 )
        self.close_button = Button(tk, text="Close", width=15, command=tk.destroy).pack(side=BOTTOM)
        self.insert_button = Button ( tk,text="Insert To DB",width=15,command=lambda: self.insert_data(csv_file_path) ).pack ( side=BOTTOM )
        self.insert_button = Button ( tk,text="Display From DB",width=15,command=lambda: self.display_data_from_DB ( ) ).pack ( side=BOTTOM )

        TableMargin = Frame ( tk,width=500 )
        TableMargin.pack ( side=TOP )
        scrollbarx = Scrollbar ( TableMargin,orient=HORIZONTAL )
        scrollbary = Scrollbar ( TableMargin,orient=VERTICAL )
        tree = ttk.Treeview ( TableMargin, height=400,selectmode="extended",yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set,
                              columns=("REF_DATE",
                                       "GEO",
                                       "DGUID",
                                       "FoodCategories",
                                       "Commodity",
                                       "UOM",
                                       "UOM_ID",
                                       "SCALAR_FACTOR",
                                       "SCALAR_ID",
                                       "VECTOR",
                                       "COORDINATE",
                                       "VALUE",
                                       "STATUS",
                                       "SYMBOLS",
                                       "TERMINATED",
                                       "DECIMALS"))
        scrollbary.config ( command=tree.yview )
        scrollbary.pack ( side=RIGHT,fill=Y )
        scrollbarx.config ( command=tree.xview )
        scrollbarx.pack ( side=BOTTOM,fill=X )

        tree.heading ( 'REF_DATE',text="REF_DATE",anchor=W )
        tree.heading ( 'GEO',text="GEO",anchor=W )
        tree.heading ( 'DGUID',text="DGUID",anchor=W )
        tree.heading ( 'FoodCategories',text="FoodCategories",anchor=W )
        tree.heading ( 'Commodity',text="Commodity",anchor=W )
        tree.heading ( 'UOM',text="UOM",anchor=W )
        tree.heading ( 'UOM_ID',text="UOM_ID",anchor=W )
        tree.heading ( 'SCALAR_FACTOR',text="SCALAR_FACTOR",anchor=W )
        tree.heading ( 'SCALAR_ID',text="SCALAR_ID",anchor=W )
        tree.heading ( 'VECTOR',text="VECTOR",anchor=W )
        tree.heading ( 'COORDINATE',text="COORDINATE",anchor=W )
        tree.heading ( 'VALUE',text="VALUE",anchor=W )
        tree.heading ( 'STATUS',text="STATUS",anchor=W )
        tree.heading ( 'SYMBOLS',text="SYMBOLS",anchor=W )
        tree.heading ( 'TERMINATED',text="TERMINATED",anchor=W )
        tree.heading ( 'DECIMALS',text="DECIMALS",anchor=W )

        tree.column ( '#0',stretch=NO,minwidth=0,width=0 )
        tree.column ( '#1',stretch=NO,minwidth=0,width=70 )
        tree.column ( '#2',stretch=NO,minwidth=0,width=70 )
        tree.column ( '#3',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#4',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#5',stretch=NO,minwidth=0,width=200 )
        tree.column ( '#6',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#7',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#8',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#9',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#10',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#11',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#12',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#13',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#14',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#15',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#16',stretch=NO,minwidth=0,width=100 )

        tree.pack ()

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
                    refDate = row[0]
                    geo = row[1]
                    dguid = row[2]
                    foodCategories = row[3]
                    commodity = row[4]
                    uom = row[5]
                    uomId = row[6]
                    scalarFactor = row[7]
                    scalarId = row[8]
                    vector = row[9]
                    coordinate = row[10]
                    value = row[11]
                    status = row[12]
                    symbols = row[13]
                    terminated = row[14]
                    decimals = row[15]

                    tree.insert ( "",0,values=(refDate,geo,dguid,foodCategories,commodity,uom,uomId,scalarFactor,scalarId,
                                          vector,coordinate,value,status,symbols,terminated,decimals))

            tk.mainloop()
            dataSet.close()
        except IOError:                               # exception handling
            print("could not open the file:")



    def insert_data(self, csv_file_path):
        dbconnection = self.connect_db ()
        i = 0
        try:  # try catch block to handle the exceptions.
            with open ( csv_file_path ) as dataSet:
                reader = csv.reader ( dataSet,delimiter=',' )

                for row in reader:
                    if i==0:  # Skip the first row and print title

                        i = i + 1
                        continue
                    refDate = row[0]
                    geo = row[1]
                    dguid = row[2]
                    foodCategories = row[3]
                    commodity = row[4]
                    uom = row[5]
                    uomId = row[6]
                    scalarFactor = row[7]
                    scalarId = row[8]
                    vector = row[9]
                    coordinate = row[10]
                    value = row[11]
                    status = row[12]
                    symbols = row[13]
                    terminated = row[14]
                    decimals = row[15]

                    query = "INSERT INTO assignment4.food (`REF_DATE`,`GEO`,`DGUID`,`FoodCategories`,`Commodity`,`UOM`,`UOM_ID`,`SCALAR_FACTOR`,`SCALAR_ID`,`VECTOR`,`COORDINATE`,`VALUE`,`STATUS`,`SYMBOLS`,`TERMINATED`,`DECIMALS`) VALUES ( '" + refDate + "','" +  geo + "','" + dguid + "','" +  foodCategories + "','" + commodity + "','" + uom + "','" + uomId + "','" + scalarFactor + "','" + scalarId + "','" + vector + "','" + coordinate + "','" + value + "','" + status + "','" + symbols + "','" + terminated + "','" + decimals + "')"
                    self.mysql_insert_data ( dbconnection,query )
                    i = i + 1
            dataSet.close ()
        except IOError:  # exception handling
            print ( "could not open the file:" )


    def display_data_from_DB(self):
        dbconnection = self.connect_db ()
        query = "SELECT * FROM food"
        data = self.mysql_select_data(dbconnection, query)

        tk = tkinter.Tk()
        tk.title("Python - Display from DB")
        width = 700
        height = 600
        screen_width = tk.winfo_screenwidth ()
        screen_height = tk.winfo_screenheight ()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        tk.geometry ( "%dx%d+%d+%d" % (width,height,x,y) )
        tk.resizable ( 0,0 )

        TableMargin = Frame ( tk,width=500 )
        TableMargin.pack ( side=TOP )
        scrollbarx = Scrollbar ( TableMargin,orient=HORIZONTAL )
        scrollbary = Scrollbar ( TableMargin,orient=VERTICAL )
        tree = ttk.Treeview ( TableMargin, height=400,selectmode="extended",yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set,
                              columns=("ID",
                                        "REF_DATE",
                                       "GEO",
                                       "DGUID",
                                       "FoodCategories",
                                       "Commodity",
                                       "UOM",
                                       "UOM_ID",
                                       "SCALAR_FACTOR",
                                       "SCALAR_ID",
                                       "VECTOR",
                                       "COORDINATE",
                                       "VALUE",
                                       "STATUS",
                                       "SYMBOLS",
                                       "TERMINATED",
                                       "DECIMALS"))
        scrollbary.config ( command=tree.yview )
        scrollbary.pack ( side=RIGHT,fill=Y )
        scrollbarx.config ( command=tree.xview )
        scrollbarx.pack ( side=BOTTOM,fill=X )

        tree.heading ( 'ID',text="ID",anchor=W )
        tree.heading ( 'REF_DATE',text="REF_DATE",anchor=W )
        tree.heading ( 'GEO',text="GEO",anchor=W )
        tree.heading ( 'DGUID',text="DGUID",anchor=W )
        tree.heading ( 'FoodCategories',text="FoodCategories",anchor=W )
        tree.heading ( 'Commodity',text="Commodity",anchor=W )
        tree.heading ( 'UOM',text="UOM",anchor=W )
        tree.heading ( 'UOM_ID',text="UOM_ID",anchor=W )
        tree.heading ( 'SCALAR_FACTOR',text="SCALAR_FACTOR",anchor=W )
        tree.heading ( 'SCALAR_ID',text="SCALAR_ID",anchor=W )
        tree.heading ( 'VECTOR',text="VECTOR",anchor=W )
        tree.heading ( 'COORDINATE',text="COORDINATE",anchor=W )
        tree.heading ( 'VALUE',text="VALUE",anchor=W )
        tree.heading ( 'STATUS',text="STATUS",anchor=W )
        tree.heading ( 'SYMBOLS',text="SYMBOLS",anchor=W )
        tree.heading ( 'TERMINATED',text="TERMINATED",anchor=W )
        tree.heading ( 'DECIMALS',text="DECIMALS",anchor=W )

        tree.column ( '#0',stretch=NO,minwidth=0,width=0 )
        tree.column ( '#1',stretch=NO,minwidth=0,width=70 )
        tree.column ( '#2',stretch=NO,minwidth=0,width=70 )
        tree.column ( '#3',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#4',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#5',stretch=NO,minwidth=0,width=200 )
        tree.column ( '#6',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#7',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#8',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#9',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#10',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#11',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#12',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#13',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#14',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#15',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#16',stretch=NO,minwidth=0,width=100 )
        tree.column ( '#17',stretch=NO,minwidth=0,width=100 )

        tree.pack ()

        i = 0
        try:
            for row in data:
                id = row[0]
                refDate = row[1]
                geo = row[2]
                dguid = row[3]
                foodCategories = row[4]
                commodity = row[5]
                uom = row[6]
                uomId = row[7]
                scalarFactor = row[8]
                scalarId = row[9]
                vector = row[10]
                coordinate = row[11]
                value = row[12]
                status = row[13]
                symbols = row[14]
                terminated = row[15]
                decimals = row[16]

                tree.insert ( "",0,values=(id,refDate,geo,dguid,foodCategories,commodity,uom,uomId,scalarFactor,scalarId,
                                      vector,coordinate,value,status,symbols,terminated,decimals))

            tk.mainloop()
        except IOError:                               # exception handling
            print("could not open the file:")