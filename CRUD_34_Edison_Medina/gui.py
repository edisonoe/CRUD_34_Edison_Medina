from tkinter import *
from tkinter import ttk
import database
import mysql.connector

connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_los_de_mary")

window = Tk()
window.geometry("800x800")
frame_app = Frame(window, width=900, height=600)
frame_app.pack()
window.title("Empleados")




usuario = StringVar()
contraseña = StringVar()
direccion = StringVar()
telefono = StringVar
rtn = StringVar
bancaria = StringVar



def crear_registro():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    rtn = entry_rtn.get()
    bancaria = entry_bancaria.get()
    
    v_db = database.MyDatabase()
    data = (usuario, contraseña, direccion, telefono, rtn, bancaria)
    print(data)
    v_db.insert_db(usuario, contraseña, direccion, telefono, rtn, bancaria)
    



frame_navbar = Frame(frame_app, width=500, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=400)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=300)
frame_options.grid(row=2, column=0)

frame_food = Frame(frame_title, width=1000, height=300, bg="#F89021")
frame_food.place(x=25, y=90)


label_usuario = Label(frame_food, 
              text="Usuario:",
              font=("Calibri", "17", "bold"),
              fg="white",
              bg="#F89021")
label_usuario.place(x=20, y=45)
entry_usuario = Entry(frame_food, justify=LEFT, width=14, font=("Calibri", "14", "bold"))
entry_usuario.place(x=115, y=50)
label_contraseña = Label(frame_food, 
              text="Contraseña:",
              font=("Calibri", "17", "bold"),
              fg="white",
              bg="#F89021")
label_contraseña.place(x=20, y=85)
entry_contraseña = Entry(frame_food, justify=LEFT, width=14, font=("Calibri", "14", "bold"))
entry_contraseña.place(x=140, y=85)

label_direccion = Label(frame_food, 
              text="Dirección:",
              font=("Calibri", "17", "bold"),
              fg="white",
              bg="#F89021")
label_direccion.place(x=20, y=115)
entry_direccion = Entry(frame_food, justify=LEFT, width=14, font=("Calibri", "14", "bold"))
entry_direccion.place(x=130, y=120)

label_telefono = Label(frame_food, 
              text="Telefono:",
              font=("Calibri", "17", "bold"),
              fg="white",
              bg="#F89021")
label_telefono.place(x=20, y=150)
entry_telefono = Entry(frame_food, justify=LEFT, width=14, font=("Calibri", "14", "bold"))
entry_telefono.place(x=130, y=153)

label_rtn = Label(frame_food, 
              text="RTN:",
              font=("Calibri", "17", "bold"),
              fg="white",
              bg="#F89021")
label_rtn.place(x=40, y=180)
entry_rtn = Entry(frame_food, justify=LEFT, width=14, font=("Calibri", "14", "bold"))
entry_rtn.place(x=130, y=185)

label_bancaria = Label(frame_food, 
              text="Cuenta Bancaria:",
              font=("Calibri", "17", "bold"),
              fg="white",
              bg="#F89021")
label_bancaria.place(x=20, y=215)
entry_bancaria = Entry(frame_food, justify=LEFT, width=14, font=("Calibri", "14", "bold"))
entry_bancaria.place(x=190, y=220)


button_agregar = Button(frame_food, text="Crear Pedido", command=crear_registro, font=("Calibri", "12", "bold"))
button_agregar.place(x=120, y=253)


title1 = Label(frame_title, 
             text="Los Tacos De Mary", 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="Todos los campos son obligartorios.", 
              font=("Century Gothic", "14"),justify=LEFT)
title2.place(x=25, y=50)

my_table = ttk.Treeview(frame_app)
my_table['columns'] = ('USUARIO', 'CONTRASEÑA', 'DIRECCION', 'TEL','RTN','CUENTA')
my_table.column('#0', width=55, minwidth=10)
my_table.column('USUARIO', anchor=W, width=60)
my_table.column('CONTRASEÑA', anchor=W, width=85)
my_table.column('DIRECCION', anchor=W, width=80)
my_table.column('TEL', anchor=W, width=60)
my_table.column('RTN', anchor=W, width=60)
my_table.column('CUENTA', anchor=W, width=250)

my_table.heading('#0', text='ID_EMPL', anchor=W)
my_table.heading('USUARIO', text='USUARIO', anchor=W)
my_table.heading('CONTRASEÑA', text='CONTRASEÑA', anchor=W)
my_table.heading('DIRECCION', text='DIRECCION', anchor=W)
my_table.heading('TEL', text='TEL', anchor=W)
my_table.heading('RTN', text='RTN', anchor=W)
my_table.heading('CUENTA', text='CUENTA', anchor=W)

cursor = connection.cursor()
cursor.execute("SELECT USUARIO, CONTRASEÑA, DIRECCION, TELEFONO, RTN, CUENTA_BANCARIA FROM TBL_EMPLEADOS")
registro = 0
for fila in cursor:
        registro = registro + 1
        print(str(registro) +" - "+ str(fila))
        usuario = fila[0]
        contraseña = fila [1]
        direccion = fila[2]
        telefono = fila[3]
        rtn = fila[4]
        bancaria = fila[5]
        my_table.insert(parent= '', index='end' , iid=registro, text=str(registro),
                values=(usuario, contraseña, direccion, telefono, rtn, bancaria))         

connection.close()
  
my_table.place(x=30,y=500)

window.mainloop()