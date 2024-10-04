import sqlite3, os

if os.path.exists("patoche.db"):
    os.remove("patoche.db")
    print("Fichier patoche.db supprimé.")
else:
    print("Fichier patoche.db introuvable.")

print("Création du Fichier patoche.db")
con = sqlite3.connect("patoche.db")
cursor = con.cursor()

#Créer une table Clients (id , nom, prenom, email, date_inscription)
cursor.execute('''CREATE TABLE IF NOT EXISTS Clients
                 (id INTEGER PRIMARY KEY, 
                 nom TEXT, 
                 prenom TEXT, 
                 email TEXT, 
                 date_inscription TEXT)''')
#Créer une table Commandes (id, client_id, produit, date_commande) avec client_id clé étrangère de la table Clients
cursor.execute('''CREATE TABLE IF NOT EXISTS Commandes
                 (id INTEGER PRIMARY KEY, 
                 client_id INTEGER,
                 produit TEXT, 
                 date_commande TEXT,
                 FOREIGN KEY (client_id) REFERENCES Clients (id))''')

# Insérer des données Clients
cursor.execute("INSERT INTO Clients (nom, prenom, email, date_inscription) VALUES ('HEM', 'Patrick', 'hp5454@hotmail.fr', DATETIME('now'))")
cursor.execute("INSERT INTO Clients (nom, prenom, email, date_inscription) VALUES ('HEM', 'Thierry', 'tp5454@hotmail.fr', DATETIME('now'))")
cursor.execute("INSERT INTO Commandes (client_id, produit, date_commande) VALUES (1, 'Whey 300g', DATETIME('now'))")
cursor.execute("INSERT INTO Commandes (client_id, produit, date_commande) VALUES (2, 'Whey 1000g', DATETIME('now'))")


# Valider les modifications
con.commit()

# Fermer la connexion
con.close()
