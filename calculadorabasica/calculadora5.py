import tkinter as tk
from tkinter import messagebox
import re  

def calcular():
    try:
        expresion = entrada.get()

        
        expresion = re.sub(r'(\d)\s*\(', r'\1*(', expresion)
        expresion = re.sub(r'\)\s*(\d)', r')*\1', expresion)

    
        match = re.match(r'(\d+(\.\d+)?)%\s*(\d+(\.\d+)?)', expresion)
        if match:
            porcentaje = float(match.group(1)) / 100
            cifra = float(match.group(3))
            if porcentaje < 0 or porcentaje > 1:
                messagebox.showerror("Error", "El porcentaje debe estar entre 1% y 100%.")
                entrada.delete(0, tk.END)
                return
            resultado = porcentaje * cifra
        else:
            try:
                resultado = eval(expresion)
            except:
                messagebox.showerror("Error", "Expresión no válida.")
                entrada.delete(0, tk.END)
                return

        entrada.delete(0, tk.END)
        entrada.insert(0, str(round(resultado, 6)))
    except Exception as e:
        messagebox.showerror("Error", "Expresión no válida")

def agregar_texto(texto):
    if texto == "()":
        contenido = entrada.get()
        if contenido.count("(") > contenido.count(")"):
            entrada.insert(tk.END, ")")
        else:
            entrada.insert(tk.END, "(")
    else:
        entrada.insert(tk.END, texto)  

def borrar_ultimo():
    contenido = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, contenido[:-1])

def limpiar():
    entrada.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Calculadora Basica")
ventana.geometry("300x500")
ventana.resizable(True, True)


entrada = tk.Entry(ventana, font=("Arial", 18), justify="right", bd=10)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


botones = [
    ('AC', 1, 0), ('←', 1, 1), ('%', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('()', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
]


for (texto, fila, columna) in botones:
    if texto == "=":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14), command=calcular)
    elif texto == "AC":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14), command=limpiar)
    elif texto == "←":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14), command=borrar_ultimo)
    else:
        boton = tk.Button(ventana, text=texto, font=("Arial", 14),
                          command=lambda t=texto: agregar_texto(t))
    boton.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)


for i in range(6):  
    ventana.grid_rowconfigure(i, weight=1)
for j in range(4):
    ventana.grid_columnconfigure(j, weight=1)

ventana.mainloop()
