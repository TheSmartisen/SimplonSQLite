import sqlite3
import csv

# Connexion à la base de données SQLite
con = sqlite3.connect("patoche.db")
cursor = con.cursor()

# Sélectionner toutes les données de toutes les tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Boucle pour récupérer les données de chaque table et les exporter vers des fichiers CSV
for table in tables:
    table_name = table[0]

    # Récupérer toutes les données de la table actuelle
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Récupérer les noms de colonnes
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cursor.fetchall()]  # Le nom des colonnes est dans la deuxième position de chaque ligne

    # Créer un fichier CSV pour chaque table
    csv_filename = f"{table_name}.csv"
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Écrire les noms des colonnes
        writer.writerow(columns)

        # Écrire toutes les données
        writer.writerows(rows)

    print(f"Les données de la table {table_name} ont été exportées dans {csv_filename}.")

# Fermer la connexion
con.close()
