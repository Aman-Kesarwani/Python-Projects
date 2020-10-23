'''
Name: Aman Kesarwani
Date: 22/10/2020

Search and Delete File recursively with the extension provided
'''


import os
import time
from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb


class CleanerWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Location')
        self.lbl2=Label(win, text='Older than (Years)')
        self.lbl3 = Label(win, text='Type')

        self.t1=Entry(bd=2)
        self.t2=Entry()
        self.t3=Entry()


        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)

        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)

        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150)

        self.b1=Button(win, text='Start Cleaning', command=self.add)

        self.b1.place(x=100, y=200)


    def validate(self):
        if self.t1.get() == "" or  self.t2.get() == "" or self.t2.get() == "":
            mb.showerror("Warning", "Text Fields Can't be Empty")
            return False

        elif not self.t2.get().isdigit():
            mb.showerror("Warning", "'Older than' should be digit")
            return False

        elif int(self.t2.get()) < 1 or int(self.t2.get()) > 10:
            mb.showerror("Warning", "'Older than' should be in range: 1-10")
            return False

        else:
            return  True

    def add(self):

        if self.validate()== False:
            return

        path = self.t1.get()
        duration = self.t2.get()
        type = self.t3.get()

        print(path)
        print(type)
        self.scandirs(path, duration, type)

        self.reset()

    def reset(self):
        self.t1.delete(0, END)
        self.t1.insert(0, "")

        self.t2.delete(0, END)
        self.t2.insert(0, "")

        self.t3.delete(0, END)
        self.t3.insert(0, "")

    def scandirs(self,path, duration, type):
        now = time.time()

        int_duration = int(duration)

        for root, dirs, files in os.walk(path):
            for currentFile in files:
                absolute_f_name = os.path.join(root, currentFile)
                print(absolute_f_name)

                if os.stat(absolute_f_name).st_mtime < now - (int_duration * 365 * 86400):
                    extension = '.'+type
                    print(extension)
                    tuple_ext = tuple(extension)
                    #In case future requirement
                    #exts = ('.txt', '.exe','.csv', '.pdf')
                    if currentFile.lower().endswith(tuple_ext):
                        os.remove(os.path.join(root, currentFile))

window=Tk()
mywin=CleanerWindow(window)
window.title('Cleaner')
window.geometry("400x300+10+10")
window.mainloop()