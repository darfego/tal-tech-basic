import tkinter as tk  # Importa la biblioteca tkinter para crear interfaces gráficas
from tkinter import messagebox  # Importa messagebox de tkinter para mostrar cuadros de diálogo
import csv  # Importa la biblioteca csv para manejar archivos CSV
import re  # Importa la biblioteca re para usar expresiones regulares

# Define una clase llamada Formulario que representa el formulario de registro
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

# Bloque principal que crea la ventana y ejecuta el bucle principal
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    formulario = Formulario(root)  # Crea una instancia de la clase Formulario
    root.mainloop()  # Inicia el bucle principal de la ventana
