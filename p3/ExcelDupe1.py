from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import csv
import os


class MyFrame(Frame):

    
    def __init__(self):
        Frame.__init__(self)
        self.master.title("CSV Deduplication")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.master.minsize(width=700, height=100)
        self.grid(sticky=W+E+N+S)
        self.fname = ''


        self.label0 = Label(self)
        self.label0.grid(row=2, column=0, padx=10, sticky=W)

        self.label1 = Label(self, text="CSV Location: ")
        self.label1.grid(row=2, column=1, sticky=W)

        self.button1 = Button(self, text="Browse", command=self.load_file, width=10)
        self.button1.grid(row=2, column=2, sticky=W, pady=10)

        self.button2 = Button(self, text="Dedupe", command=self.dedupe, width=10)
        self.button2.grid(row=2, column=3, sticky=W, padx=10)




    def load_file(self):
##        fname = askopenfilename(filetypes=(("CSV files", "*.csv"),
##                                           ("All files", "*.*") ))
        fname = 'x'                               
        label2 = Label(text=fname, width=50)
        label2.grid(row=0, column=4, columnspan=2, sticky=W)                              
        print (fname)
        return fname


    def dedupe(fname):
        print (fname)
        print ('test')
##        reader=csv.reader(open(fname, 'rb'), delimiter=',')
##        writer=csv.writer(open('result.csv', 'w'), delimiter=',')
##        entries = set()
##
##        for row in reader:
##           key = (row[0], row[1]) # instead of just the last name
##
##           if key not in entries:
##              writer.writerow(row)
##              entries.add(key)



if __name__ == "__main__":
    MyFrame().mainloop()
