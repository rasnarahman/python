import tkinter  # import the tkinter
import csv  # import the csv
from tkinter import *
from tkinter.filedialog import askopenfilename  # import the method askopenfilename


class load_Data:  # create class DisplayDataSet
    def __init__(self):  # create the constructor of DisplayDataSet
        self

    def load_data(self):
        csv_file_path = askopenfilename()

        tk = tkinter.Tk()
        self.close_button = Button(tk, text="Close", width=10, command=tk.destroy).pack(side=BOTTOM)
        scrollbar = Scrollbar(tk)
        scrollbar.pack(side=RIGHT, fill=Y)
        tk.geometry("700x550")

        lb1 = Listbox ( tk, yscrollcommand=scrollbar.set, width=100 )  # create the list box
        i = 0
        try:
            with open(csv_file_path) as dataSet:
                reader = csv.reader(dataSet, delimiter=',')

                for row in reader:
                    if i == 0: # Skip the first row and print title
                        data = "YEAR - COUNTRY - COMMODITY - VECTOR - COORDINATE - VALUE"
                        lb1.insert ( i, data )
                        i = i + 1
                        continue
                    year = row[0]
                    country = row[1]
                    commodity = row[4]
                    vector = row[9]
                    coordinate = row[10]
                    value = row[11]
                    data = year + " - " + country + " - " + commodity + " - " + vector + " - " + coordinate + " - " + value
                    lb1.insert ( i, data)
                    i = i + 1
                lb1.pack(side=LEFT, fill=BOTH)
            tk.mainloop()
            dataSet.close()
        except IOError:
            print("could not open the file:")