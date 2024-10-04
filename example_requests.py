import sqlite3

# Connexion à la base de données
con = sqlite3.connect("patoche.db")
cursor = con.cursor()

# Sélectionner tous les clients
print("Tous les clients :")
cursor.execute("SELECT * FROM Clients")
clients = cursor.fetchall()
for client in clients:
    print(client)

# Récupérer les commandes d'un client spécifique (client_id = 1)
print("\nCommandes du client avec client_id = 1 :")
client_id = 1
cursor.execute("SELECT * FROM Commandes WHERE client_id = ?", (client_id,))
commandes = cursor.fetchall()
for commande in commandes:
    print(commande)

# Mettre à jour l'adresse e-mail d'un client spécifique (client_id = 1)
nouveau_email = 'sokprir.hem@exemple.com'
cursor.execute("UPDATE Clients SET email = ? WHERE id = ?", (nouveau_email, client_id))
con.commit()
print(f"\nAdresse e-mail du client mise à jour {nouveau_email} du client {client_id}.")

# Supprimer une commande spécifique (commande_id = 1)
commande_id = 1
cursor.execute("DELETE FROM Commandes WHERE id = ?", (commande_id,))
con.commit()
print("\nCommande supprimée.")

# Fermer la connexion
con.close()
