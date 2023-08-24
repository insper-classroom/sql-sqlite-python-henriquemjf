import sqlite3

import db.db_utils as db_utils

conn = sqlite3.connect("db/database_alunos.db")
cursor = conn.cursor()

estudantes = [    ("Ana Silva", "Computação",2019 ),
    ("Pedro Mendes","Física", 2021),
    ("Carla Souza", "Computação", 2020),
    ("João Alves", "Matemática", 2018),
    ("Maria Oliveira", "Química", 2022)]

db_utils.create_table('Estudantes')

db_utils.add_records('Estudantes', estudantes)

db_utils.update_records('Estudantes', 'AnoDeIngresso', 2018)

db_utils.select_record('Estudantes')

db_utils.delete_records('Estudantes', 3)
