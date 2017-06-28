
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import csv
import os

xname = []
def load_file():
    fname = askopenfilename(filetypes=(("CSV files", "*.csv"),
                                           ("All files", "*.*") ))
    label0 = Label()
    label0.grid(row=2, column=0, padx=10, sticky=W)           
    label2 = Label(text=fname, width=50)
    label2.grid(row=2, column=4, columnspan=2, sticky=W)                              
    print (fname)
    xname.append(fname)
    return fname


def dedupe():
    yname = str(xname[0])
    print (str(xname[0]))
    print ('test')
    reader=csv.reader(open(yname, 'r'), delimiter=',')
    writer=csv.writer(open('result.csv', 'w'), delimiter=',')
    entries = set()

    for row in reader:
       key = (row[0], row[1]) # instead of just the last name

       if key not in entries:
          writer.writerow(row)
          entries.add(key)
    

root = Tk()
root.title("CSV Deduplication")
root.rowconfigure(5, weight=1)
root.columnconfigure(5, weight=1)
root.minsize(width=700, height=100)
#root.grid(sticky=W+E+N+S)



label0 = Label()
label0.grid(row=2, column=0, padx=10, sticky=W)

label1 = Label(text="CSV Location: ")
label1.grid(row=2, column=1, sticky=W)

button1 = Button(text="Browse", command=load_file, width=10)
button1.grid(row=2, column=2, sticky=W, pady=10)

button2 = Button(text="Dedupe", command=dedupe, width=10)
button2.grid(row=2, column=3, sticky=W, padx=10)








root.mainloop()
