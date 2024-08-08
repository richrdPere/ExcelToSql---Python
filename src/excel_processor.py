import pandas as pd
from sqlalchemy import create_engine
import os

def process_excel_files(folder_path):
    """
    1ra forma
    # for file_name in os.listdir(folder_path):
    #     if (file_name.endswith('.xlsx') or file_name.endswith('.xls')):
    #         file_path = os.path.join(folder_path, file_name)
    #         df = pd.read_excel(file_path)
    #         yield file_name, df
    """
    for file_name in os.listdir(folder_path):
        if (file_name.endswith('.xlsx') or file_name.endswith('.xls')):
            file_path = os.path.join(folder_path, file_name)
            file_path = file_path.replace("/","\\")
            yield file_name, file_path

def get_sheet_excel(ruta_archivo):
    sheets = pd.ExcelFile(ruta_archivo)
    sheets = sheets.sheet_names
    sheets = [s for s in sheets if not s.startswith('|PRIVATE|') and not s.startswith('Presentation Sheet')]

    return sheets


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
    
    print("Carga de datos realizado satisfactoriamente!!")