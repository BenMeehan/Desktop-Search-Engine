from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo,showwarning

import core

i=core.IndexSearch()


# Root Window and grid setup
window=Tk()

window.title("Desktop Search Engine")
window.geometry("750x450+100+100")
window.resizable()

window.columnconfigure(3)
window.rowconfigure(7)


# Part of GUI to get the folder path and create or load a index
ttk.Label(window,text="Enter the path to index : ",font=("Helvetica", 12)).grid(column=0,row=0,padx=(50,0),pady=(50,20))

folderPath=ttk.Entry(window,width=50,font=("Helvetica", 10))
folderPath.grid(row=0,column=1,pady=(50,20),padx=(20,0))


def getFolder():        # Function for browse button to browse and select directory
    folderPath.delete(0,END)
    folderPath.insert(0,string=filedialog.askdirectory())

ttk.Button(text="browse",command=getFolder).grid(column=2,row=0,padx=(0,50),pady=(50,20))


def create():           # Function for create index
    if folderPath.get()=="":
        showwarning("Empty Path","Select or Enter a valid directory")
    elif i.create_index(folderPath.get()):
        showinfo("Success","Index Created Successfully!")

ttk.Button(text="Create Index",command=create).grid(column=1,row=1,padx=(0,250))


def load():             #Function for load index
    if i.load_index():
        showinfo("Success","Index Loaded Successfully!")

ttk.Button(text="Load Existing Index",command=load).grid(column=1,row=1)

# Part of the GUI to search a file or folder
ttk.Label(window,text="Enter name to search : ",font=("Helvetica", 12)).grid(column=0,row=2,padx=(50,0),pady=(50,20))

name=ttk.Entry(window,width=50,font=("Helvetica", 10))
name.grid(row=2,column=1,columnspan=2,pady=(50,20),padx=(20,50))

method=StringVar()
ttk.Radiobutton(window,text="starts with",value="prefix",variable=method).grid(row=3,column=0)
ttk.Radiobutton(window,text="ends with",value="suffix",variable=method).grid(row=3,column=1)
ttk.Radiobutton(window,text="all",value="all",variable=method).grid(row=3,column=2)

type=StringVar()
ttk.Label(window,text="Choose a type",font=("Helvetica", 12)).grid(column=0,row=4,padx=(50,0),pady=(50,20))
ttk.Radiobutton(window,text="files",value="files",variable=type).grid(row=5,column=0,padx=(0,15))
ttk.Radiobutton(window,text="folders",value="folders",variable=type).grid(row=6,column=0)


def search():           # Function to call the correct search method based on options
    if type.get()=="files":
        i.search_files(name.get(),method.get())
    else:
        i.search_dirs(name.get(),method.get())


ttk.Button(text="Search",command=search).grid(column=1,row=7)

window.mainloop()