import os
from excel_processor import process_excel_files as process_excels
from excel_processor import get_sheet_excel as get_tables
from excel_processor import excel_to_sql as to_sql

URL_SQL = 'mysql+pymysql://root:root@localhost:3306/energias_egemsa'

# from database import insert_data, example_table

def process_excel_files(folder_path):
    i=0
    for file_name, file_path in process_excels(folder_path):

        # iterador
        print(f'Processing {file_name} - URL: {file_path}')        

        # Obtener arreglo de las hojas para que sirvan como tablas

        tablas = get_tables(file_path)
        #print(tablas)

        # Enviar los datos a la BD
        to_sql(file_path, 'Energías', URL_SQL, tablas)

        


if __name__ == '__main__':
    folder_path = 'data'  # Por defecto, usa la carpeta 'data'
    process_excel_files(folder_path)
