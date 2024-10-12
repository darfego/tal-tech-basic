import tkinter as tk  # Importa la biblioteca tkinter para crear interfaces gráficas
from tkinter import messagebox  # Importa el módulo messagebox de tkinter para mostrar cuadros de diálogo
import math  # Importa la biblioteca math para realizar operaciones matemáticas

# Define una clase llamada Calculadora para crear una calculadora
class Calculadora:
    # Método constructor de la clase Calculadora, se llama automáticamente al crear una instancia de la clase
    def __init__(self, root):
        self.root = root  # Asigna la ventana principal a la variable root
        self.root.title("Calculadora Estándar")  # Establece el título de la ventana principal
        self.root.configure(bg="#ffffff")  # Configura el color de fondo de la ventana principal a blanco
        self.root.geometry("375x700")  # Establece el tamaño de la ventana para acomodar todos los botones
        self.root.resizable(False, False)  # Impide que la ventana se redimensione

        # Crea un campo de entrada (Entry) deshabilitado para mostrar los números y resultados
        self.entrada = tk.Entry(root, width=17, font=("Arial", 28), borderwidth=0, relief='solid', bg="#ffffff", fg="black", justify="right", state='disabled')
        self.entrada.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=(10, 5))  # Posiciona el campo de entrada en la cuadrícula de la ventana

        self.resultado = None  # Inicializa la variable resultado como None (sin valor)
        self.operacion_pendiente = False  # Bandera para indicar si hay una operación pendiente
        self.memoria = []  # Inicializa una lista para almacenar los valores en memoria
        self.crear_botones()  # Llama al método para crear los botones de la calculadora

    # Método para crear los botones de la calculadora
    def crear_botones(self):
        # Lista de botones con sus etiquetas y el span de columna (número de columnas que ocupan)
        botones = [
            ("MC", 1), ("MR", 1), ("M+", 1), ("M-", 1),
            ("1/x", 1), ("x²", 1), ("√", 1), ("±", 1),
            ("C", 1), ("←", 1), ("/", 1), ("%", 1),
            ("7", 1), ("8", 1), ("9", 1), ("*", 1),
            ("4", 1), ("5", 1), ("6", 1), ("-", 1),
            ("1", 1), ("2", 1), ("3", 1), ("+", 1),
            ("0", 2), (".", 1), ("=", 1),
        ]

        # Diccionario que define los colores para diferentes tipos de botones
        colores_botones = {
            "numero": "#4d4d4d",  # Color para botones numéricos
            "operador": "#fe9505",  # Color para botones de operadores
            "igual": "#fe9505",  # Color para el botón igual
            "fondo": "#ffffff",  # Color de fondo de la calculadora
            "texto": "#000000",  # Color del texto de los botones
            "reset": "#d32f2f",  # Color para el botón de reset (C)
            "borrar": "#fe9505"  # Color para el botón de borrar (←)
        }

        # Crea un marco (Frame) para contener los botones
        frame_botones = tk.Frame(self.root, bg="#ffffff")  # Marco con fondo blanco
        frame_botones.grid(row=1, column=0, columnspan=4, pady=(0, 10))  # Posiciona el marco en la cuadrícula

        fila, columna = 0, 0  # Inicializa las variables de fila y columna

        # Itera sobre la lista de botones para crear cada botón
        for boton, span in botones:
            # Define el color de fondo basado en el tipo de botón
            color_fondo = colores_botones["operador"] if boton in ["/", "*", "-", "+", "=", "←", "MC", "MR", "M+", "M-", "%", "1/x", "x²", "√", "±"] else colores_botones["numero"]
            if boton == "C":
                color_fondo = colores_botones["reset"]
            elif boton == "←":
                color_fondo = colores_botones["borrar"]
            elif boton == "=":
                color_fondo = colores_botones["igual"]

            # Crea el botón y lo agrega al marco de botones
            tk.Button(frame_botones, text=boton, width=5 * span, height=2, font=("Arial", 20), bg=color_fondo, fg=colores_botones["texto"], borderwidth=0, command=lambda b=boton: self.click_boton(b)).grid(row=fila, column=columna, columnspan=span, padx=1, pady=1, sticky="nsew")

            columna += span  # Incrementa la columna por el span del botón
            if columna >= 4:  # Si la columna es mayor o igual a 4, reinicia la columna y pasa a la siguiente fila
                columna, fila = 0, fila + 1

        # Configura las columnas y filas del grid del marco de botones
        for i in range(4):
            frame_botones.grid_columnconfigure(i, weight=1)  # Configura el peso de las columnas
        for i in range(fila + 1):
            frame_botones.grid_rowconfigure(i, weight=1)  # Configura el peso de las filas

    # Método que maneja el clic de los botones
    def click_boton(self, valor):
        if valor == "=":  # Si el botón presionado es "="
            try:
                resultado = str(eval(self.entrada.get()))  # Evalúa la expresión en el campo de entrada y convierte el resultado en cadena
                self.entrada.config(state='normal')  # Habilita el campo de entrada
                self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
                self.entrada.insert(tk.END, resultado)  # Inserta el resultado en el campo de entrada
                self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
                self.resultado = resultado  # Almacena el resultado
                self.operacion_pendiente = True  # Marca que hay una operación pendiente
            except Exception as e:
                messagebox.showerror("Error", "Entrada no válida")  # Muestra un mensaje de error si la entrada no es válida
                self.entrada.config(state='normal')  # Habilita el campo de entrada
                self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
                self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
        elif valor == "C":  # Si el botón presionado es "C"
            self.entrada.config(state='normal')  # Habilita el campo de entrada
            self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
            self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
            self.resultado = None  # Reinicia el resultado
            self.operacion_pendiente = False  # Reinicia la operación pendiente
        elif valor == "←":  # Si el botón presionado es "←"
            self.entrada.config(state='normal')  # Habilita el campo de entrada
            self.entrada.delete(len(self.entrada.get()) - 1, tk.END)  # Elimina el último carácter del campo de entrada
            self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
        elif valor == "MC":  # Si el botón presionado es "MC"
            self.memoria = []  # Limpia la memoria
        elif valor == "MR":  # Si el botón presionado es "MR"
            messagebox.showinfo("Memoria", "Memoria: " + ", ".join(map(str, self.memoria)))  # Muestra el contenido de la memoria
        elif valor == "M+":  # Si el botón presionado es "M+"
            try:
                self.memoria.append(eval(self.entrada.get()))  # Agrega el valor actual a la memoria
            except Exception as e:
                messagebox.showerror("Error", "Entrada no válida")  # Muestra un mensaje de error si la entrada no es válida
        elif valor == "M-":  # Si el botón presionado es "M-"
            try:
                if self.memoria:  # Si hay valores en la memoria
                    self.memoria.pop()  # Elimina el valor más reciente de la memoria
                else:
                    messagebox.showinfo("Memoria", "La memoria está vacía")  # Muestra un mensaje si la memoria está vacía
            except Exception as e:
                messagebox.showerror("Error", "Operación fallida")  # Muestra un mensaje de error si la operación falla
        elif valor == "%":  # Si el botón presionado es "%"
            try:
                resultado = str(eval(self.entrada.get() + "/100"))  # Calcula el porcentaje dividiendo por 100
                self.entrada.config(state='normal')  # Habilita el campo de entrada
                self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
                self.entrada.insert(tk.END, resultado)  # Inserta el resultado en el campo de entrada
                self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
            except Exception as e:
                messagebox.showerror("Error", "Entrada no válida")  # Muestra un mensaje de error si la entrada no es válida
                self.entrada.config(state='normal')  # Habilita el campo de entrada
                self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
                self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
        elif valor == "1/x":  # Si el botón presionado es "1/x"
            try:
                resultado = str(eval("1/(" + self.entrada.get() + ")"))  # Calcula el inverso de la entrada
                self.entrada.config(state='normal')  # Habilita el campo de entrada
                self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
                self.entrada.insert(tk.END, resultado)  # Inserta el resultado en el campo de entrada
                self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
            except Exception as e:
                messagebox.showerror("Error", "Entrada no válida")  # Muestra un mensaje de error si la entrada no es válida
                self.entrada.config(state='normal')  # Habilita el campo de entrada
                self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
                self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
        elif valor == "x²":  # Si el botón presionado es "x²"
            try:
                resultado = str(eval(self.entrada.get() + "**2"))  # Calcula el cuadrado de la entrada
                self.entrada.config(state='normal')  # Habilita el campo de entrada
                self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
                self.entrada.insert(tk.END, resultado)  # Inserta el resultado en el campo de entrada
                self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
            except Exception as e:
                messagebox.showerror("Error", "Entrada no válida")  # Muestra un mensaje de error si la entrada no es válida
                self.entrada.config(state='normal')  # Habilita el campo de entrada
                self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
                self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
        elif valor == "√":  # Si el botón presionado es "√"
            try:
                resultado = str(eval("math.sqrt(" + self.entrada.get() + ")"))  # Calcula la raíz cuadrada de la entrada usando math.sqrt
                self.entrada.config(state='normal')  # Habilita el campo de entrada
                self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
                self.entrada.insert(tk.END, resultado)  # Inserta el resultado en el campo de entrada
                self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
            except Exception as e:
                messagebox.showerror("Error", "Entrada no válida")  # Muestra un mensaje de error si la entrada no es válida
                self.entrada.config(state='normal')  # Habilita el campo de entrada
                self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
                self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
        elif valor == "±":  # Si el botón presionado es "±"
            try:
                resultado = str(eval("-1*(" + self.entrada.get() + ")"))  # Cambia el signo del número de la entrada
                self.entrada.config(state='normal')  # Habilita el campo de entrada
                self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
                self.entrada.insert(tk.END, resultado)  # Inserta el resultado en el campo de entrada
                self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
            except Exception as e:
                messagebox.showerror("Error", "Entrada no válida")  # Muestra un mensaje de error si la entrada no es válida
                self.entrada.config(state='normal')  # Habilita el campo de entrada
                self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
                self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
        else:  # Si se presiona cualquier otro botón (números u operadores)
            if self.operacion_pendiente and valor not in ["/", "*", "-", "+"]:  # Si hay una operación pendiente y el valor no es un operador
                self.entrada.config(state='normal')  # Habilita el campo de entrada
                self.entrada.delete(0, tk.END)  # Limpia el campo de entrada
                self.operacion_pendiente = False  # Reinicia la bandera de operación pendiente
                self.entrada.config(state='disabled')  # Deshabilita el campo de entrada
            elif self.operacion_pendiente and valor in ["/", "*", "-", "+"]:  # Si hay una operación pendiente y el valor es un operador
                self.operacion_pendiente = False  # Reinicia la bandera de operación pendiente
            self.entrada.config(state='normal')  # Habilita el campo de entrada
            self.entrada.insert(tk.END, valor)  # Inserta el valor en el campo de entrada
            self.entrada.config(state='disabled')  # Deshabilita el campo de entrada

# Bloque principal que crea la ventana principal y ejecuta el bucle principal
if __name__ == "__main__":
    root = tk.Tk()  # Crea una instancia de la ventana principal
    calculadora = Calculadora(root)  # Crea una instancia de la calculadora
    root.mainloop()  # Inicia el bucle principal de la ventana
