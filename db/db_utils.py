import sqlite3 

conn = sqlite3.connect("db/database_alunos.db")
cursor = conn.cursor()

def create_table(table_name):
    cursor.execute(f""" 
CREATE TABLE IF NOT EXISTS {table_name} (
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               Nome TEXT NOT NULL,
               Curso TEXT NOT NULL,
               AnoDeIngresso INTEGER  
               );
               """)
    return conn.commit()

def select_record(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    return print(cursor.fetchall())

def add_records(table_name, records_list):
    cursor.executemany(f"""
                INSERT INTO {table_name} 
                (Nome, Curso, AnoDeIngresso)
                  VALUES (?, ? ,?)
                        """, records_list)
    return conn.commit()

def update_records(table_name, column, value_updated):
    cursor.execute(f"UPDATE {table_name} SET {column} = {value_updated}")
    return conn.commit()

def delete_records(table_name, id_number):
    cursor.execute(f"DELETE FROM {table_name} WHERE ID = ?", (f"{id_number}"))
    return conn.commit()