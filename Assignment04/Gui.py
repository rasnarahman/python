"""CST8333: Assignment 03 – Proof of Concept Delivery
   Author: Rasna Rahman
   Date: October 10, 2018
   this class displaying the windows and displaying the .csv file.
   Both sorted and in regular file will be displayed"""

from tkinter import Tk, Button, Frame
import ReadDataSetFile
import tkinter as tk


class DisplayDataSetGUI:        #created the DisplayDataSetGUI class

    def __init__(self, master):  # constructor of the class
        self.master = master
        master.wm_title('Programming Language Research Project')
        frame = Frame(master)  # frame created
        frame.pack()
        master.geometry("500x150")    # window size is set.

        v = tk.StringVar ()                            #String variable
        tk.Label ( root,text="""Select Sort Property:""").pack ()
        tk.Radiobutton ( root,text="REF_DATE",padx=200,variable=v,value="REF_DATE" ).pack ( anchor=tk.W)
        tk.Radiobutton ( root,text="COMMODITY",padx=200,variable=v,value="COMMODITY" ).pack ( anchor=tk.W )
        tk.Radiobutton ( root,text="VALUE",padx=200,variable=v,value="VALUE" ).pack ( anchor=tk.W )

        fileReadLoadData = ReadDataSetFile.ReadDataSetFile()
        Button(frame, text='Open File', width=20, command=lambda: fileReadLoadData.load_data(v.get())).grid(row=3, column=0)   # Button to open the file

        self.close_button = Button(frame, text="Exit", width=20, command=root.destroy)                 #close Button
        self.close_button.grid(row=4, column=0)


root = Tk()                        #instantiate root
my_gui = DisplayDataSetGUI(root)   #instantiate my_gui
root.mainloop()                    #start to display
