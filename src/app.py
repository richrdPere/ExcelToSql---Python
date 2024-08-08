# Librerias
import openpyxl
from tabulate import tabulate
import pandas as pd

from sqlalchemy import create_engine
from energias import acciones_energias as connect

import tkinter as tk
from tkinter import filedialog, messagebox

from main import process_excel_files


class Excel_to_MySQL:
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


#hazEl = connect.Acciones_Energias()

URL_SQL = 'mysql+pymysql://root:root@localhost:3306/energias_egemsa'

"""
1.-Diseño Grafico - Tkinter
"""
# url = ""
# raiz = Tk()

"""
1.- Guardar Datos en MySQL - Pandas
"""
def obtener_hojas_excel(ruta_archivo):
    xls = pd.ExcelFile(ruta_archivo)
    return xls.sheet_names

def excel_to_sql(file_path, nombre_hoja, db_connection_string, table_names):
    # Lee el archivo xlsx
    df = pd.read_excel(file_path, sheet_name=nombre_hoja)

    # Limpia los espacios extra en los nombres de las columnas
    df.columns = df.columns.str.strip()

    # Crear la conexión a la base de datos
    engine = create_engine(db_connection_string)

    # Sube los DataFrames a la base de datos
    for table_name in table_names:
        if table_name in df.columns:
            df[[table_name]].drop_duplicates().to_sql(table_name, con = engine, if_exists = 'replace', index = False)
        df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)
    
    print("Procesos Satisfactorio!!")

"""
2.- Obtener path del archivo - filedialog
"""
def abrirArchivo():

    # Obtener el path del archivo
    archivo = filedialog.askopenfilename(title="Abrir", initialdir="C:/", filetypes=(("Archivo Excel","*.xlsx"),("Archivo Excel","*.xls")))
    archivo = archivo.replace("/","\\")

    # Obtener el arreglo de tablas
    tablas_excel = obtener_hojas_excel(archivo)
    print(tablas_excel)

    # Guardarlo en la Base de Datos MySQL
    # excel_to_sql(archivo, 'Energías' , URL_SQL, tablas_excel)


# Boton - abrir
url = Button(raiz, text="Abrir archivo", command=abrirArchivo).pack()

raiz.mainloop()















"""
2.-Guardar Datos en MySQL - Pandas
"""

def excel_to_sql(file_path, nombre_hoja, db_connection_string, table_names):
    # Lee el archivo xlsx
    df = pd.read_excel(file_path, sheet_name=nombre_hoja)

    # Limpia los espacios extra en los nombres de las columnas
    df.columns = df.columns.str.strip()

    # Crear la conexión a la base de datos
    engine = create_engine(db_connection_string)

    # Sube los DataFrames a la base de datos
    for table_name in table_names:
        if table_name in df.columns:
            df[[table_name]].drop_duplicates().to_sql(table_name, con = engine, if_exists = 'replace', index = False)
        df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)
    
    print("Procesos Satisfactorio!!")


archivo2 = 'D:/Programas_python/ExcelToSql/Energias.xls'
# datos_energias=pd.read_excel(archivo, sheet_name='Energías')

# excel_to_sql(archivo, 'Energías' , URL_SQL, ['energias'])













# OPCION 1:
"""
# Ruta de los excels
archivo1 = '..\..\ExcelToSql\Energias.xls'
archivo2 = '..\..\ExcelToSql\MAC13G04 - Energías.xls'
archivo = 'D:/Programas_python/ExcelToSql/Energias.xls'

# datos_energias=pd.read_excel(archivo2, sheet_name='Energías', header=None)
datos_energias=pd.read_excel(archivo2, sheet_name='Energías')

# base de datos (MySQL)

# FUNCION

def excel_to_sql(file_path, nombre_hoja, db_connection_string, table_names):
    # Lee el archivo xlsx
    df = pd.read_excel(file_path, sheet_name=nombre_hoja)

    # Limpia los espacios extra en los nombres de las columnas
    df.columns = df.columns.str.strip()

    # Crear la conexión a la base de datos
    engine = create_engine(db_connection_string)

    # Sube los DataFrames a la base de datos
    for table_name in table_names:
        if table_name in df.columns:
            df[[table_name]].drop_duplicates().to_sql(table_name, con = engine, if_exists = 'replace', index = False)
        df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)
    
    print("Procesos Satisfactorio!!")

# Uso del método:

# 'mysql+pymysql://<usuario>:<contraseña>@<host>:<puerto>/<nombre_base_de_datos>'
# 'mysql+pymysql://root:0000@localhost:3306/base-de-datos'
# 'dialect+driver://username:password@host:port/database'


excel_to_sql(archivo2, 'Energías' ,'mysql+pymysql://root:root@localhost:3306/energias_egemsa', ['energias'])
"""

# # base de datos (SQL Server)

# # Librerias
# import pymssql
# import pyodbc

# # Conexion 1 
# try: 
#     conn = pymssql.connect(
#             server='DESKTOP-9EN7FOS\SQLEXPRESS', 
#             user='sa', 
#             password='root', 
#             database='BD_Energias',
#             as_dict=True)
    
#     print("Conexion exitosa")
# except pymssql.OperationalError as e:
#     print("Error de conexión:", e)


# Conexion 2
"""
conn = pyodbc.connect(
    Trusted_Connection='Yes',
    Driver = '{SQL Server Native Client 11.0}',
    Server = 'DESKTOP-9EN7FOS\SQLEXPRESS',
    Database = 'BD_Energias'
)
"""

# # Iteracion  - SQL Server
# cursor = conn.cursor()  
# cursor.execute('SELECT ID_COMUNA, DESCRIPCION FROM PEGAXUS_COMUNAS_PROVINCIAS ORDER BY DESCRIPCION;')  
# row = cursor.fetchone()  
# i = 1
# while row:  
#     print( str(i) + " - " + str(row[0]) + " " + str(row[1])  )
#     row = cursor.fetchone()  
#     i = i + 1
        
# cursor.close()
# conn.close()   

# Ruta de los excels
# archivo1 = '..\..\ExcelToSql\Energias.xls'
# archivo2 = '..\..\ExcelToSql\MAC13G04 - Energías.xls'



"""

mysql = "mysql://root:root@localhost?statusColor=&env=local&name=MySQL%20Localhost&tLSMode=0&usePrivateKey=false&safeModeLevel=0&advancedSafeModeLevel=0&driverVersion=0&showSystemSchemas=0&driverVersion=0&lazyload=False"


# print(datos_energias.columns)

# print(datos_energias['Timestamp'])

#print("Nro de columnas: ", datos_energias.shape[1]) # Muestra el numero de filas y columnas (filas, columnas)

# Obtener columnas
nro_cols = datos_energias.shape[1]
input_cols = []

# Pasando a numeros
for i in range(0, nro_cols):
    input_cols.append(i)

data_columns = pd.read_excel(archivo2, sheet_name="Energías", header=0, usecols=input_cols)
#print(data_columns.columns)

# Obteniendo un arreglo
headers = []
for header in data_columns.columns:
    headers.append(header)

print(headers)

# Recorriendo las filas
# nro_rows = datos_energias.shape[0]
# for row in range(1, nro_rows):
#     print(datos_energias[row])

# for row in range(1, datos_energias.):
#     print(row)
# hazEl.agregar()

# df.to_sql()
"""