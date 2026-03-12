import tkinter as tk
from tkinter import ttk, messagebox

from modelos.vehiculo import Vehiculo
from servicios.garaje_servicio import GarajeServicio


class App:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Registro de Vehiculos - Garaje")
        self.root.geometry("620x400")
        self.root.resizable(False, False)

        self.servicio = GarajeServicio()  # capa de logica
        self.placa_var = tk.StringVar()
        self.marca_var = tk.StringVar()
        self.propietario_var = tk.StringVar()
        self.color_var = tk.StringVar()

        self._crear_widgets()
        self._actualizar_lista()

    def _crear_widgets(self) -> None:
        titulo = tk.Label(self.root, text="Gestion de Garaje", font=("Arial", 14, "bold"))
        titulo.grid(row=0, column=0, columnspan=3, pady=8)

        tk.Label(self.root, text="Placa:").grid(row=1, column=0, sticky="e", padx=5, pady=4)
        tk.Entry(self.root, textvariable=self.placa_var, width=22).grid(row=1, column=1, padx=5, pady=4, sticky="w")

        tk.Label(self.root, text="Marca:").grid(row=2, column=0, sticky="e", padx=5, pady=4)
        tk.Entry(self.root, textvariable=self.marca_var, width=22).grid(row=2, column=1, padx=5, pady=4, sticky="w")

        tk.Label(self.root, text="Propietario:").grid(row=3, column=0, sticky="e", padx=5, pady=4)
        tk.Entry(self.root, textvariable=self.propietario_var, width=22).grid(row=3, column=1, padx=5, pady=4, sticky="w")

        tk.Label(self.root, text="Color:").grid(row=4, column=0, sticky="e", padx=5, pady=4)
        tk.Entry(self.root, textvariable=self.color_var, width=22).grid(row=4, column=1, padx=5, pady=4, sticky="w")

        btn_agregar = tk.Button(
            self.root,
            text="Agregar vehiculo",
            command=self._agregar_vehiculo,
            width=16,
        )
        btn_agregar.grid(row=5, column=0, padx=5, pady=8)

        btn_limpiar = tk.Button(
            self.root,
            text="Limpiar",
            command=self._limpiar_campos,
            width=16,
        )
        btn_limpiar.grid(row=5, column=1, padx=5, pady=8, sticky="w")

        self.tree = ttk.Treeview(
            self.root,
            columns=("Placa", "Marca", "Propietario", "Color"),
            show="headings",
            height=10,
        )
        for heading, width in (("Placa", 110), ("Marca", 170), ("Propietario", 180), ("Color", 110)):
            self.tree.heading(heading, text=heading)
            self.tree.column(heading, width=width)

        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        scrollbar.grid(row=6, column=2, sticky="ns", pady=10)

        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def _agregar_vehiculo(self) -> None:
        placa = self.placa_var.get().strip()
        marca = self.marca_var.get().strip()
        propietario = self.propietario_var.get().strip()
        color = self.color_var.get().strip()

        if not placa or not marca or not propietario or not color:
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
            return

        vehiculo = Vehiculo(placa, marca, propietario, color)

        try:
            self.servicio.agregar_vehiculo(vehiculo)
        except ValueError as error:
            messagebox.showerror("Duplicado", str(error))
            return

        self._actualizar_lista()
        self._limpiar_campos()
        messagebox.showinfo("Exito", "Vehiculo agregado correctamente.")

    def _limpiar_campos(self) -> None:
        self.placa_var.set("")
        self.marca_var.set("")
        self.propietario_var.set("")
        self.color_var.set("")

    def _actualizar_lista(self) -> None:
        for row in self.tree.get_children():
            self.tree.delete(row)

        for vehiculo in self.servicio.obtener_vehiculos():
            self.tree.insert("", tk.END, values=(vehiculo.placa, vehiculo.marca, vehiculo.propietario, vehiculo.color))
