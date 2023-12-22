# En el archivo main.py
import tkinter as tk
from tkinter import ttk
from methods import Register, Recognition
import os

class Main:
    def __init__(self):
        self.register = Register()
        self.recognition = Recognition()

    def clear_log(self):
        operative_system = os.name
        if operative_system == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    
    def show_main(self):
        root = tk.Tk()
        root.title("Sistema de Registro y Reconocimiento Facial")

        main_gui = MainGUI(root, self)

        root.mainloop()

    def registrar_persona(self, document_number, names, last_names, gender):
        self.clear_log()
        print("************************************************************************")
        print("*************************  Registrar persona  **************************")
        self.register.create_register_user(document_number, names, last_names, gender)
        print("************************************************************************")
        input()

    def identificar_personas(self):
        self.clear_log()
        print("************************************************************************")
        print("***********************  Identificar personas  *************************")
        self.recognition.catch_face()
        print("************************************************************************")
        input()

class MainGUI:
    def __init__(self, master, main_instance):
        self.master = master
        self.master.geometry("400x300")
        self.main_instance = main_instance

        self.create_widgets()

    def create_widgets(self):
        self.form_frame = ttk.Frame(self.master, padding="20")
        self.form_frame.pack(pady=20)

        ttk.Label(self.form_frame, text="Número de documento:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_documento = ttk.Entry(self.form_frame)
        self.entry_documento.grid(row=0, column=1, pady=5)

        ttk.Label(self.form_frame, text="Nombres:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_nombres = ttk.Entry(self.form_frame)
        self.entry_nombres.grid(row=1, column=1, pady=5)

        ttk.Label(self.form_frame, text="Apellidos:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_apellidos = ttk.Entry(self.form_frame)
        self.entry_apellidos.grid(row=2, column=1, pady=5)

        ttk.Label(self.form_frame, text="Género:").grid(row=3, column=0, sticky="w", pady=5)
        self.entry_genero = ttk.Entry(self.form_frame)
        self.entry_genero.grid(row=3, column=1, pady=5)

        self.btn_registrar = ttk.Button(self.master, text="Registrar persona", command=self.registrar_persona)
        self.btn_registrar.pack(pady=10)

        self.btn_identificar = ttk.Button(self.master, text="Identificar personas", command=self.identificar_personas)
        self.btn_identificar.pack(pady=10)

        self.btn_salir = ttk.Button(self.master, text="Salir", command=self.master.destroy)
        self.btn_salir.pack(pady=10)

    def registrar_persona(self):
        document_number = int(self.entry_documento.get())
        names = self.entry_nombres.get()
        last_names = self.entry_apellidos.get()
        gender = self.entry_genero.get()
        self.main_instance.registrar_persona(document_number, names, last_names, gender)

    def identificar_personas(self):
        self.main_instance.identificar_personas()

if __name__ == '__main__':
    main = Main()
    main.show_main()


