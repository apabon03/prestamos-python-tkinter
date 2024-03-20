#importar la libreria para interfaz grafica de usuario
from tkinter import *
from tkinter import messagebox

#regular expressions
import re

#crear ventana
v = Tk()
v.title("Plan pagos préstamo")
v.minsize(500, 300)

#agregar las etiquetas
Label(v, text="Monto a prestar: ").grid(row=0, column=0)
Label(v, text="Tasa de interés (%): ").grid(row=1, column=0)
Label(v, text="Plazo: ").grid(row=2, column=0)

Label(v, text="Cuota:").grid(row=3, column=1)

#agregar las cajas de texto
txtMonto = Entry(v, width=15)
txtMonto.grid(row=0, column=1)

txtTasa = Entry(v, width=5)
txtTasa.grid(row=1, column=1)

txtPlazo = Entry(v, width=5)
txtPlazo.grid(row=2, column=1)

txtCuota = Entry(v, width=15)
txtCuota.grid(row=3, column=2)
txtCuota.configure(state=DISABLED) #bloquea la caja de texto

txtPlanPagos = Text(v, width=70, height=20)
txtPlanPagos.grid(row=4, column=0, columnspan=3)

def calcular_Plan_Pagos():
    #validacion datos de entrada
    if re.match("^[0-9]+$", txtMonto.get()) and \
       re.match("^[0-9]+[.]?[0-9]*$", txtTasa.get()) and \
       re.match("^[0-9]+$", txtPlazo.get()):
        #obtener datos de entrada
        monto = int(txtMonto.get())
        tasa= float(txtTasa.get())/100
        plazo = int(txtPlazo.get())
        
        #proceso
        cuota = monto * (1 + tasa)**plazo *tasa/((1 + tasa)**plazo -1)
        saldo = monto
        planPagos = "# Cuota\t\tAbono Capital\t\tIntereses\t\tSaldo\n"

        for i in range(1, plazo + 1):
            intereses = saldo*tasa
            abono = cuota - intereses
            saldo -= abono

            planPagos += str(i) + "\t" + "${0:,.2f}".format(abono) \
                             + "\t\t" + "${0:,.2f}".format(intereses) \
                             + "\t\t" + "${0:,.2f}".format(saldo) \
                             + "\n"
        
        
        #Mostrar resultados
        txtCuota.configure(state=NORMAL) # se desbloquea la caja de texto
        txtCuota.delete(0, END) #quitar si tiene datos
        txtCuota.insert(0, "${0:,.2f}".format(cuota)) #lleva el dato
        txtCuota.configure(state=DISABLED)

        txtPlanPagos.configure(state=NORMAL) # se desbloquea la caja de texto
        txtPlanPagos.delete(1.0, END) #quitar si tiene datos
        txtPlanPagos.insert(1.0, planPagos) #lleva el dato
        txtPlanPagos.configure(state=DISABLED)

        
    else:
        messagebox.showerror("Error en la entrada de datos", "Los datos deben ser numéricos")

#agregar boton de comando
Button(v, text="Calcular", command=calcular_Plan_Pagos).grid(row=3, column=0)

  
