
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import csv
import os
xnewfile=[]
xname = []
def load_file():
    fname = askopenfilename(filetypes=(("CSV files", "*.csv"),
                                           ("All files", "*.*") ))
    label0 = Label()
    label0.grid(row=2, column=0, padx=10, sticky=W)           
    label2 = Label(text=fname, width=50)
    label2.grid(row=2, column=4, columnspan=2, sticky=W)



    xname.append(fname)
    return fname



def openfile():
    ynewfile = str(xnewfile[0])
    os.startfile(ynewfile)



def dedupe():
    yname = str(xname[0])
    reader=csv.reader(open(yname, 'r'), delimiter=',')
    writer=csv.writer(open(yname+'_NoDupes.csv', 'w', newline=''), delimiter=',')
    entries = set()

    for row in reader:
       key = (row[0]) # instead of just the last name

       if key not in entries:
          writer.writerow(row)
          entries.add(key)

    label3 = Label(text="New File:        ")
    label3.grid(row=3, column=1, sticky=W)

    button3 = Button(text="Open", command=openfile, width=10)
    button3.grid(row=3, column=2, sticky=W)
    
    label4 = Label(text="           "+yname+"_NoDupes.csv" )
    label4.grid(row=3, column=3, sticky=W, columnspan=4, padx=10)

    newfile = yname+"_NoDupes.csv"
    xnewfile.append(newfile)
    return newfile

 

root = Tk()
root.title("CSV Deduplication")
root.rowconfigure(5, weight=1)
root.columnconfigure(5, weight=1)
root.minsize(width=700, height=140)
#root.grid(sticky=W+E+N+S)



label0 = Label()
label0.grid(row=2, column=0, padx=10, sticky=W)

label00 = Label()
label00.grid(row=0, column=0, padx=10, sticky=W)

label5 = Label(text="Checks First Column")
label5.grid(row=1, column=1, sticky=W)

label01 = Label()
label01.grid(row=0, column=0, padx=10, sticky=W)

label1 = Label(text="CSV Location: ")
label1.grid(row=2, column=1, sticky=W)

button1 = Button(text="Browse", command=load_file, width=10)
button1.grid(row=2, column=2, sticky=W, pady=10)

button2 = Button(text="Dedupe", command=dedupe, width=10)
button2.grid(row=2, column=3, sticky=W, padx=10)








root.mainloop()
