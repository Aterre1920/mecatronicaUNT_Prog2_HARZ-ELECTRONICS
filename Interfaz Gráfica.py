import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox as MessageBox
from ControlPostgres import *
import webbrowser
from datetime import datetime

class Supervisor():
    
    def __init__(self,usuario,contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
     
    def actualizar_cantidad(self,producto,cantidad):
        try:
            update_cantidad(producto,cantidad)
            MessageBox.showinfo("", f"Cantidad de {producto} actualizada correctamente")
        except:
            MessageBox.showerror("", "Datos inválidos")
    
    def actualizar_precio(self,producto,precio):
        try:
            update_precio(producto,precio)
            MessageBox.showinfo("", f"Precio de {producto} actualizada correctamente")
        except:
            MessageBox.showerror("", "Datos inválidos")
        
    def agregar_vendedores(self,vendedor,contraseña,venta,comision):
        add_vendedores(vendedor,contraseña,venta,comision)
     
    def eliminar_vendedores(self,vendedor):
        try:
            delete_vendedores(vendedor)
            MessageBox.showinfo("", f"{vendedor} eliminado correctamente")
        except:
            MessageBox.showerror("", "Dato inválido")
        
class Vendedor():
    
    def __init__(self,nombre,contra):
        self.nombre = nombre
        self.contra = contra
        vendedores.append([self.nombre,self.contra])

SUPER = Supervisor("SUPER1","jefe")
headers = ["PRODUCTOS","CANT.","PRECIO UNIT."]
vendedores = extraer_vendedor()

try:
    Crear_tablas()
    add_vendedores('JOSE','1234',0,0)
    vendedores = extraer_vendedor()
    insert_productos('Arduino UNO',30,30.0)
    insert_productos('Capacitor',150,1.5)
    insert_productos('LDR',150,3.0)
    insert_productos('LED',500,0.2)
    insert_productos('Potenciometro',350,1.0)
    insert_productos('Resistor',200,0.5)
    insert_productos('Servomotor',50,25.0)
    insert_productos('Transistor',250,5.0)
    insert_productos('Triac',100,2.5)
except:
    print("Operaciones realizadas con anterioridad")

def Tabla(ps1):
    inventario = visualizar_productos()
    espaciol = tk.Label(ps1,text="               ",bg="#d9d9d9").grid(row=2,column=1)
    tee = tk.Label(ps1,text="       INVENTARIO:",bg="#d9d9d9",font=("Bahnschrift Light",14,'bold')).grid(row=2,column=1,columnspan=5,pady=10,padx=50)
            
    for i in range(3):
        b = tk.Entry(ps1)
        b.insert(0,headers[i])
        b.config(font=("Times New Roman", 11,"bold"))
        b.config(justify="center")
        if i!=0:
            b.config(width=14)
        b.config(state="readonly")
        b.grid(row=3 ,column= i+2)
    
    for i in range(9):
        b = tk.Entry(ps1)
        b.insert(0,inventario[i][0])
        b.config(font=("Times New Roman", 11,"bold","italic"))
        b.config(state="readonly")
        b.grid(row=i+4 ,column= 2)
    
    for i in range(9):
        b = tk.Entry(ps1)
        b.insert(0,inventario[i][1])
        b.config(font=("Times New Roman", 11,"italic"))
        b.config(justify="right")
        b.config(width=14)
        b.config(state="readonly")
        b.grid(row=i+4 ,column= 3)
    
    for i in range(9):
        b = tk.Entry(ps1)
        b.insert(0,inventario[i][2])
        b.config(font=("Times New Roman", 11,"italic"))
        b.config(justify="right")
        b.config(width=14)
        b.config(state="readonly")
        b.grid(row=i+4 ,column= 4)
        
    return inventario

class Log_sup():
    
    def __init__(self):
        
        self.ventana_superv()
        self.Super()
    
    def ventana_superv(self):
        
        self.Login_sup = tk.Toplevel()
        self.Login_sup.title("LOGIN SUPERVISOR")
        self.Login_sup.geometry("245x150")
        self.Login_sup.config(bg="#d9d9d9")
        self.Login_sup.resizable(False,False)
        self.Login_sup.iconbitmap('Imagenes/unt.ico')
                
        self.Ind = tk.Label(self.Login_sup,bg="#d9d9d9",text = "Introduzca usuario y contraseña", font = ("Bahnschrift Light",11), fg = "black")
        self.Ind.place(x = 15, y = 10)
        self.Us1 = tk.Label(self.Login_sup,bg="#d9d9d9",text = "USUARIO:",font = ("Bahnschrift Light",11,'bold'), fg = "black")
        self.Us1.place(x = 20, y = 40)
        self.Us2 = tk.Entry(self.Login_sup, state = 'normal',font = ("Bahnschrift Light",11,'italic'), width = 10)
        self.Us2.place(x = 140, y = 40)
        self.Us2.bind('<Return>', self.Enter1)
        self.Con1 = tk.Label(self.Login_sup,bg="#d9d9d9",text = "CONTRASEÑA:",font = ("Bahnschrift Light",11,'bold'), fg = "black")
        self.Con1.place(x = 20, y = 70)
        self.Con2 = tk.Entry(self.Login_sup, show ='*', state = 'normal',font = ("Bahnschrift Light",11), width = 10)
        self.Con2.place(x = 140, y = 70)
        self.Con2.bind('<Return>', self.Enter1)
        self.Ingresar = tk.Button(self.Login_sup, width = 8, height = 1, bg = "blue", text = "INGRESAR", font = ("Berlin Sans FB Demi", 12, "bold"), fg = "#FFFFFF",  borderwidth = 2.3,command = self.Super)
        self.Ingresar.place(x = 75, y = 105)
        self.Login_sup.mainloop()
    
    def Enter1(self,event):
        self.Super()
    
    def Super(self):
        
        if ((self.Us2.get() == SUPER.usuario) and (self.Con2.get() == SUPER.contraseña)):
            
            self.Login_sup.destroy()
            
            Super = tk.Toplevel()
            Super.title("Interfaz Supervisor")
            Super.geometry("500x325")
            Super.resizable(False,False)
            Super.iconbitmap('Imagenes/unt.ico')
            
            style = ttk.Style()
            settings = {"TNotebook.Tab": {"configure": {"padding": [5, 1],
                                            "background": "#BACAD3",
                                            "font": ("Bahnschrift Light",10)
                                           },
                              "map": {"background": [("selected", "#124BD8"),
                                                     ("active","#62B3DD")],
                                      "foreground": [("selected", "#ffffff"),
                                                     ("active", "#000000")]

                                     }
                              }
            }      

            style.theme_create("mi_estilo", parent="alt", settings=settings)
            style.theme_use("mi_estilo")
            
            panel1 = ttk.Notebook(Super)
            panel1.pack(fill = 'both', expand = 'yes')
            
            ps1 = ttk.Frame(panel1)
            ps2 = ttk.Frame(panel1)
            ps3 = ttk.Frame(panel1)
            
            #PESTAÑA VISUALIZAR
            Tabla(ps1)
            
            #PESTAÑA ACTUALIZAR PRODUCTOS
            #actualización de cantidades
            def actu_cant():
                producto = prod_e.get()
                cantidad = cant_e.get()
                prod_e.delete(0,'end')
                cant_e.delete(0,'end')
                SUPER.actualizar_cantidad(producto,cantidad)
                Tabla(ps1)
                
            frame1 = tk.LabelFrame(ps2,text="Actualizar cantidades de productos:",bg="#d9d9d9",font = ("Bahnschrift Light",11,'bold'))
            frame1.grid(row=1,column=1, columnspan=2, padx=100, pady=10)
            prod_l = tk.Label(frame1,text="Producto:",bg="#d9d9d9",font = ("Bahnschrift Light",11))
            prod_l.grid(row=1,column=1,padx=10)
            prod_e = tk.Entry(frame1,state='normal',width=15,font = ("Bahnschrift Light",11,'italic'))
            prod_e.grid(row=1,column=2,pady=5)
            cant_l = tk.Label(frame1,text="Nueva Cantidad:",bg="#d9d9d9",font = ("Bahnschrift Light",11))
            cant_l.grid(row=3,column=1,padx=12)
            cant_e = tk.Entry(frame1,state='normal',width=15,font = ("Bahnschrift Light",11,'italic'))
            cant_e.grid(row=3,column=2,pady=5)
            cant_b = tk.Button(frame1,width = 10, height = 1, bg = "blue", text = "ACTUALIZAR", font = ("Berlin Sans FB Demi", 10, "bold"), fg = "#FFFFFF",  borderwidth = 2.3,command=actu_cant)
            cant_b.grid(row=4,column=1,columnspan=2,pady=10)
            
            #actualizacion de precios
            def actu_prec():
                producto = produ_e.get()
                precio = prec_e.get()
                produ_e.delete(0,'end')
                prec_e.delete(0,'end')
                SUPER.actualizar_precio(producto,precio)
                Tabla(ps1)
            
            frame2 = tk.LabelFrame(ps2,text="Actualizar precios de productos:",bg="#d9d9d9",font = ("Bahnschrift Light",11,'bold'))
            frame2.grid(row=2,column=1,columnspan=2, padx=130, pady=5)
            produ_l = tk.Label(frame2,text="Producto:",bg="#d9d9d9",font = ("Bahnschrift Light",11))
            produ_l.grid(row=1,column=1)
            produ_e = tk.Entry(frame2,state='normal',width=15,font = ("Bahnschrift Light",11,'italic'))
            produ_e.grid(row=1,column=2,pady=5)
            prec_l = tk.Label(frame2,text="Nuevo Precio:",bg="#d9d9d9",font = ("Bahnschrift Light",11))
            prec_l.grid(row=3,column=1,padx=10)
            prec_e = tk.Entry(frame2,state='normal',width=15,font = ("Bahnschrift Light",11,'italic'))
            prec_e.grid(row=3,column=2,pady=5)
            prec_b = tk.Button(frame2,width = 10, height = 1, bg = "blue", text = "ACTUALIZAR", font = ("Berlin Sans FB Demi", 10, "bold"), fg = "#FFFFFF",  borderwidth = 2.3,command=actu_prec)
            prec_b.grid(row=4,column=1,columnspan=2,pady=10)
            
            #PESTAÑA ACTUALIZAR VENDEDORES
            def agre_vend():
                try:
                    nombre = nomb_e.get()
                    contra = contr_e.get()
                    a = len(nombre)
                    b = len(contra)
                    c=(1/a)+(1/b)
                    nomb_e.delete(0,'end')
                    contr_e.delete(0,'end')
                    SUPER.agregar_vendedores(nombre,contra,0,0)
                    nombre1 = Vendedor(nombre,contra)
                    MessageBox.showinfo("", f"{nombre} agregado correctamente")
                except:
                    MessageBox.showerror("", "Datos inválidos")
                
            frame3 = tk.LabelFrame(ps3,text="Agregar vendedor:",bg="#d9d9d9",font = ("Bahnschrift Light",11,'bold'))
            frame3.grid(row=1,column=1, columnspan=2, padx=150, pady=10)
            nomb_l = tk.Label(frame3,text="Nombre:",bg="#d9d9d9",font = ("Bahnschrift Light",11))
            nomb_l.grid(row=1,column=1,padx=3)
            nomb_e = tk.Entry(frame3,state='normal',width=15,font = ("Bahnschrift Light",11,'italic'))
            nomb_e.grid(row=1,column=2,pady=5,padx=5)
            contr_l = tk.Label(frame3,text="Contraseña:",bg="#d9d9d9",font = ("Bahnschrift Light",11))
            contr_l.grid(row=3,column=1)
            contr_e = tk.Entry(frame3,state='normal',width=15,show='*',font = ("Bahnschrift Light",11,'italic'))
            contr_e.grid(row=3,column=2,pady=5)
            agre_b = tk.Button(frame3,width = 8, height = 1, bg = "blue", text = "AGREGAR", font = ("Berlin Sans FB Demi", 10, "bold"), fg = "#FFFFFF",  borderwidth = 2.3,command=agre_vend)
            agre_b.grid(row=4,column=1,columnspan=2,pady=10)
            
            def elim_vend():
                nombre = nombre_e.get()
                nombre_e.delete(0,'end')
                SUPER.eliminar_vendedores(nombre)
            
            frame4 = tk.LabelFrame(ps3,text="Eliminar vendedor:",bg="#d9d9d9",font = ("Bahnschrift Light",11,'bold'))
            frame4.grid(row=2,column=1,columnspan=2, padx=140, pady=10)
            nombre_l = tk.Label(frame4,text="Nombre:",bg="#d9d9d9",font = ("Bahnschrift Light",11))
            nombre_l.grid(row=1,column=1,padx=5)
            nombre_e = tk.Entry(frame4,state='normal',width=12,font = ("Bahnschrift Light",11,'italic'))
            nombre_e.grid(row=1,column=2,pady=5,padx=5)
            elim_b = tk.Button(frame4,width = 9, height = 1, bg = "#DE433A", text = "ELIMINAR", font = ("Berlin Sans FB Demi", 10, "bold"), fg = "#FFFFFF",  borderwidth = 2.3,command=elim_vend)
            elim_b.grid(row=4,column=1,columnspan=2,pady=10)
            
            panel1.add(ps1, text = "  Visualizar Inventario   ")
            panel1.add(ps2, text = "  Actualizar Productos   ")
            panel1.add(ps3, text = "  Agregar/Eliminar Vendedores   ")           
        else:
            self.Us2.delete("0","end")
            self.Con2.delete("0","end")
            MessageBox.showerror("ERROR AL LOGEAR", "Usuario y/o contraseña inválidos")
  
class Log_vent():
    
    def __init__(self):
        
        self.ventana_vend()
        self.Vende()
        self.imprimir()
        
    def ventana_vend(self):
        
        self.Login_ven = tk.Toplevel()
        self.Login_ven.title("LOGIN VENDEDOR")
        self.Login_ven.geometry("250x150")
        self.Login_ven.config(bg="#d9d9d9") 
        self.Login_ven.resizable(False,False)
        self.Login_ven.iconbitmap('Imagenes/unt.ico')
    
        self.Ind = tk.Label(self.Login_ven,bg="#d9d9d9",text = "Introduzca usuario y contraseña", font = ("Bahnschrift Light",11), fg = "black")
        self.Ind.place(x = 20, y = 10)
        self.Us11 = tk.Label(self.Login_ven,bg="#d9d9d9",text = "USUARIO:",font = ("Bahnschrift Light",11,'bold'), fg = "black")
        self.Us11.place(x = 20, y = 40)
        self.Us22 = tk.Entry(self.Login_ven, state = 'normal',font = ("Bahnschrift Light",11,'italic'), width = 11)
        self.Us22.place(x = 140, y = 40)
        self.Us22.bind('<Return>', self.Enter2)
        self.Con11 = tk.Label(self.Login_ven,bg="#d9d9d9",text = "CONTRASEÑA:",font = ("Bahnschrift Light",11,'bold'), fg = "black")
        self.Con11.place(x = 20, y = 70)
        self.Con22 = tk.Entry(self.Login_ven, show ='*', state = 'normal',font = ("Bahnschrift Light",11), width = 11)
        self.Con22.place(x = 140, y = 70)
        self.Con22.bind('<Return>', self.Enter2)
        self.Ingresar1 = tk.Button(self.Login_ven, width = 8, height = 1, bg = "blue", text = "INGRESAR", font = ("Berlin Sans FB Demi", 12, "bold"), fg = "#FFFFFF",  borderwidth = 2.3, command = self.Vende)
        self.Ingresar1.place(x = 75, y = 105)
        self.Login_ven.mainloop()
    
    def Enter2(self,event):
        self.Vende()
    
    def Vende(self):
               
        for i in range(len(vendedores)):
            if ((self.Us22.get() == vendedores[i][0]) and (self.Con22.get() == vendedores[i][1])):
                
                vendedor = self.Us22.get()
                
                self.Login_ven.destroy()
                
                Log_venta(vendedor)
                
                break
        else:
            self.Us22.delete("0","end")
            self.Con22.delete("0","end")
            MessageBox.showerror("ERROR AL LOGEAR", "Usuario y/o contraseña inválidos")
    
class Log_venta(Log_vent):
    
    def __init__(self,vendedor):
        self.vendedor = vendedor
        self.pantallaventa()
        
    def pantallaventa(self):
        #ventana principal
        self.venta = tk.Toplevel()
        self.venta.title("Interfaz Vendedor")
        self.venta.geometry("1040x660")
        self.venta.resizable(False,False)
        self.venta.config(bg="#d9d9d9")
        self.venta.iconbitmap('Imagenes/unt.ico')
        self.inventario = visualizar_productos()
        self.Inven = {}
        self.Carrito = {}
        self.cont = [1,1,1,1,1,1,1,1,1]
        self.n = 0
        
        for i in range(len(self.inventario)):
            self.Inven[self.inventario[i][0]] = [self.inventario[i][1],float(self.inventario[i][2])]

        #LabelFrame de datos de usuarios:
        self.frame_usuario = tk.LabelFrame(self.venta, text="DATOS DEL COMPRADOR",bg="#d9d9d9",font=("Bahnschrift Light",11,"bold"))
        self.frame_usuario.grid(row=2,column=1, padx=30, pady=1)
        self.espacio1 = tk.Label(self.frame_usuario, text='     ',bg="#d9d9d9").grid(row=1,column=1)
        self.nom_comp1 = tk.Label(self.frame_usuario,bg="#d9d9d9", text="Nombres y apellidos: ",font=("Bahnschrift Light",11,"bold")).grid(row=1,column=2)
        self.nom_comp2 = tk.Entry(self.frame_usuario, font=("Bahnschrift Light",11),state='normal',width=30)
        self.nom_comp2.grid(row=1,column=3,pady=3)
        self.espacio2 = tk.Label(self.frame_usuario, text='     ',bg="#d9d9d9").grid(row=1,column=4)
        self.dni_1 = tk.Label(self.frame_usuario,bg="#d9d9d9" ,text= 'DNI: ', font=("Bahnschrift Light",11,"bold")).grid(row=1,column=5)
        self.dni_2 = tk.Entry(self.frame_usuario, font=("Bahnschrift Light",11),state='normal',width=10)
        self.dni_2.grid(row=1,column=6,pady=3)
        self.espacio3 = tk.Label(self.frame_usuario,bg="#d9d9d9", text='     ').grid(row=1,column=7)
        self.direccion1 = tk.Label(self.frame_usuario, bg="#d9d9d9",text="Dirección: ",font=("Bahnschrift Light",11,"bold")).grid(row=2,column=2)
        self.direccion2 = tk.Entry(self.frame_usuario, font=("Bahnschrift Light",11),state='normal',width=33)
        self.direccion2.grid(row=2,column=3,columnspan=2,pady=3)

        #LabelFrame de productos:
        self.frame_productos = tk.LabelFrame(self.venta, text="PRODUCTOS",bg="#d9d9d9",font=("Bahnschrift Light",11,"bold"))
        self.frame_productos.grid(row=3,column=1,padx=30,pady=5)
        #frame de potenciometro: 
        self.frame_pot = tk.LabelFrame(self.frame_productos, text="Potenciometro",bg="#d9d9d9",font=("Bahnschrift Light",11,"bold","italic"))
        self.frame_pot.grid(row=1,column=1)
        self.pot_imagen = PhotoImage(file="Imagenes/pot.png").subsample(3)
        self.pot_imagen1 = tk.Label(self.frame_pot,bg="#d9d9d9", image=self.pot_imagen).grid(row=1,column=1,rowspan=3)
        self.pot_disp_num = "Disponibles: {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Potenciometro')][0])
        self.pot_disp = tk.Label(self.frame_pot,bg="#d9d9d9",text=self.pot_disp_num,font=("Bahnschrift Light",11))
        self.pot_disp.grid(row=1,column=2,columnspan=2)
        self.pot_unit_num = "Precio Unit.: S/. {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Potenciometro')][1])
        self.pot_unit = tk.Label(self.frame_pot,bg="#d9d9d9",text=self.pot_unit_num,font=("Bahnschrift Light",11))
        self.pot_unit.grid(row=2,column=2,columnspan=2)
        self.pot_comp = tk.Label(self.frame_pot,bg="#d9d9d9",text='Cantidad:',font=("Bahnschrift Light",11)).grid(row=4,column=1)
        self.pot_comp1 = tk.Entry(self.frame_pot,font=("Bahnschrift Light",11),state='normal',width=6)
        self.pot_comp1.grid(row=4,column=2)
        self.pot_bot = tk.Button(self.frame_pot,text="AÑADIR AL CARRITO",bg='#1A52E0',fg='white',font = ("Berlin Sans FB Demi", 11, "bold"),command=self.AñadirPot).grid(row=6,column=1,columnspan=2,padx=40,pady=8)
        #frame de resistencia:
        self.frame_res = tk.LabelFrame(self.frame_productos,bg="#d9d9d9", text="Resistor",font=("Bahnschrift Light",11,"bold","italic"))
        self.frame_res.grid(row=1,column=2)
        self.res_imagen = PhotoImage(file="Imagenes/res.png").subsample(3)
        self.res_imagen1 = tk.Label(self.frame_res,bg="#d9d9d9", image=self.res_imagen).grid(row=1,column=1,rowspan=3)
        self.res_disp_num = "Disponibles: {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Resistor')][0])
        self.res_disp = tk.Label(self.frame_res,bg="#d9d9d9",text=self.res_disp_num,font=("Bahnschrift Light",11))
        self.res_disp.grid(row=1,column=2,columnspan=2)
        self.res_unit_num = "Precio Unit.: S/. {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Resistor')][1])
        self.res_unit = tk.Label(self.frame_res,bg="#d9d9d9",text=self.res_unit_num,font=("Bahnschrift Light",11))
        self.res_unit.grid(row=2,column=2,columnspan=2)
        self.res_comp = tk.Label(self.frame_res,bg="#d9d9d9",text='Cantidad:',font=("Bahnschrift Light",11)).grid(row=4,column=1)
        self.res_comp1 = tk.Entry(self.frame_res,font=("Bahnschrift Light",11),state='normal',width=6)
        self.res_comp1.grid(row=4,column=2)
        self.res_bot = tk.Button(self.frame_res,text="AÑADIR AL CARRITO",bg='#1A52E0',fg='white',font = ("Berlin Sans FB Demi", 11, "bold"),command=self.AñadirRes).grid(row=6,column=1,columnspan=2,padx=40,pady=8)
        #frame de arduino:
        self.frame_ard = tk.LabelFrame(self.frame_productos,bg="#d9d9d9", text="Arduino UNO",font=("Bahnschrift Light",11,"bold","italic"))
        self.frame_ard.grid(row=1,column=3)
        self.ard_imagen = PhotoImage(file="Imagenes/ard.png").subsample(3)
        self.ard_imagen1 = tk.Label(self.frame_ard,bg="#d9d9d9", image=self.ard_imagen).grid(row=1,column=1,rowspan=3)
        self.ard_disp_num = "Disponibles: {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Arduino UNO')][0])
        self.ard_disp = tk.Label(self.frame_ard,bg="#d9d9d9",text=self.ard_disp_num,font=("Bahnschrift Light",11))
        self.ard_disp.grid(row=1,column=2,columnspan=2)
        self.ard_unit_num = "Precio Unit.: S/. {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Arduino UNO')][1])
        self.ard_unit = tk.Label(self.frame_ard,bg="#d9d9d9",text=self.ard_unit_num,font=("Bahnschrift Light",11))
        self.ard_unit.grid(row=2,column=2,columnspan=2)
        self.ard_comp = tk.Label(self.frame_ard,bg="#d9d9d9",text='Cantidad:',font=("Bahnschrift Light",11)).grid(row=4,column=1)
        self.ard_comp1 = tk.Entry(self.frame_ard,font=("Bahnschrift Light",11),state='normal',width=6)
        self.ard_comp1.grid(row=4,column=2)
        self.ard_bot = tk.Button(self.frame_ard,text="AÑADIR AL CARRITO",bg='#1A52E0',fg='white',font = ("Berlin Sans FB Demi", 11, "bold"),command=self.AñadirArd).grid(row=6,column=1,columnspan=2,padx=40,pady=8)
        #frame de condensador
        self.frame_cap = tk.LabelFrame(self.frame_productos,bg="#d9d9d9", text="Capacitor",font=("Bahnschrift Light",11,"bold","italic"))
        self.frame_cap.grid(row=2,column=1)
        self.cap_imagen = PhotoImage(file="Imagenes/cap.png").subsample(3)
        self.cap_imagen1 = tk.Label(self.frame_cap,bg="#d9d9d9", image=self.cap_imagen).grid(row=1,column=1,rowspan=3)
        self.cap_disp_num = "Disponibles: {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Capacitor')][0])
        self.cap_disp = tk.Label(self.frame_cap,bg="#d9d9d9",text=self.cap_disp_num,font=("Bahnschrift Light",11))
        self.cap_disp.grid(row=1,column=2,columnspan=2)
        self.cap_unit_num = "Precio Unit.: S/. {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Capacitor')][1])
        self.cap_unit = tk.Label(self.frame_cap,bg="#d9d9d9",text=self.cap_unit_num,font=("Bahnschrift Light",11))
        self.cap_unit.grid(row=2,column=2,columnspan=2)
        self.cap_comp = tk.Label(self.frame_cap,bg="#d9d9d9",text='Cantidad:',font=("Bahnschrift Light",11)).grid(row=4,column=1)
        self.cap_comp1 = tk.Entry(self.frame_cap,font=("Bahnschrift Light",11),state='normal',width=6)
        self.cap_comp1.grid(row=4,column=2)
        self.cap_bot = tk.Button(self.frame_cap,text="AÑADIR AL CARRITO",bg='#1A52E0',fg='white',font = ("Berlin Sans FB Demi", 11, "bold"),command=self.AñadirCap).grid(row=6,column=1,columnspan=2,padx=40,pady=8)
        #frame de LDR
        self.frame_ldr = tk.LabelFrame(self.frame_productos,bg="#d9d9d9", text="LDR",font=("Bahnschrift Light",11,"bold","italic"))
        self.frame_ldr.grid(row=2,column=2)
        self.ldr_imagen = PhotoImage(file="Imagenes/ldr.png").subsample(3)
        self.ldr_imagen1 = tk.Label(self.frame_ldr,bg="#d9d9d9", image=self.ldr_imagen).grid(row=1,column=1,rowspan=3)
        self.ldr_disp_num = "Disponibles: {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('LDR')][0])
        self.ldr_disp = tk.Label(self.frame_ldr,bg="#d9d9d9",text=self.ldr_disp_num,font=("Bahnschrift Light",11))
        self.ldr_disp.grid(row=1,column=2,columnspan=2)
        self.ldr_unit_num = "Precio Unit.: S/. {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('LDR')][1])
        self.ldr_unit = tk.Label(self.frame_ldr,bg="#d9d9d9",text=self.ldr_unit_num,font=("Bahnschrift Light",11))
        self.ldr_unit.grid(row=2,column=2,columnspan=2)
        self.ldr_comp = tk.Label(self.frame_ldr,bg="#d9d9d9",text='Cantidad:',font=("Bahnschrift Light",11)).grid(row=4,column=1)
        self.ldr_comp1 = tk.Entry(self.frame_ldr,font=("Bahnschrift Light",11),state='normal',width=6)
        self.ldr_comp1.grid(row=4,column=2)
        self.ldr_bot = tk.Button(self.frame_ldr,text="AÑADIR AL CARRITO",bg='#1A52E0',fg='white',font = ("Berlin Sans FB Demi", 11, "bold"),command=self.AñadirLDR).grid(row=6,column=1,columnspan=2,padx=40,pady=8)
        #frame de LED
        self.frame_led = tk.LabelFrame(self.frame_productos,bg="#d9d9d9", text="LED",font=("Bahnschrift Light",11,"bold","italic"))
        self.frame_led.grid(row=2,column=3)
        self.led_imagen = PhotoImage(file="Imagenes/led.png").subsample(3)
        self.led_imagen1 = tk.Label(self.frame_led,bg="#d9d9d9", image=self.led_imagen).grid(row=1,column=1,rowspan=3)
        self.led_disp_num = "Disponibles: {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('LED')][0])
        self.led_disp = tk.Label(self.frame_led,bg="#d9d9d9",text=self.led_disp_num,font=("Bahnschrift Light",11))    
        self.led_disp.grid(row=1,column=2,columnspan=2)
        self.led_unit_num = "Precio Unit.: S/. {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('LED')][1])
        self.led_unit = tk.Label(self.frame_led,bg="#d9d9d9",text=self.led_unit_num,font=("Bahnschrift Light",11))
        self.led_unit.grid(row=2,column=2,columnspan=2)
        self.led_comp = tk.Label(self.frame_led,bg="#d9d9d9",text='Cantidad:',font=("Bahnschrift Light",11)).grid(row=4,column=1)
        self.led_comp1 = tk.Entry(self.frame_led,font=("Bahnschrift Light",11),state='normal',width=6)
        self.led_comp1.grid(row=4,column=2)
        self.led_bot = tk.Button(self.frame_led,text="AÑADIR AL CARRITO",bg='#1A52E0',fg='white',font = ("Berlin Sans FB Demi", 11, "bold"),command=self.AñadirLED).grid(row=6,column=1,columnspan=2,padx=40,pady=8)
        #frame de servo
        self.frame_ser = tk.LabelFrame(self.frame_productos,bg="#d9d9d9", text="Servomotor",font=("Bahnschrift Light",11,"bold","italic"))
        self.frame_ser.grid(row=3,column=1)
        self.ser_imagen = PhotoImage(file="Imagenes/servo.png").subsample(3)
        self.ser_imagen1 = tk.Label(self.frame_ser, bg="#d9d9d9",image=self.ser_imagen).grid(row=1,column=1,rowspan=3)
        self.ser_disp_num = "Disponibles: {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Servomotor')][0])
        self.ser_disp = tk.Label(self.frame_ser,bg="#d9d9d9",text=self.ser_disp_num,font=("Bahnschrift Light",11))
        self.ser_disp.grid(row=1,column=2,columnspan=2)
        self.ser_unit_num = "Precio Unit.: S/. {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Servomotor')][1])
        self.ser_unit = tk.Label(self.frame_ser,bg="#d9d9d9",text=self.ser_unit_num,font=("Bahnschrift Light",11))
        self.ser_unit.grid(row=2,column=2,columnspan=2)
        self.ser_comp = tk.Label(self.frame_ser,bg="#d9d9d9",text='Cantidad:',font=("Bahnschrift Light",11)).grid(row=4,column=1)
        self.ser_comp1 = tk.Entry(self.frame_ser,font=("Bahnschrift Light",11),state='normal',width=6)
        self.ser_comp1.grid(row=4,column=2)
        self.ser_bot = tk.Button(self.frame_ser,text="AÑADIR AL CARRITO",bg='#1A52E0',fg='white',font = ("Berlin Sans FB Demi", 11, "bold"),command=self.AñadirSer).grid(row=6,column=1,columnspan=2,padx=40,pady=8)
        #frame de transistor
        self.frame_tra = tk.LabelFrame(self.frame_productos,bg="#d9d9d9", text="Transistor",font=("Bahnschrift Light",11,"bold","italic"))
        self.frame_tra.grid(row=3,column=2)
        self.tra_imagen = PhotoImage(file="Imagenes/tran.png").subsample(3)
        self.tra_imagen1 = tk.Label(self.frame_tra,bg="#d9d9d9", image=self.tra_imagen).grid(row=1,column=1,rowspan=3)
        self.tra_disp_num = "Disponibles: {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Transistor')][0])
        self.tra_disp = tk.Label(self.frame_tra,bg="#d9d9d9",text=self.tra_disp_num,font=("Bahnschrift Light",11))
        self.tra_disp.grid(row=1,column=2,columnspan=2)
        self.tra_unit_num = "Precio Unit.: S/. {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Transistor')][1])
        self.tra_unit = tk.Label(self.frame_tra,bg="#d9d9d9",text=self.tra_unit_num,font=("Bahnschrift Light",11))
        self.tra_unit.grid(row=2,column=2,columnspan=2)
        self.tra_comp = tk.Label(self.frame_tra,bg="#d9d9d9",text='Cantidad:',font=("Bahnschrift Light",11)).grid(row=4,column=1)
        self.tra_comp1 = tk.Entry(self.frame_tra,font=("Bahnschrift Light",11),state='normal',width=6)
        self.tra_comp1.grid(row=4,column=2)
        self.tra_bot = tk.Button(self.frame_tra,text="AÑADIR AL CARRITO",bg='#1A52E0',fg='white',font = ("Berlin Sans FB Demi", 11, "bold"),command=self.AñadirTra).grid(row=6,column=1,columnspan=2,padx=40,pady=8)
        #frame de triac
        self.frame_triac = tk.LabelFrame(self.frame_productos,bg="#d9d9d9", text="Triac",font=("Bahnschrift Light",11,"bold","italic"))
        self.frame_triac.grid(row=3,column=3)
        self.tri_imagen = PhotoImage(file="Imagenes/triac.png").subsample(3)
        self.tri_imagen1 = tk.Label(self.frame_triac,bg="#d9d9d9", image=self.tri_imagen).grid(row=1,column=1,rowspan=3)
        self.tri_disp_num = "Disponibles: {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Triac')][0])
        self.tri_disp = tk.Label(self.frame_triac,bg="#d9d9d9",text=self.tri_disp_num,font=("Bahnschrift Light",11))
        self.tri_disp.grid(row=1,column=2,columnspan=2)
        self.tri_unit_num = "Precio Unit.: S/. {}".format(list(self.Inven.values())[list(self.Inven.keys()).index('Triac')][1])
        self.tri_unit = tk.Label(self.frame_triac,bg="#d9d9d9",text=self.tri_unit_num,font=("Bahnschrift Light",11))
        self.tri_unit.grid(row=2,column=2,columnspan=2)
        self.tri_comp = tk.Label(self.frame_triac,bg="#d9d9d9",text='Cantidad:',font=("Bahnschrift Light",11)).grid(row=4,column=1)
        self.tri_comp1 = tk.Entry(self.frame_triac,font=("Bahnschrift Light",11),state='normal',width=6)
        self.tri_comp1.grid(row=4,column=2)
        self.tri_bot = tk.Button(self.frame_triac,text="AÑADIR AL CARRITO",bg='#1A52E0',fg='white',font = ("Berlin Sans FB Demi", 11, "bold"),command=self.AñadirTri).grid(row=6,column=1,columnspan=2,padx=40,pady=8)

        #Frame de carrito
        self.frame_carrito = tk.LabelFrame(self.venta,bg="#d9d9d9",text="CARRITO",font=("Bahnschrift Light",11,"bold"))
        self.frame_carrito.grid(row=3,column=2,padx=1,pady=5)
        self.carrito_lista = tk.Listbox(self.frame_carrito,height=9,width=25,justify='center',font=("Bahnschrift Light",11,'italic'))
        self.carrito_lista.grid(row=1,column=1,columnspan=2,padx=5,pady=3)
        self.carrito_label = tk.Label(self.frame_carrito,bg="#d9d9d9",text='TOTAL:',font=("Bahnschrift Light",11)).grid(row=2,column=1,pady=8)
        self.carrito_tot = tk.Entry(self.frame_carrito,font=("Bahnschrift Light",11),state='readonly',width=6)
        self.carrito_tot.grid(row=2,column=2)
        self.carrito_bot_borrar = tk.Button(self.frame_carrito,text='LIMPIAR \n CARRITO',bg='red',fg='white',font = ("Berlin Sans FB Demi", 11, "bold"),command=self.Limpiar_carrito).grid(row=3,column=2,pady=12)
        self.carrito_bot_comprar = tk.Button(self.frame_carrito,text='GENERAR \n BOLETA',bg='green',fg='white',font = ("Berlin Sans FB Demi", 11, "bold"),command=self.Boleta).grid(row=3,column=1,pady=12)

        #Iniciador de ventana
        self.venta.mainloop()
        
    #funcion para comprobar si ingresa un numero
    def comprobacion(self,entry):
        try:
            int(entry)
            return True
        except ValueError:
            return False   
    #funcion general para llenado de carrito
    def Llenar(self,nombre_producto,entrada):
        self.carrito_lista.insert(self.n,str(entrada+' unidades de '+nombre_producto))
        self.n = self.n + 1
        prec_unit = float(list(self.Inven.values())[list(self.Inven.keys()).index(nombre_producto)][1])
        disponibilidad = int(list(self.Inven.values())[list(self.Inven.keys()).index(nombre_producto)][0])
        self.Carrito[nombre_producto] = [entrada, prec_unit, (prec_unit*float(entrada)),disponibilidad]
        self.costos=[]
        for i in range(len(self.Carrito)):
            self.costos.append((list(self.Carrito.values()))[i][2])
        self.carrito_tot.config(state='normal')
        self.carrito_tot.delete(0,'end')
        self.carrito_tot.insert(0,round((sum(self.costos))*1.18,3))   
        self.carrito_tot.config(state='readonly')
    #funcion añadir potenciometros
    def AñadirPot(self):
        producto = 'Potenciometro'
        if self.cont[0]==1:
            cantidad = self.pot_comp1.get()
            self.pot_comp1.delete(0,'end')
            if self.comprobacion(cantidad) == True:
                if int(cantidad) <= list(self.Inven.values())[list(self.Inven.keys()).index(producto)][0]:
                    self.Llenar(producto,cantidad)
                    self.cont[0] = self.cont[0]+1
                else:
                    MessageBox.showerror("Error al añadir"," Cantidad excede la disponibilidad")
            else:
                MessageBox.showerror("Error en ingreso de datos"," Introduzca solo números enteros \n en 'Cantidad' porfavor")
        else:
            self.pot_comp1.delete(0,'end')
            MessageBox.showerror("Error al añadir"," {} añadido con anterioridad. \n Limpie el carrito si desea agregar \n este producto nuevamente".format(producto))
    #funcion añadir resistencias
    def AñadirRes(self):
        producto = 'Resistor'
        if self.cont[1]==1:
            cantidad = self.res_comp1.get()
            self.res_comp1.delete(0,'end')
            if self.comprobacion(cantidad) == True:
                if int(cantidad) <= list(self.Inven.values())[list(self.Inven.keys()).index(producto)][0]:
                    self.Llenar(producto,cantidad)
                    self.cont[1] = self.cont[1]+1
                else:
                    MessageBox.showerror("Error al añadir"," Cantidad excede la disponibilidad")
            else:
                MessageBox.showerror("Error en ingreso de datos"," Introduzca solo números enteros \n en 'Cantidad' porfavor")
        else:
            self.res_comp1.delete(0,'end')
            MessageBox.showerror("Error al añadir"," {} añadido con anterioridad. \n Limpie el carrito si desea agregar \n este producto nuevamente".format(producto))
    #funcion añadir arduinos
    def AñadirArd(self):
        producto = 'Arduino UNO'
        if self.cont[2]==1:
            cantidad = self.ard_comp1.get()
            self.ard_comp1.delete(0,'end')
            if self.comprobacion(cantidad) == True:
                if int(cantidad) <= list(self.Inven.values())[list(self.Inven.keys()).index(producto)][0]:
                    self.Llenar(producto,cantidad)
                    self.cont[2] = self.cont[2]+1
                else:
                    MessageBox.showerror("Error al añadir"," Cantidad excede la disponibilidad")
            else:
                MessageBox.showerror("Error en ingreso de datos"," Introduzca solo números enteros \n en 'Cantidad' porfavor")
        else:
            self.ard_comp1.delete(0,'end')
            MessageBox.showerror("Error al añadir"," {} añadido con anterioridad. \n Limpie el carrito si desea agregar \n este producto nuevamente".format(producto))
    #funcion de añadir condensadores
    def AñadirCap(self):
        producto = 'Capacitor'
        if self.cont[3]==1:
            cantidad = self.cap_comp1.get()
            self.cap_comp1.delete(0,'end')
            if self.comprobacion(cantidad) == True:
                if int(cantidad) <= list(self.Inven.values())[list(self.Inven.keys()).index(producto)][0]:
                    self.Llenar(producto,cantidad)
                    self.cont[3] = self.cont[3]+1
                else:
                    MessageBox.showerror("Error al añadir"," Cantidad excede la disponibilidad")
            else:
                MessageBox.showerror("Error en ingreso de datos"," Introduzca solo números enteros \n en 'Cantidad' porfavor")
        else:
            self.cap_comp1.delete(0,'end')
            MessageBox.showerror("Error al añadir"," {} añadido con anterioridad. \n Limpie el carrito si desea agregar \n este producto nuevamente".format(producto))
    #funcion para añadir LDR
    def AñadirLDR(self):
        producto = 'LDR'
        if self.cont[4]==1:
            cantidad = self.ldr_comp1.get()
            self.ldr_comp1.delete(0,'end')
            if self.comprobacion(cantidad) == True:
                if int(cantidad) <= list(self.Inven.values())[list(self.Inven.keys()).index(producto)][0]:
                    self.Llenar(producto,cantidad)
                    self.cont[4] = self.cont[4]+1
                else:
                    MessageBox.showerror("Error al añadir"," Cantidad excede la disponibilidad")
            else:
                MessageBox.showerror("Error en ingreso de datos"," Introduzca solo números enteros \n en 'Cantidad' porfavor")
        else:
            self.ldr_comp1.delete(0,'end')
            MessageBox.showerror("Error al añadir"," {} añadido con anterioridad. \n Limpie el carrito si desea agregar \n este producto nuevamente".format(producto))
    #funcion para añadir led
    def AñadirLED(self):
        producto = 'LED'
        if self.cont[5]==1:
            cantidad = self.led_comp1.get()
            self.led_comp1.delete(0,'end')
            if self.comprobacion(cantidad) == True:
                if int(cantidad) <= list(self.Inven.values())[list(self.Inven.keys()).index(producto)][0]:
                    self.Llenar(producto,cantidad)
                    self.cont[5] = self.cont[5]+1
                else:
                    MessageBox.showerror("Error al añadir"," Cantidad excede la disponibilidad")
            else:
                MessageBox.showerror("Error en ingreso de datos"," Introduzca solo números enteros \n en 'Cantidad' porfavor")
        else:
            self.led_comp1.delete(0,'end')
            MessageBox.showerror("Error al añadir"," {} añadido con anterioridad. \n Limpie el carrito si desea agregar \n este producto nuevamente".format(producto))
    #funcion para añadir servo
    def AñadirSer(self):
        producto = 'Servomotor'
        if self.cont[6]==1:
            cantidad = self.ser_comp1.get()
            self.ser_comp1.delete(0,'end')
            if self.comprobacion(cantidad) == True:
                if int(cantidad) <= list(self.Inven.values())[list(self.Inven.keys()).index(producto)][0]:
                    self.Llenar(producto,cantidad)
                    self.cont[6] = self.cont[6]+1
                else:
                    MessageBox.showerror("Error al añadir"," Cantidad excede la disponibilidad")
            else:
                MessageBox.showerror("Error en ingreso de datos"," Introduzca solo números enteros \n en 'Cantidad' porfavor")
        else:
            self.ser_comp1.delete(0,'end')
            MessageBox.showerror("Error al añadir"," {} añadido con anterioridad. \n Limpie el carrito si desea agregar \n este producto nuevamente".format(producto))
    #funcion para añadir transistor
    def AñadirTra(self):
        producto = 'Transistor'
        if self.cont[7]==1:
            cantidad = self.tra_comp1.get()
            self.tra_comp1.delete(0,'end')
            if self.comprobacion(cantidad) == True:
                if int(cantidad) <= list(self.Inven.values())[list(self.Inven.keys()).index(producto)][0]:
                    self.Llenar(producto,cantidad)
                    self.cont[7] = self.cont[7]+1
                else:
                    MessageBox.showerror("Error al añadir"," Cantidad excede la disponibilidad")
            else:
                MessageBox.showerror("Error en ingreso de datos"," Introduzca solo números enteros \n en 'Cantidad' porfavor")
        else:
            self.tra_comp1.delete(0,'end')
            MessageBox.showerror("Error al añadir"," {} añadido con anterioridad. \n Limpie el carrito si desea agregar \n este producto nuevamente".format(producto))
    #funcion para añadir triac
    def AñadirTri(self):
        producto = 'Triac'
        if self.cont[8]==1:
            cantidad = self.tri_comp1.get()
            self.tri_comp1.delete(0,'end')
            if self.comprobacion(cantidad) == True:
                if int(cantidad) <= list(self.Inven.values())[list(self.Inven.keys()).index(producto)][0]:
                    self.Llenar(producto,cantidad)
                    self.cont[8] = self.cont[8]+1
                else:
                    MessageBox.showerror("Error al añadir"," Cantidad excede la disponibilidad")
            else:
                MessageBox.showerror("Error en ingreso de datos"," Introduzca solo números enteros \n en 'Cantidad' porfavor")
        else:
            self.tri_comp1.delete(0,'end')
            MessageBox.showerror("Error al añadir"," {} añadido con anterioridad. \n Limpie el carrito si desea agregar \n este producto nuevamente".format(producto))

    #funcion para limpiar carrito
    def Limpiar_carrito(self):
        self.Carrito = {}
        self.carrito_lista.delete(0,8)
        self.cont = [1,1,1,1,1,1,1,1,1]
        self.carrito_tot.config(state='normal')
        self.carrito_tot.delete(0,'end')  
        self.carrito_tot.config(state='readonly')

    #funcion para boleta
    def Boleta(self):
        vendedor_venta = self.vendedor
        if len(self.Carrito)== 0:
            MessageBox.showerror('Error al generar boleta',' Seleccione almenos un producto \n para generar boleta.')
        else:
            usuario = self.nom_comp2.get().title()
            dni = self.dni_2.get()
            domicilio = self.direccion2.get().title()
            if (len(usuario)!=0) or (len(dni)!=0) or (len(domicilio)!=0):
                             
                self.alto = str(300+(((len(self.Carrito))-1)*20))
                print(self.alto)
                
                #ventana de boleta:
                boleta = tk.Toplevel()
                boleta.title("Boleta de compra")
                boleta.geometry("700x{}".format(self.alto))
                boleta.config(bg="#d9d9d9")
                boleta.resizable(False,False)
                boleta.iconbitmap('Imagenes/unt.ico')
              
                #fecha y hora de compra
                fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            
                #titulo:
                Titulo_boleta = tk.Label(boleta,bg="#d9d9d9",text="HARZ   ELECTRONICS S.A.C.", font=("Broadway", 20), fg="black")
                Titulo_boleta.grid(row=1,column=1,columnspan=6)
                espacio = tk.Label(boleta,text='   ',bg="#d9d9d9").grid(row=1,column=1)
                #frame de datos
                frame_datos = tk.LabelFrame(boleta,bg="#d9d9d9")
                frame_datos.grid(row=2,column=1,columnspan=6,pady=10)
                nombre1 = tk.Label(frame_datos,bg="#d9d9d9",text='Señor(es): ',font=("Times New Roman",12,'bold')).grid(row=1,column=1)
                nombre2 = tk.Label(frame_datos,bg="#d9d9d9",text = usuario, font=("Times New Roman", 12, 'italic'))
                nombre2.grid(row=1,column=2)
                direc1 = tk.Label(frame_datos,bg="#d9d9d9",text='Domicilio: ',font=("Times New Roman",12,'bold')).grid(row=2,column=1)
                direc2 = tk.Label(frame_datos,bg="#d9d9d9",text = domicilio, font=("Times New Roman", 12, 'italic'))
                direc2.grid(row=2,column=2)
                dni1 = tk.Label(frame_datos,bg="#d9d9d9",text='DNI: ',font=("Times New Roman",12,'bold')).grid(row=1,column=3)
                dni2 = tk.Label(frame_datos,bg="#d9d9d9",text = dni, font=("Times New Roman", 12, 'italic'))
                dni2.grid(row=1,column=4)
                fecha1 = tk.Label(frame_datos,bg="#d9d9d9",text='Fecha: ',font=("Times New Roman",12,'bold')).grid(row=2,column=3)
                fecha2 = tk.Label(frame_datos,bg="#d9d9d9",text = fecha, font=("Times New Roman", 12, 'italic'))
                fecha2.grid(row=2,column=4)
                
                #tabla de productos
                headers_productos = ['CANT.','PRODUCTO','P. UNIT','IMPORTE']
                headers_totales = ['SUBTOTAL','IGV (18%)','TOTAL']
                
                objetos_tabla = []
                for i in range(len(self.Carrito)):
                    objetos_tabla.append((list(self.Carrito.values()))[i])
                objetos_totales = [round(sum(self.costos),3), round((sum(self.costos)*0.18),3), round((sum(self.costos)*1.18),3)]
                
                for i in range(4):
                    b = tk.Entry(boleta,font=("Times New Roman",11,'bold'))
                    b.insert(0,headers_productos[i])
                    b.config(justify="center")
                    b.config(state="readonly")
                    b.grid(row=3,column=3+i)
                    
                for i in range(len(self.Carrito)):
                    b = tk.Entry(boleta,font=("Times New Roman",11,'italic'))
                    b.insert(0,objetos_tabla[i][0])
                    b.config(state="readonly")
                    b.config(justify="center")
                    b.grid(row=i+5 ,column= 3)
                
                for i in range(len(self.Carrito)):
                    b = tk.Entry(boleta,font=("Times New Roman",11,'italic'))
                    b.insert(0,(list(self.Carrito.keys()))[i])
                    b.config(state="readonly")
                    b.grid(row=i+5 ,column= 4)
                    
                for i in range(len(self.Carrito)):
                    b = tk.Entry(boleta,font=("Times New Roman",11,'italic'))
                    b.insert(0,objetos_tabla[i][1])
                    b.config(state="readonly")
                    b.config(justify="right")
                    b.grid(row=i+5 ,column= 5)    
                    
                for i in range(len(self.Carrito)):
                    b = tk.Entry(boleta,font=("Times New Roman",11,'italic'))
                    b.insert(0,round(objetos_tabla[i][2],1))
                    b.config(state="readonly")
                    b.config(justify="right")
                    b.grid(row=i+5 ,column= 6) 
                    
                espacio_tot = tk.Label(boleta,text='',bg="#d9d9d9").grid(row=len(self.Carrito)+5,column=2)
                
                for i in range(3):
                    b = tk.Entry(boleta,font=("Times New Roman",11,'bold'))
                    b.insert(0,headers_totales[i])
                    b.config(state='readonly')
                    b.config(justify="right")
                    b.grid(row=i+(len(self.Carrito))+6,column=5)

                for i in range(3):
                    b = tk.Entry(boleta,font=("Times New Roman",11,'italic'))
                    b.insert(0, 'S/.' + str(objetos_totales[i]))
                    b.config(state="readonly")
                    b.config(justify="right")
                    b.grid(row=i+(len(self.Carrito)+6),column=6)             
                
                bot_boleta = tk.Button(boleta,text='FINALIZAR',bg='#1A52E0',fg='white',font = ("Berlin Sans FB Demi", 13, "bold"),command=boleta.destroy).grid(row=9+len(self.Carrito),column=5,columnspan=2,pady=10)
                             
                #actualizando cantidades en base de datos
                for i in range(len(self.Carrito)):
                    cantidad_new = int(objetos_tabla[i][3]) - int((objetos_tabla[i][0]))
                    update_cantidad((list(self.Carrito.keys())[i]),cantidad_new)
                
                self.Limpiar_carrito()
                
                #limpiando datos
                self.nom_comp2.delete(0,'end')
                self.dni_2.delete(0,'end')
                self.direccion2.delete(0,'end')
                
                #actualizacion de cantidades
                self.inventario_new = visualizar_productos()
                self.Inven_new = {}
                for i in range(len(self.inventario_new)):
                    self.Inven_new[self.inventario_new[i][0]] = [self.inventario_new[i][1],float(self.inventario_new[i][2])]
                self.pot_disp_nume = "Disponibles: {}".format(list(self.Inven_new.values())[list(self.Inven_new.keys()).index('Potenciometro')][0])
                self.pot_disp.config(text=self.pot_disp_nume)
                self.res_disp_nume = "Disponibles: {}".format(list(self.Inven_new.values())[list(self.Inven_new.keys()).index('Resistor')][0])
                self.res_disp.config(text=self.res_disp_nume)
                self.ard_disp_nume = "Disponibles: {}".format(list(self.Inven_new.values())[list(self.Inven_new.keys()).index('Arduino UNO')][0])
                self.ard_disp.config(text=self.ard_disp_nume)
                self.cap_disp_nume = "Disponibles: {}".format(list(self.Inven_new.values())[list(self.Inven_new.keys()).index('Capacitor')][0])
                self.cap_disp.config(text=self.cap_disp_nume)
                self.ldr_disp_nume = "Disponibles: {}".format(list(self.Inven_new.values())[list(self.Inven_new.keys()).index('LDR')][0])
                self.ldr_disp.config(text=self.ldr_disp_nume)
                self.led_disp_nume = "Disponibles: {}".format(list(self.Inven_new.values())[list(self.Inven_new.keys()).index('LED')][0])
                self.led_disp.config(text=self.led_disp_nume)
                self.ser_disp_nume = "Disponibles: {}".format(list(self.Inven_new.values())[list(self.Inven_new.keys()).index('Servomotor')][0])
                self.ser_disp.config(text=self.ser_disp_nume)
                self.tra_disp_nume = "Disponibles: {}".format(list(self.Inven_new.values())[list(self.Inven_new.keys()).index('Transistor')][0])
                self.tra_disp.config(text=self.tra_disp_nume)
                self.tri_disp_nume = "Disponibles: {}".format(list(self.Inven_new.values())[list(self.Inven_new.keys()).index('Triac')][0])
                self.tri_disp.config(text=self.tri_disp_nume)
                
                #extraer datos del vendedor
                datos_vendedor = extraer_ventaycomision(vendedor_venta)
                valor_venta = round(float(datos_vendedor[0]) + (sum(self.costos)*1.18),2) 
                valor_comision =  round(float(datos_vendedor[1]) + ((sum(self.costos))*1.18*0.2),2)
                
                #cambios en la base de datos
                update_ventaycomision(vendedor_venta,valor_venta,valor_comision)
                #resetear carrito
                self.Carrito = {}
            else:
                MessageBox.showerror('Error en datos de comprador', 'Introduzca todos los datos del comprador')

def abrir_web():
        webbrowser.open("https://projecventas.herokuapp.com/")

#Ventana Principal

class Ventana_Principal():

    def __init__(self):
        self.Inicio()

    def Inicio(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("HARZ ELECTRONICS S.A.C.")
        self.ventana1.geometry("540x420")
        self.ventana1.config(bg="#d9d9d9")
        self.ventana1.resizable(False, False)
        self.ventana1.iconbitmap('Imagenes/unt.ico')

        self.Titulo = tk.Label(bg="#d9d9d9",text="BIENVENIDO A \n HARZ   ELECTRONICS S.A.C.", font=("Broadway", 25), fg="black")
        self.Titulo.place(x=25, y=20)
        self.Ind = tk.Label(bg="#d9d9d9",text="Presione el botón que indique su rol/cargo:", font=("Bahnschrift Light",15,'bold','italic'), fg="blue")
        self.Ind.place(x=26, y=120)
        self.Rol1 = tk.Button(self.ventana1, width=11, height=2, bg="#05C967", text="SUPERVISOR",
                         font=("Berlin Sans FB Demi", 12, "bold"), fg="#FFFFFF", borderwidth=2.3, command=Log_sup)
        self.Rol1.place(x=200, y=160)
        self.Rol2 = tk.Button(self.ventana1, width=11, height=2, bg="#05C967", text="VENDEDOR",
                         font=("Berlin Sans FB Demi", 12, "bold"), fg="#FFFFFF", borderwidth=2.3, command=Log_vent)
        self.Rol2.place(x=200, y=225)
        self.Rol3 = tk.Button(self.ventana1, width=11, height=2, bg="#05C967", text="CLIENTE",
                         font=("Berlin Sans FB Demi", 12, "bold"), fg="#FFFFFF", borderwidth=2.3, command=abrir_web)
        self.Rol3.place(x=200, y=290)
        self.Salir = tk.Button(self.ventana1, width=11, height=2, bg="#DE433A", text="SALIR",
                          font=("Berlin Sans FB Demi", 12, "bold"), fg="#FFFFFF", borderwidth=2.3,
                          command=self.ventana1.destroy)
        self.Salir.place(x=390, y=350)
        self.Cred = tk.Label(bg="#d9d9d9",text="by estudiantes de: \n UNT - Ing. Mecatrónica", font=("Bahnschrift Light", 10,'bold'), fg="black")
        self.Cred.place(x=10, y=368)
        
        self.ventana1.mainloop()

if __name__=="__main__":
    Ventana_Principal()