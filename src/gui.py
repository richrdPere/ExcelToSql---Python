import os
import tkinter as tk
from tkinter import filedialog, messagebox
from main import process_excel_files

class ExcelProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Processor")
        
        self.label = tk.Label(root, text="Seleccione la carpeta con los archivos Excel:")
        self.label.pack(pady=10)
        
        self.select_button = tk.Button(root, text="Seleccionar carpeta", command=self.select_folder)
        self.select_button.pack(pady=10)
        
        self.process_button = tk.Button(root, text="Procesar archivos", command=self.process_files)
        self.process_button.pack(pady=10)
        
        self.folder_path = None

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            messagebox.showinfo("Carpeta seleccionada", f"Carpeta seleccionada: {self.folder_path}")

    def process_files(self):
        if not self.folder_path:
            messagebox.showwarning("Advertencia", "Debe seleccionar una carpeta primero.")
            return
        
        try:
            # Aquí llamamos a la función principal para procesar los archivos
            process_excel_files(self.folder_path)
            messagebox.showinfo("Éxito", "Archivos procesados exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar los archivos: {str(e)}")

def main():
    root = tk.Tk()
    app = ExcelProcessorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
