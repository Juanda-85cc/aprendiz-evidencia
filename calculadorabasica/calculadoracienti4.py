import tkinter as tk
from tkinter import messagebox
import re
import math

modo_grados = True 

def sin(x):
    return math.sin(math.radians(x) if modo_grados else x)

def cos(x):
    return math.cos(math.radians(x) if modo_grados else x)

def tan(x):
    return math.tan(math.radians(x) if modo_grados else x)

def asin(x):
    angulo = math.asin(x)
    return math.degrees(angulo) if modo_grados else angulo

def acos(x):
    angulo = math.acos(x)
    return math.degrees(angulo) if modo_grados else angulo

def atan(x):
    angulo = math.atan(x)
    return math.degrees(angulo) if modo_grados else angulo

def ln(x):
    return math.log(x)

def sqrt(x):
    return math.sqrt(x)

def log(*args):
    if len(args) == 1:
        return math.log10(args[0])  
    elif len(args) == 2:
        return math.log(args[1], args[0])  
    else:
        raise ValueError("log debe tener uno o dos argumentos.")

def factorial(x):
    if not float(x).is_integer() or x < 0:
        raise ValueError("El factorial solo está definido para enteros no negativos.")
    return math.factorial(int(x))

def calcular():
    try:
        expresion = entrada.get().lower()

        
        expresion = re.sub(r'(\d+(?:\.\d+)?)\s*%\s*de\s*(\d+(?:\.\d+)?)', r'(\1/100)*\2', expresion)
        expresion = re.sub(r'(\d+(?:\.\d+)?)\s*%', r'(\1/100)', expresion)

        resultado = eval(expresion, {"__builtins__": None}, {
            "sin": sin, "cos": cos, "tan": tan,
            "asin": asin, "acos": acos, "atan": atan,
            "log": log, "ln": ln, "sqrt": sqrt,
            "factorial": factorial,  
            "π": math.pi, "e": math.e
        })

        entrada.delete(0, tk.END)
        entrada.insert(0, str(round(resultado, 6)))
    except Exception as e:
        messagebox.showerror("Error", f"Expresión no válida.\n{e}")
        entrada.delete(0, tk.END)

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

def cambiar_a_grados():
    global modo_grados
    modo_grados = True
    label_modo.config(text="Modo: DEG")

def cambiar_a_radianes():
    global modo_grados
    modo_grados = False
    label_modo.config(text="Modo: RAD")

ventana = tk.Tk()
ventana.title("Calculadora Científica")
ventana.geometry("350x700")
ventana.resizable(True, True)

entrada = tk.Entry(ventana, font=("Arial", 18), justify="right", bd=12)
entrada.grid(row=0, column=0, columnspan=5, padx=12, pady=12)

label_modo = tk.Label(ventana, text="Modo: DEG", font=("Arial", 12), anchor="w")
label_modo.grid(row=1, column=0, columnspan=4, sticky="w", padx=10)

botones = [
    ('Deg', 1, 0), ('Rad', 1, 1), ('Sin', 1, 2), ('Cos', 1, 3), ('Tan', 1, 4),
    ('^', 2, 0), ('Log', 2, 1), ('Ln', 2, 2), ('e', 2, 3), ('()', 2, 4),
    ('√', 3, 0), ('AC', 3, 1), ('←', 3, 2), ('%', 3, 3), ('/', 3, 4),
    ('x!', 4, 0), ('7', 4, 1), ('8', 4, 2), ('9', 4, 3), ('*', 4, 4),
    ('asin', 5, 0), ('4', 5, 1), ('5', 5, 2), ('6', 5, 3), ('-', 5, 4),
    ('acos', 6, 0), ('1', 6, 1), ('2', 6, 2), ('3', 6, 3), ('+', 6, 4),
    ('atan', 7, 0), ('π', 7, 1), ('0', 7, 2), ('.', 7, 3), ('=', 7, 4),
]

for (texto, fila, columna) in botones:
    if texto == "=":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14), command=calcular)
    elif texto == "AC":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14), command=limpiar)
    elif texto == "←":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14), command=borrar_ultimo)
    elif texto == "Deg":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14), command=cambiar_a_grados)
    elif texto == "Rad":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14), command=cambiar_a_radianes)
    elif texto in ["Sin", "Cos", "Tan", "Log", "Ln", "asin", "acos", "atan"]:
        boton = tk.Button(ventana, text=texto, font=("Arial", 14),
                          command=lambda t=texto.lower(): agregar_texto(f"{t}("))
    elif texto == "√":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14),
                          command=lambda: agregar_texto("sqrt("))
    elif texto == "^":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14),
                          command=lambda: agregar_texto("**"))
    elif texto == "π":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14),
                          command=lambda: agregar_texto("π"))
    elif texto == "e":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14),
                          command=lambda: agregar_texto("e"))
    elif texto == "x!":
        boton = tk.Button(ventana, text=texto, font=("Arial", 14),
                          command=lambda: agregar_texto("factorial("))
    else:
        boton = tk.Button(ventana, text=texto, font=("Arial", 14),
                          command=lambda t=texto: agregar_texto(t))
    boton.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)

for i in range(8):
    ventana.grid_rowconfigure(i, weight=1)
for j in range(5):
    ventana.grid_columnconfigure(j, weight=1)

ventana.mainloop()