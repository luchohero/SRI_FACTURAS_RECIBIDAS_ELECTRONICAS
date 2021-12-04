#Import the Tkinter library
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import csv
import xlsxwriter

def convertir_csv(ruta):
    with open(ruta, encoding='latin-1') as f:
        new = f.read().replace("\t",",")
        new = new.replace("\n.", "\n0.")
        new = new.replace(",,", ",")
        count = 1
        string_final = ""

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
        crear_xls()
def crear_csv(contenido):
    file = open("file_csv.csv", "w")
    file.write(contenido)
    file.close()

def crear_xls():
    with open('file_csv.csv', newline='') as File:
        reader = csv.reader(File)
        workbook = xlsxwriter.Workbook('file_xls.xlsx')
        worksheet = workbook.add_worksheet()
        index = 3

        for row in reader:
            worksheet.write('A' + str(index), row[0])
            worksheet.write('B' + str(index), row[1])
            worksheet.write('C' + str(index), row[2])
            worksheet.write('D' + str(index), row[3])
            worksheet.write('E' + str(index), row[4])
            worksheet.write('F' + str(index), row[5])
            worksheet.write('G' + str(index), row[6])
            worksheet.write('H' + str(index), row[7])
            worksheet.write('I' + str(index), row[8])
            worksheet.write('J' + str(index), row[9])
            worksheet.write('K' + str(index), row[10].replace(".", ","))
            #print(row)
            index+= 1

        workbook.close()





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