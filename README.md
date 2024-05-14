addBook() : Ajoute un livre
updateBook(): Met à jour un livre
deleteBook() : Supprime un livre (Supprime le livre si il a été loué par quelqu'un)
	Paramètres utilisés : title,author,editor,year,type


addUser() : Ajoute un utilisateur
updateUser() : Met à jour un utlisateur
deleteUser(): Supprime un utilisateur (Remet les livres loués en disponible)
	Paramètres utilisés : name,surname,age,email,type


searchBook() : Recherche un livre
	Paramètres utilisés : title,author,type - Les 3 ne sont pas obligatoires et 3 caractères de recherche minimum par paramètres


checkBookAvailable() : Affiche tous les livres disponibles et empruntés ainsi que le nom de l'emprunteur.


checkUserBook() : Affiche le nombre de livres ainsi que le nom des livres empruntés de chaque utilisateur.


reserveBook() : Réserve un livre
	Paramètres utilisés pour trouver l'utilisateur : name, surname, email
	Paramètres utilisés pour trouver le livre : title, author


dropBook() : Retourne un livre
	Paramètres utilisés pour trouver l'utilisateur : name, surname, email
	Paramètres utilisés pour trouver le livre : title, author

On peut afficher les utilisateurs à l'aide de la méthode showBook() ou showUser()

Pour retrouver les utilisateurs dans les fonctions, on utilise ses informations (nom,prenom,email...).
Pour retrouver les livres dans les fonctions, on utilise ses informations (titre,auteur etc...).
Les recherches de livres et d'utilisateurs ne sont sensiblent à la casse, toutes les recherches sont mises en minuscules avant pour éviter les conflits.

Les fonctions permettent de :
- Gérer les utilisateurs (ajout, modification, suppression)
- Gérer les livres (ajout, modification, suppression)
- Gérer les emprunts et les retours
- Afficher les livres ainsi que leurs statut
- Rechercher les livres avec leur titre, auteur ou genre (3 caractères de recherche minimum)

Les fonctions convertissent d'abord le contenu du fichier .json en dictionnaire avec la commande .load(), on traite ensuite les informations dans ce dernier, une fois les modifications faites, on les reinjectes dans le fichier .json avec la commande .dump().


Tests:

Créer un utilisateur
(Modifier ce dernier)
Créer un livre
(Modifier ce dernier)
Le louer avec un Utilisateur
Afficher tous les livres disponibles et non disponibles
Afficher la liste des livres louer pour chaques utilisateurs
Le Retourner
Supprimer l'utilisateur
Supprimer le livre
