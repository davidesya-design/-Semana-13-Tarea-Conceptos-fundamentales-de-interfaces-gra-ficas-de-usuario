import tkinter as tk
## Archivo principal que inicia la aplicación y muestra la ventana principal de Tkinter
from ui.app_tkinter import App

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
