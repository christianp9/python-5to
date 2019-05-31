import sqlite3
from sqlite3 import Error
from tkinter import *
from tkinter import messagebox
lista = []

# Function to Execute Database Querys
def run_query(query, parameters = ()):
    db_name = ".\data.db"
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result
     
def guardar():
 n = nombre.get()
 ap = app.get()
 am = apm.get()
 c = correo.get()
 t = telefono.get()
 lista.append(n+"$"+ap+"$"+am+"$"+t+"$"+c)
 query = 'INSERT INTO Agenda VALUES(?, ?, ?,?,?)'
 parameters =  (n,ap,am,c,t)
 run_query(query, parameters)
 messagebox.showinfo("Guardado","El contacto ha sido guardado en la agenda")
 nombre.set("")
 app.set("")
 apm.set("")
 correo.set("")
 telefono.set("")
 consultar()

def eliminar():
    eliminado = conteliminar.get()
    query = 'DELETE FROM Agenda WHERE Telefono = ?'
    run_query(query, (eliminado, ))
    consultar()

def consultar():
    r = Text(ventana, width=80, height=15)
    valores = []
    r.insert(INSERT, "Nombre\tApellido \t\tcorte 1\t\tcorte 2\t\tcorte 3\n")
    query = 'SELECT * FROM Agenda'
    db_rows = run_query(query)
    for row in db_rows:
        valores.append(row[3])
        print(row[3])
        r.insert(INSERT, row[0]+"\t"+row[1]+"\t\t"+
        row[2]+"\t\t"+row[3]+"\t\t"+row[4]+"\t\n")
    r.place(x=20,y=230)
    spinTelefono = Spinbox(ventana, value=(valores),textvariable=conteliminar).place(x=450,   y=50)
    if lista ==[]:
        spinTelefono = Spinbox(ventana, value=(valores)).place(x=450,y=50)
    r.config(state=DISABLED)


ventana = Tk()
nombre = StringVar()
app = StringVar()
apm = StringVar()
correo = StringVar()
telefono = StringVar()
conteliminar = StringVar()
colorFondo = "#006"
colorLetra = "#FFF"
consultar()
ventana.title("notas con archivos")
ventana.geometry("700x500")
ventana.configure(background = colorFondo)
etiquetaTitulo = Label(ventana, text="notas con Archivos",
 bg=colorFondo, fg=colorLetra).place(x=270,y=10)
etiquetaN = Label(ventana, text="Nombre", bg=colorFondo,
 fg=colorLetra).place(x=50, y=50)
cajaN = Entry(ventana, textvariable=nombre).place(x=150, y=50)
etiquetaApp = Label(ventana, text="Apellido", bg=colorFondo,
 fg=colorLetra).place(x=50, y=80)
cajaApp = Entry(ventana, textvariable=app).place(x=150, y=80)
etiquetaApm = Label(ventana, text="Corte1", bg=colorFondo,
 fg=colorLetra).place(x=50, y=110)
cajaApm = Entry(ventana, textvariable=apm).place(x=150, y=110)
etiquetaT = Label(ventana, text="Corte 2", bg=colorFondo,
 fg=colorLetra).place(x=50, y=140)
cajaT = Entry(ventana, textvariable=telefono).place(x=150, y=140)
etiquetaC = Label(ventana, text="Corte 3", bg=colorFondo,
 fg=colorLetra).place(x=50, y=170)
cajaC = Entry(ventana, textvariable=correo).place(x=150, y=170)
\
spinTelefono = Spinbox(ventana, textvariable=conteliminar).place(x=450, y=50)
botoGuardar = Button(ventana, text="Guardar", command=guardar, bg="#009",
 fg="white").place(x=180, y=200)
botoEliminar = Button(ventana, text="Eliminar", command=eliminar, bg="#009",
 fg="white").place(x=490, y=80)
mainloop()