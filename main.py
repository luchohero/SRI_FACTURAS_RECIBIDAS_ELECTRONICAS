#Import the Tkinter library
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
def convertir_csv(ruta):
    with open(ruta, encoding='latin-1') as f:
        new = f.read().replace("\t",",")
        new = new.replace("\n.", "\n0.")
        new = new.replace(",,", ",")
        count = 1
        string_final = ""
        #print(new)
        for r in new:
            if r == "\n":
                if count % 2 != 0:
                    string_final = string_final + ","
                else:
                    string_final = string_final + r
                count = count + 1
            else:
                string_final = string_final + r
        crear_csv(string_final)

def crear_csv(contenido):
    file = open("file.csv", "w")
    file.write(contenido)
    file.close()

def crear_xls(contenido):
    pass



#Create an instance of Tkinter frame
win= Tk()
#Define the geometry
win.geometry("600x300")
def select_file():
   path= filedialog.askopenfilename(title="Seleccionar arcivo txt", filetype=(('text files''*.txt'),('all files','*.*')))
   Label(win, text=path, font=13).pack()
   convertir_csv(path)
#Create a label and a Button to Open the dialog
Label(win, text="SELECCIONAR EL ARCHIVO FORMATO .TXT", font=('Aerial 18 bold')).pack(pady=20)
button= ttk.Button(win, text="SELECCIONAR", command= select_file)
button.pack(ipadx=5, pady=15)
win.mainloop()