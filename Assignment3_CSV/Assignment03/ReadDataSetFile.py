"""CST8333: Assignment 03 – Proof of Concept Delivery
   Author: Rasna Rahman
   Date: October 10, 2018
   this class opening the .csv file and loading it in a label."""

import tkinter  # import the tkinter
import csv  # import the csv
from tkinter import *
from tkinter.filedialog import askopenfilename  # import the method to open the file(Dialog Box)

class ReadDataSetFile:  # class ReadDataSetFile created
    def __init__(self):  # constructor
        self

    def verifyCsvFile(self, filePath):
        if ".csv" not in filePath:
            return False
        else:
            return True

    def load_data(self, sortProperty):                    # method to read the .csv file and load 6 columns
        csv_file_path = askopenfilename()

        if not self.verifyCsvFile(csv_file_path):
            raise Exception("Not a valid CSV file!")

        tk = tkinter.Tk()
        self.close_button = Button(tk, text="Close", width=10, command=tk.destroy).pack(side=BOTTOM)  # Button to close the window
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

                print("Sort property: " + sortProperty)
                if sortProperty == "REF_DATE":
                    reader = sorted ( reader,key=lambda row: row[0])
                elif sortProperty == "COMMODITY":
                    reader = sorted ( reader,key=lambda row: row[4])
                elif sortProperty == "VALUE":
                    reader = sorted ( reader, key=lambda row: row[11])

                #reader = sorted ( reader,key=lambda row: row[0],reverse=True )

                for row in reader:
                    if i == 0: # Skip the first row and print title
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
        except IOError:
            print("could not open the file:")