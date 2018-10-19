
from tkinter import Tk, Label, Button, StringVar, Frame, TOP, NO, NONE, LEFT
from Assignment03 import file_Read


class DisplayDataSetGUI:

    def __init__(self, master):
        self.master = master
        master.wm_title('TestDataSetGUI' )
        frame = Frame(master)
        frame.pack()
        master.geometry("300x100")

        fileReadLoadData = file_Read.load_Data()
        Button(frame, text='Open File', width=20, command=lambda: fileReadLoadData.load_data()).grid(row=3, column=0)

        self.close_button = Button(frame, text="Exit", width=20, command=root.destroy)
        self.close_button.grid(row=4, column=0)


root = Tk()
my_gui = DisplayDataSetGUI(root)
root.mainloop()
