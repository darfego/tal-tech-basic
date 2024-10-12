import tkinter as tk  # Importa la biblioteca tkinter para crear interfaces gráficas
from tkinter import messagebox  # Importa el submódulo messagebox de tkinter para mostrar cuadros de diálogo
import csv  # Importa la biblioteca csv para manejar archivos CSV
import re  # Importa la biblioteca re para usar expresiones regulares
import math # Importa la biblioteca math para realizar operaciones matemáticas
# Variable global para verificar si la sesión ya está iniciada
sesion_iniciada = False
# Define una clase llamada LoginApp para crear la aplicación de inicio de sesión
class LoginApp:
    # Método constructor de la clase LoginApp, se llama automáticamente al crear una instancia de la clase
    def __init__(self, root):
        # Variable de clase para verificar si la sesión ya está iniciada
        global sesion_iniciada
        self.root = root  # Asigna la ventana principal (root) a la variable de instancia self.root
        self.root.title("Login")  # Establece el título de la ventana principal a "Login"
        self.root.geometry("300x400")  # Establece el tamaño de la ventana principal a 300x400 píxeles
        self.root.configure(bg="#f5f5f5")  # Configura el color de fondo de la ventana principal a un color gris claro
        
        # Si la sesión ya está iniciada, mostrar el menú principal directamente
        if sesion_iniciada:
            self.menu_principal()
        else:
            # Crea y configura una etiqueta (Label) para el título "Login"
            self.titulo = tk.Label(root, text="Login", font=("Arial", 24), bg="#f5f5f5")
            self.titulo.pack(pady=20)  # Empaqueta la etiqueta en la ventana con un espacio vertical de 20 píxeles

            # Crea y configura una etiqueta y un campo de entrada (Entry) para el usuario
            self.label_usuario = tk.Label(root, text="Usuario:", font=("Arial", 14), bg="#f5f5f5")
            self.label_usuario.pack(pady=5)  # Empaqueta la etiqueta en la ventana con un espacio vertical de 5 píxeles
            self.entrada_usuario = tk.Entry(root, font=("Arial", 14))  # Crea el campo de entrada para el usuario
            self.entrada_usuario.pack(pady=5)  # Empaqueta el campo de entrada en la ventana con un espacio vertical de 5 píxeles

            # Crea y configura una etiqueta y un campo de entrada para la contraseña
            self.label_contrasena = tk.Label(root, text="Contraseña:", font=("Arial", 14), bg="#f5f5f5")
            self.label_contrasena.pack(pady=5)  # Empaqueta la etiqueta en la ventana con un espacio vertical de 5 píxeles
            self.entrada_contrasena = tk.Entry(root, font=("Arial", 14), show="*")  # Crea el campo de entrada para la contraseña con asteriscos
            self.entrada_contrasena.pack(pady=5)  # Empaqueta el campo de entrada en la ventana con un espacio vertical de 5 píxeles

            # Crea y configura un botón para iniciar sesión
            self.boton_login = tk.Button(root, text="Iniciar sesión", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.iniciar_sesion)
            self.boton_login.pack(pady=20)  # Empaqueta el botón en la ventana con un espacio vertical de 20 píxeles

            # Crea y configura un botón para registrarse
            self.boton_registrar = tk.Button(root, text="Registrarse", font=("Arial", 14), bg="#2196F3", fg="white", command=self.registrarse)
            self.boton_registrar.pack(pady=10)  # Empaqueta el botón en la ventana con un espacio vertical de 10 píxeles

    # Método para iniciar sesión
    def iniciar_sesion(self):
        usuario = self.entrada_usuario.get()  # Obtiene el valor ingresado en el campo de entrada de usuario
        contrasena = self.entrada_contrasena.get()  # Obtiene el valor ingresado en el campo de entrada de contraseña

        # Abre el archivo CSV de usuarios en modo lectura
        with open('usuarios.csv', mode='r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=',')  # Crea un lector CSV que usa la coma como delimitador
            for fila in lector_csv:  # Itera sobre cada fila en el archivo CSV
                if fila[0] == usuario and fila[1] == contrasena:  # Verifica si el usuario y la contraseña coinciden
                    messagebox.showinfo("Éxito", "Inicio de sesión exitoso")  # Muestra un mensaje de éxito
                    global sesion_iniciada 
                    sesion_iniciada = True  # Marca la sesión como iniciada
                    self.menu_principal()  # Llama al método para mostrar el menú principal
                    return  # Sale del método

        # Si las credenciales no coinciden, muestra un mensaje de error
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    # Método para registrarse
    def registrarse(self):
        usuario = self.entrada_usuario.get()  # Obtiene el valor ingresado en el campo de entrada de usuario
        contrasena = self.entrada_contrasena.get()  # Obtiene el valor ingresado en el campo de entrada de contraseña

        # Verifica que los campos de usuario y contraseña no estén vacíos
        if not usuario or not contrasena:
            messagebox.showerror("Error", "Todos los campos son obligatorios")  # Muestra un mensaje de error
            return  # Sale del método

        # Abre el archivo CSV de usuarios en modo append (agregar)
        with open('usuarios.csv', mode='a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv, delimiter=',')  # Crea un escritor CSV que usa la coma como delimitador
            escritor_csv.writerow([usuario, contrasena])  # Escribe una nueva fila con el usuario y la contraseña

        # Muestra un mensaje de éxito
        messagebox.showinfo("Éxito", "Registro exitoso")

    # Método para mostrar el menú principal
    def menu_principal(self):
        # Crea una nueva ventana para el menú principal
        self.menu = tk.Toplevel(self.root)  # Crea una nueva ventana secundaria
        self.menu.title("Menú Principal")  # Establece el título de la ventana del menú principal
        self.menu.geometry("300x300")  # Establece el tamaño de la ventana del menú principal
        self.menu.configure(bg="#f5f5f5")  # Configura el color de fondo de la ventana del menú principal

        # Crea y configura una etiqueta para el título "Menú Principal"
        self.label_menu = tk.Label(self.menu, text="Menú Principal", font=("Arial", 18), bg="#f5f5f5")
        self.label_menu.pack(pady=20)  # Empaqueta la etiqueta en la ventana con un espacio vertical de 20 píxeles

        # Crea y configura un botón para abrir la calculadora
        self.boton_calculadora = tk.Button(self.menu, text="Calculadora", font=("Arial", 14), command=self.abrir_calculadora)
        self.boton_calculadora.pack(pady=10)  # Empaqueta el botón en la ventana con un espacio vertical de 10 píxeles

        # Crea y configura un botón para abrir el formulario de registro
        self.boton_registro = tk.Button(self.menu, text="Registro", font=("Arial", 14), command=self.abrir_registro)
        self.boton_registro.pack(pady=10)  # Empaqueta el botón en la ventana con un espacio vertical de 10 píxeles

        # Crea y configura un botón para abrir la serie de Fibonacci
        self.boton_fibonacci = tk.Button(self.menu, text="Serie Fibonacci", font=("Arial", 14), command=self.abrir_fibonacci)
        self.boton_fibonacci.pack(pady=10)  # Empaqueta el botón en la ventana con un espacio vertical de 10 píxeles

    # Método placeholder para abrir la calculadora
    def abrir_calculadora(self):
        self.calculadora = tk.Toplevel(self.menu)  # Crea una nueva ventana secundaria (Toplevel) y la asigna a self.calculadora
        self.calculadora.title("Calculadora") # Establece el título de la nueva ventana a "Calculadora"
        self.calculadora.geometry("375x700") # Establece el tamaño de la nueva ventana a 375x700 píxeles
        self.calculadora.configure(bg="#ffffff") # Configura el color de fondo de la nueva ventana a blanco
        Calculadora(self.calculadora) # Crea una instancia de la clase Calculadora y le pasa la nueva ventana como argumento

    # Método para abrir la ventana del formulario de registro
    def abrir_registro(self):
        self.registro = tk.Toplevel(self.menu) # Crea una nueva ventana secundaria (Toplevel) y la asigna a self.registro
        self.registro.title("Formulario") # Establece el título de la nueva ventana a "Formulario"
        self.registro.geometry("400x400") # Establece el tamaño de la nueva ventana a 400x400 píxeles
        self.registro.configure(bg="#ffffff") # Configura el color de fondo de la nueva ventana a blanco
        Formulario(self.registro) # Crea una instancia de la clase Formulario y le pasa la nueva ventana como argumento

    # Método para abrir la ventana de la serie de Fibonacci
    def abrir_fibonacci(self):
        self.fibonacci = tk.Toplevel(self.menu) # Crea una nueva ventana secundaria (Toplevel) y la asigna a self.fibonacci
        self.fibonacci.title("Serie Fibonacci") # Establece el título de la nueva ventana a "Serie Fibonacci"
        self.fibonacci.geometry("400x300") # Establece el tamaño de la nueva ventana a 400x300 píxeles
        self.fibonacci.configure(bg="#f5f5f5") # Configura el color de fondo de la nueva ventana a un color gris claro

        # Crea y configura una etiqueta para el título "Serie de Fibonacci"
        self.label_fibonacci = tk.Label(self.fibonacci, text="Serie de Fibonacci", font=("Arial", 18), bg="#f5f5f5")
        self.label_fibonacci.pack(pady=20) # Empaqueta la etiqueta en la ventana con un espacio vertical de 20 píxeles

        # Crea y configura una etiqueta y un campo de entrada para el número de términos
        self.label_terminos = tk.Label(self.fibonacci, text="Número de términos:", font=("Arial", 14), bg="#f5f5f5")
        self.label_terminos.pack(pady=5) # Empaqueta la etiqueta en la ventana con un espacio vertical de 5 píxeles
        self.entrada_terminos = tk.Entry(self.fibonacci, font=("Arial", 14)) # Crea el campo de entrada para el número de términos
        self.entrada_terminos.pack(pady=5) # Empaqueta el campo de entrada en la ventana con un espacio vertical de 5 píxeles

        # Crea y configura un botón para generar la serie de Fibonacci
        self.boton_generar = tk.Button(self.fibonacci, text="Generar", font=("Arial", 14), command=self.generar_fibonacci)
        self.boton_generar.pack(pady=20) # Empaqueta el botón en la ventana con un espacio vertical de 20 píxeles

    # Método para generar la serie de Fibonacci
    def generar_fibonacci(self):
        num_terminos = int(self.entrada_terminos.get()) # Obtiene el número de términos ingresado por el usuario y lo convierte a entero
        a, b = 0, 1 # Inicializa los dos primeros términos de la serie de Fibonacci
        serie = [] # Crea una lista vacía para almacenar la serie de Fibonacci
        for _ in range(num_terminos): # Itera el número de veces indicado por el usuario
            serie.append(a)  # Agrega el término actual a la lista de la serie
            a, b = b, a + b # Calcula el siguiente término de la serie
        # Muestra un cuadro de diálogo con la serie de Fibonacci generada
        messagebox.showinfo("Serie Fibonacci", ", ".join(map(str, serie)))
    
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
class Formulario:
    # Método constructor que inicializa la interfaz del formulario
    def __init__(self, root):
        self.root = root  # Asigna la ventana principal a la variable root
        self.root.title("Formulario")  # Establece el título de la ventana
        self.root.configure(bg="#f5f5f5")  # Configura el color de fondo de la ventana
        self.root.geometry("400x400")  # Establece el tamaño de la ventana
        self.root.resizable(False, False)  # Impide que la ventana se redimensione

        # Crear y configurar una etiqueta de título
        self.titulo = tk.Label(root, text="Registro", font=("Arial", 24), bg="#f5f5f5")
        self.titulo.pack(pady=20)  # Agrega un espacio alrededor del título

        # Crear y configurar una etiqueta y un campo de entrada para el nombre
        self.label_nombre = tk.Label(root, text="Nombre:", font=("Arial", 14), bg="#f5f5f5")
        self.label_nombre.pack(pady=5)  # Agrega un espacio alrededor de la etiqueta de nombre
        self.entrada_nombre = tk.Entry(root, font=("Arial", 14), width=30)  # Crea un campo de entrada para el nombre
        self.entrada_nombre.pack(pady=5)  # Agrega un espacio alrededor del campo de entrada de nombre

        # Crear y configurar una etiqueta y un campo de entrada para el correo
        self.label_correo = tk.Label(root, text="Correo:", font=("Arial", 14), bg="#f5f5f5")
        self.label_correo.pack(pady=5)  # Agrega un espacio alrededor de la etiqueta de correo
        self.entrada_correo = tk.Entry(root, font=("Arial", 14), width=30)  # Crea un campo de entrada para el correo
        self.entrada_correo.pack(pady=5)  # Agrega un espacio alrededor del campo de entrada de correo

        # Crear y configurar una etiqueta y un campo de entrada para el teléfono
        self.label_telefono = tk.Label(root, text="Teléfono:", font=("Arial", 14), bg="#f5f5f5")
        self.label_telefono.pack(pady=5)  # Agrega un espacio alrededor de la etiqueta de teléfono
        self.entrada_telefono = tk.Entry(root, font=("Arial", 14), width=30)  # Crea un campo de entrada para el teléfono
        self.entrada_telefono.pack(pady=5)  # Agrega un espacio alrededor del campo de entrada de teléfono

        # Crear y configurar un botón para enviar los datos del formulario
        self.boton_enviar = tk.Button(root, text="Enviar", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.enviar)
        self.boton_enviar.pack(pady=20)  # Agrega un espacio alrededor del botón de enviar

    # Método que se ejecuta al presionar el botón de enviar
    def enviar(self):
        nombre = self.entrada_nombre.get()  # Obtiene el valor del campo de entrada de nombre
        correo = self.entrada_correo.get()  # Obtiene el valor del campo de entrada de correo
        telefono = self.entrada_telefono.get()  # Obtiene el valor del campo de entrada de teléfono

        # Verifica que todos los campos estén llenos
        if not nombre or not correo or not telefono:
            messagebox.showerror("Error", "Todos los campos son obligatorios")  # Muestra un mensaje de error si algún campo está vacío
            return  # Detiene la ejecución del método si algún campo está vacío

        # Usa una expresión regular para validar el formato del correo
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            messagebox.showerror("Error", "Correo no válido")  # Muestra un mensaje de error si el correo no es válido
            return  # Detiene la ejecución del método si el correo no es válido

        # Verifica que el teléfono comience con '3', tenga 10 dígitos y solo contenga números
        if not telefono.startswith('3') or len(telefono) != 10 or not telefono.isdigit():
            messagebox.showerror("Error", "Teléfono no válido. Debe comenzar con '3' y tener 10 dígitos")  # Muestra un mensaje de error si el teléfono no es válido
            return  # Detiene la ejecución del método si el teléfono no es válido

        # Abre (o crea si no existe) el archivo CSV en modo append (agregar)
        with open('datos_formulario.csv', 'a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)  # Crea un escritor de CSV
            escritor_csv.writerow([nombre, correo, telefono])  # Escribe una fila con los datos del formulario
        
        # Muestra un mensaje de éxito con los datos ingresados
        messagebox.showinfo("Éxito", f"Nombre: {nombre}\nCorreo: {correo}\nTeléfono: {telefono}")
        
        # Limpia los campos de entrada del formulario
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_correo.delete(0, tk.END)
        self.entrada_telefono.delete(0, tk.END)

# Bloque principal para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = LoginApp(root)  # Crea una instancia de la clase LoginApp
    root.mainloop()  # Inicia el bucle principal de la ventana