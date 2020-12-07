import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import messagebox as MessageBox
import pygame
import pymysql
import os
import psutil
from datetime import date
from datetime import datetime

#LaMusica

#pygame.mixer.init()
#sound1=pygame.mixer.music.load("i.wav")


#menupantalladeinicio

def menu_pantalla ():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("300x400")
    pantalla.resizable(0, 0)
    pantalla.title("TOTALSPEED")
    pantalla.configure(bg='black')

    #icono
    pantalla.iconbitmap(r"C:\\Users\\mike2\\Desktop\\seminario\\icono.ico")
    





    #logo
    Label(text="                                        ", bg="black", fg="black", width="300", height="2").pack()
    image=PhotoImage(file="logo.png")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()
    Label(text="                                        ", bg="black", fg="black", width="300", height="2").pack()
    Label(text="Acceso al Sistema", bg="white", fg="black", width="300", height="2", font=("Calibri", 15),).pack()
    #botones

    inic1= tkinter.Button(pantalla, text ="Iniciar Sesión ", width = 30 ,height=2, bg="yellow",fg="black",borderwidth=5, relief="raised", command=inicio_sesion )
    inic1.place(x=45, y=270)

    inic2= tkinter.Button(pantalla, text ="Registrarse ",width = 30 ,height=2, bg="yellow",fg="black",borderwidth=5, relief="raised", command=registrar)
    inic2.place(x=45, y=330)

    pantalla.mainloop()
#pantalla Inicio de Sesion
def inicio_sesion():

    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("300x300")
    pantalla1.resizable(0, 0)
    pantalla1.title("Inicio de Sesion")
    pantalla1.iconbitmap(r"C:\\Users\\mike2\\Desktop\\seminario\\icono.ico")





    Label(pantalla1, text="Ingrese su Usuario y Contraseña", bg="black", fg="white",width="300", height="2", font=("Calibri", 15)).pack()
    Label(pantalla1, text="").pack()
    #variables
    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify=StringVar()
    contrasenausuario_verify=StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry



    #entrada a usuario
    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry= Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()
    #entrada a contraseña
    Label(pantalla1, text="Contraseña").pack()
    contrasena_usuario_entry= Entry(pantalla1, show="*", textvariable=contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()
    #boton iniciar sesion
    inic3 = tkinter.Button(pantalla1, text="Iniciar Sesion ", width=30, height=2, bg="yellow", fg="black", borderwidth=5, relief="raised", command=validacion_datos)
    inic3.place(x=45, y=225)

#registrar usuario
def registrar():
    global pantalla2
    pantalla2=Toplevel(pantalla)
    pantalla2.geometry("300x300")
    pantalla2.resizable(0, 0)
    pantalla2.title("Registro")
    pantalla2.iconbitmap(r"C:\\Users\\mike2\\Desktop\\seminario\\icono.ico")

    global nombreusuario_entry
    global contrasena_entry

    nombreusuario_entry=StringVar()
    contrasena_entry=StringVar()

    Label(pantalla2, text="Por Favor elige un \n Usuario y una Contraseña", bg="black", fg="white",width="300", height="2", font=("Calibri", 15)).pack()
    Label(pantalla2, text="").pack()

    Label(pantalla2, text="Usuario").pack()
    nombreusuario_entry= Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Contraseña").pack()
    contrasena_entry= Entry(pantalla2,show="*")
    contrasena_entry.pack()
    Label(pantalla2).pack()

    inic4 = tkinter.Button(pantalla2, text="Registrar ", width=30, height=2, bg="yellow", fg="black", borderwidth=5,relief="raised",command=inserta_datos)
    inic4.place(x=45, y=225)

#incertar datos  a BD

def inserta_datos():
    bd = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )




    fcursor=bd.cursor()
    sql="INSERT INTO login (usuario, contrasena) VALUES ('{0}', '{1}')".format(nombreusuario_entry.get(), contrasena_entry.get())
    try:
              fcursor.execute(sql)
              bd.commit()
              messagebox.showinfo(message="Registro Exitoso", title="Aviso")

    except:
                bd.rollback()
                messagebox.showinfo(message="No registrado", title="Aviso")
    bd.close()


# Validar datos ingresados

def validacion_datos():
    bd = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
        )
    fcursor=bd.cursor()


    fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+nombreusuario_verify.get()+"'and contrasena='"+contrasenausuario_verify.get()+"'")
    if fcursor.fetchall():
        messagebox.showinfo(title="Inicio de Sesion correcto", message="Usuario y Contraseña correcta")
        #pygame.mixer.music.play()
        pantalla.destroy()
        global pantalla3
        pantalla3 = Tk()
        pantalla3.geometry("1000x500")
        pantalla3.resizable(0, 0)
        pantalla3.title("TOTALSPEED")
        pantalla3.iconbitmap(r"C:\\Users\\mike2\\Desktop\\seminario\\icono.ico")
        imagen = PhotoImage(file="fondo.png")
        fondo = Label(pantalla3, image=imagen).place(x=-40, y=-50)

        etiqueta = tkinter.Label(pantalla3, text="TOTALSPEED", bg="black", fg="yellow", font="DFPOP1-W9 30")
        etiqueta.pack(fill=tkinter.X)
        image2 = PhotoImage(file="logo.png")
        image2 = image2.subsample(1, 1)
        label = Label(image=image2).place(x=375, y=70)

        image3 = PhotoImage(file="images.png")
        image3 = image3.subsample(2, 2)
        label = Label(image=image3).place(x=20, y=380)
        etiqueta4 =tkinter.Label(pantalla3, text ="Elaborado para: Ceramica Santa Maria",bg="black",fg="white",font="DFPOP1-W9 10")
        etiqueta4.place(x=140, y=480)




                #LasOpcionesdelosbotones
        def temp():
            resultado = MessageBox.askquestion("Temporales",
                                       "¿Está seguro que desea borrar Archivos temporales?")
            if resultado == "yes":
                # FOLDER2
                folder2 = 'C:\Windows\Temp'
                for the_file in os.listdir(folder2):
                    file_path = os.path.join(folder2, the_file)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                        # elif os.path.isdir(file_path): shutil.rmtree(file_path)
                    except Exception as e:
                        print("Tu Computadora esta siendo optimizada")
                # FOLDER3
                folder3 = 'C:\\Users\\mike2\\AppData\\Local\\Temp'
                for the_file in os.listdir(folder3):
                    file_path = os.path.join(folder3, the_file)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                        # elif os.path.isdir(file_path): shutil.rmtree(file_path)
                    except Exception as e:
                        print("Tu Computadora esta siendo optimizada")
                        messagebox.showinfo(message="Genial!!! La Tarea Fue exitosa", title="Tarea Finzalizada")

        def prefe():
            resultado2 = MessageBox.askquestion("Prefetch",
                                                "¿Está seguro que desea borrar Prefetch ? (Recomendable no hacerlo tan seguido)")
            if resultado2 == "yes":
                # FOLDER1
                folder = 'C:\Windows\Prefetch'
                for the_file in os.listdir(folder):
                    file_path = os.path.join(folder, the_file)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                        # elif os.path.isdir(file_path): shutil.rmtree(file_path)
                    except Exception as e:
                        print(chr(27) + "[3;37m" + "Tu Computadora esta siendo optimizada.......")
                        messagebox.showinfo(message="Genial!!! La Tarea Fue exitosa", title="Tarea Finzalizada")




        def serv():
            resultado3 = MessageBox.askquestion("Servicios",
                                                "¿Esta seguro que desea deshabilitar Servicios poco usados?")
            if resultado3 == "yes":
                os.system('net stop wuauserv')
                os.system('sc config wuauserv start= disabled')
                messagebox.showinfo(message="Genial!!! La Tarea Fue exitosa", title="Tarea Finzalizada")

        def ac():
            resultado4 = MessageBox.askquestion("Aceleración Completa",
                                                "¿Esta seguro que desea una Aceleración Completa?")
            if resultado4 == "yes":
                os.system('net stop wuauserv')
                os.system('sc config wuauserv start= disabled')
                # FOLDER1
                folder = 'C:\Windows\Prefetch'
                for the_file in os.listdir(folder):
                    file_path = os.path.join(folder, the_file)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                        # elif os.path.isdir(file_path): shutil.rmtree(file_path)
                    except Exception as e:
                        print(chr(27) + "[3;37m" + "Tu Computadora esta siendo optimizada.......")
                # FOLDER2
                folder2 = 'C:\Windows\Temp'
                for the_file in os.listdir(folder2):
                    file_path = os.path.join(folder2, the_file)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                        # elif os.path.isdir(file_path): shutil.rmtree(file_path)
                    except Exception as e:

                        # FOLDER3
                        folder3 = 'C:\\Users\\mike2\\AppData\\Local\\Temp'
                        for the_file in os.listdir(folder3):
                            file_path = os.path.join(folder3, the_file)
                            try:
                                if os.path.isfile(file_path):
                                    os.unlink(file_path)
                                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
                            except Exception as e:
                                print(chr(27) + "[3;37m" + "Tu Computadora esta siendo optimizada.......")
                                messagebox.showinfo(message="Genial!!! La Tarea Fue exitosa", title="Tarea Finzalizada")



        def em():

                    print(psutil.cpu_percent())
                    print(psutil.virtual_memory())  # physical memory usage
                    print('Porcentaje en Uso:', psutil.virtual_memory()[2])
                    a = psutil.virtual_memory()[2]

                    if a>50:
                        etiqueta3 =tkinter.Label(pantalla3, text =f'El porcentaje de uso es :  {a} %',bg="black",fg="red",font="DFPOP1-W9 10")
                        etiqueta3.place(x=755, y=280)

                    else:
                        etiqueta3 =tkinter.Label(pantalla3, text =f'El porcentaje de uso es :  {a} %',bg="black",fg="green",font="DFPOP1-W9 10")
                        etiqueta3.place(x=755, y=280)





                    




        inic5 = tkinter.Button(pantalla3, text="Eliminar Archivos Basura ", command=temp, width=30, height=2, bg="yellow", fg="black", borderwidth=5, relief="raised")
        inic5.place(x=45, y=130)

        inic6 = tkinter.Button(pantalla3, text="Optimizar Memoria Ram ", command=prefe, width=30, height=2, bg="yellow", fg="black", borderwidth=5, relief="raised")
        inic6.place(x=45, y=210)

        inic7 = tkinter.Button(pantalla3, text="Deshabilitar Servicios Innecesarios ", command=serv, width=30, height=2, bg="yellow", fg="black", borderwidth=5, relief="raised")
        inic7.place(x=755, y=130)

        inic8 = tkinter.Button(pantalla3, text="Aceleración Completa ", command=ac, width=30, height=2, bg="black", fg="yellow", borderwidth=5, relief="raised")
        inic8.place(x=395, y=360)

        inic9 = tkinter.Button(pantalla3, text="Ver Estado de Memoria ", command=em, width=30, height=2, bg="white", fg="black", borderwidth=5, relief="raised")
        inic9.place(x = 755, y = 210)

        today = date.today()
        now = datetime.now()
        etiqueta2 =tkinter.Label(pantalla3, text =f'Fecha: {today}',bg="black",fg="yellow",font="DFPOP1-W9 10")
        etiqueta2.place(x=0, y=50)










        pantalla3.mainloop()


    else:
        messagebox.showinfo(title="Inicio de Sesion Incorrecto", message="Credenciales Invalidas")
menu_pantalla()






