# Réalisé par Gauthier GALON

import json

def addBook():
	title,author,editor,year,type = input("Quel est le titre ? : "),input("Quel est le nom de l'auteur ? : "),input("Quel est le nom de l'editeur ? : "),input("Quel est l'année de création' ? : "),input("Quel est le genre ? : ")
	file = open("livres.json", "r",encoding='utf-8')
	books = json.load(file)
	file.close()
	for book in books:
		if book["titre"].lower() == title.lower() and book["auteur"].lower() == author.lower() and book["editeur"].lower() == editor.lower() and book["annee"].lower() == year.lower() and book["genre"].lower() == type.lower():
			print("Livre déjà présent")
			return 1
	newBook = {"titre": title,"auteur": author,"editeur": editor,"annee": year,"genre": type, "disponible": "True"}
	books.append(newBook)
	file = open("livres.json", "w",encoding='utf-8')
	json.dump(books, file, indent=2, ensure_ascii=False)
	file.close()
	print("Livre ajouté")
	return 0

def updateBook():
	title,author = input("Quel est le titre ? : "),input("Quel est le nom de l'auteur ? : ")
	newTitle, newAuthor, newEditor, newYear, newType = input("Quel est le nouveau titre ? : "),input("Quel est le nouveau nom de l'auteur ? : "),input("Quel est le nouveau nom de l'editeur ? : "),input("Quel est la nouvel année de création' ? : "),input("Quel est le nouveau genre ? : ")
	file = open("livres.json", "r",encoding='utf-8')
	books = json.load(file)
	file.close()
	for book in books:
		if book["titre"].lower() == title.lower() and book["auteur"].lower() == author.lower():
			book["titre"] = newTitle
			book["auteur"] = newAuthor
			book["editeur"] = newEditor
			book["annee"] = newYear
			book["genre"] = newType
			file = open("livres.json", "w",encoding='utf-8')
			json.dump(books, file, indent=2, ensure_ascii=False)
			file.close()
			print("Livre modifié")
			return 0
	print("Livre non trouvé")
	return 1
	
def deleteBook():
	title,author = input("Quel est le titre ? : "),input("Quel est le nom de l'auteur ? : ")
	file = open("livres.json", "r",encoding='utf-8')
	books = json.load(file)
	file.close()
	file = open("utilisateurs.json", "r",encoding='utf-8')
	users = json.load(file)
	file.close()
	i = 0
	for book in books:
		if book["titre"].lower() == title.lower() and book["auteur"].lower() == author.lower():
			for user in users:
				for j in range (len(user["livres"])) :
					if user["livres"][j] == book["titre"] :
						user["livres"].pop(j)
			books.pop(i)
			file = open("utilisateurs.json", "w",encoding='utf-8')
			json.dump(users, file, indent=2, ensure_ascii=False)
			file.close()
			file = open("livres.json", "w",encoding='utf-8')
			json.dump(books, file, indent=2, ensure_ascii=False)
			print("Livre supprimé")
			file.close()
			return 0
		i += 1
	print("Livre non trouvé")
	return 1

def searchBook():
	file = open("livres.json", "r",encoding='utf-8')
	books = json.load(file)
	file.close()
	title,author,type = input("Quel est le titre du livre ? : "), input("Quel est le nom de l'auteur ? : "), input("Quel est le genre du livre ? : ")
	print("Occurence(s) avec le titre " + title + " : ")
	for book in books:
		if title.lower() in book["titre"].lower() and len(title) >= 3:
			print(book["titre"] + ", écrit en " + str(book["annee"]) + " par " + book["auteur"] + " et édité par " + book["editeur"] + " du genre " + book["genre"], end="")
			if book["disponible"] == "True":
				print(", Disponible")
			else :
				print(", non Disponible")
	print("")
	print("Occurence(s) avec le nom d'auteur " + author + " : ")
	for book in books:
		if author.lower() in book["auteur"].lower() and len(author) >= 3:
			print(book["titre"] + ", écrit en " + str(book["annee"]) + " par " + book["auteur"] + " et édité par " + book["editeur"] + " du genre " + book["genre"], end="")
			if book["disponible"] == "True":
				print(", Disponible")
			else :
				print(", non Disponible")
	print("")
	print("Occurence(s) avec le genre " + type + " : ")
	for book in books:
		if type.lower() in book["genre"].lower() and len(type) >= 3:
			print(book["titre"] + ", écrit en " + str(book["annee"]) + " par " + book["auteur"] + " et édité par " + book["editeur"] + " du genre " + book["genre"], end="")
			if book["disponible"] == "True":
				print(", Disponible")
			else :
				print(", non Disponible")

def checkBookAvailable():
	file = open("livres.json", "r",encoding='utf-8')
	books = json.load(file)
	file.close()
	print("Livres disponibles :")
	for book in books:
		if book["disponible"] == "True":
			print(book["titre"] + ", écrit en " + str(book["annee"]) + " par " + book["auteur"] + " et édité par " + book["editeur"] + " du genre " + book["genre"])
	print("Livres empruntés :")
	file = open("utilisateurs.json", "r",encoding='utf-8')
	users = json.load(file)
	file.close()
	for book in books:
		if book["disponible"] == "False":
			print(book["titre"] + ", écrit en " + str(book["annee"]) + " par " + book["auteur"] + " et édité par " + book["editeur"] + " du genre " + book["genre"], end="")
			for user in users:
				if book["titre"] in user["livres"]:
					print(", Emprunté par " + user["nom"] + " " + user["prénom"])

def reserveBook():
	name, surname, email = input("Entrez votre nom : "),input("Entrez votre prénom : "),input("Entrez votre email : "),
	title, author = input("Entrez le titre du livre : "),input("Entrez le nom de l'auteur : "),
	file = open("livres.json", "r",encoding='utf-8')
	books = json.load(file)
	file.close()
	file = open("utilisateurs.json", "r",encoding='utf-8')
	users = json.load(file)
	file.close()
	for book in books:
		if book["titre"].lower() == title.lower() and book["auteur"].lower() == author.lower():
			if book["disponible"] == "False":
				print("Livre déjà emprunté")
				return 1
			for user in users:
				if user["nom"].lower() == name.lower() and user["prénom"].lower() == surname.lower() and user["adresse email"].lower() == email.lower():
					if user["type"] == "normal" and len(user["livres"]) >= 2 or user["type"] == "étudiant" and len(user["livres"]) >= 3:
						print("Trop de livres empruntés")
						return 1
					user["livres"].append(book["titre"])
					book["disponible"] = "False"
					file = open("utilisateurs.json", "w",encoding='utf-8')
					json.dump(users, file, indent=2, ensure_ascii=False)
					file.close()
					file = open("livres.json", "w",encoding='utf-8')
					json.dump(books, file, indent=2, ensure_ascii=False)
					file.close()
					print("Livre réservé")
					return 0
	print("Utilisateur ou livre non trouvé")
	return 1

def dropBook():
	name,surname,email = input("Quel est votre nom ? : "),input("Quel est votre prénom ? : "),input("Quel est votre adresse email ? : ")
	title,author = input("Quel est le titre ? : "),input("Quel est le nom de l'auteur ? : ")
	file = open("livres.json", "r",encoding='utf-8')
	books = json.load(file)
	file.close()
	file = open("utilisateurs.json", "r",encoding='utf-8')
	users = json.load(file)
	file.close()
	for book in books:
		if book["titre"].lower() == title.lower() and book["auteur"].lower() == author.lower():
			if book["disponible"] == "True":
				print("Livre déjà disponible")
				return 1
			for user in users:
				if user["nom"].lower() == name.lower() and user["prénom"].lower() == surname.lower() and user["adresse email"].lower() == email.lower():
					if book["titre"] not in user["livres"]:
						print("Livre emprunté par quelqu'un d'autre")
						return 1
					for i in range (len(user["livres"])):
						if user["livres"][i] == book["titre"]:
							user["livres"].pop(i)
					book["disponible"] = "True"
					file = open("utilisateurs.json", "w",encoding='utf-8')
					json.dump(users, file, indent=2, ensure_ascii=False)
					file.close()
					file = open("livres.json", "w",encoding='utf-8')
					json.dump(books, file, indent=2, ensure_ascii=False)
					file.close()
					print("Livre retourné")
					return 0
	print("Utilisateur ou livre non trouvé")
	return 1



def addUser():
	name,surname,age,email,type = input("Quel est le nom ? : "),input("Quel est le prénom ? : "),input("Quel âge a-t-il ? : "),input("Quel adresse email ? : "),input("Quel type de personne ? : ")
	file = open("utilisateurs.json", "r",encoding='utf-8')
	users = json.load(file)
	file.close()
	for user in users:
		if user["nom"].lower() == name.lower() and user["prénom"].lower() == surname.lower() and user["age"].lower() == age.lower() and user["adresse email"].lower() == email.lower() and user["type"].lower() == type.lower():
			print("Utilisateur déjà présent")
			return 1
	newUser = {"nom": name,"prénom": surname,"age": age,"adresse email": email,"type": type, "livres": []}
	users.append(newUser)
	file = open("utilisateurs.json", "w",encoding='utf-8')
	json.dump(users, file, indent=2, ensure_ascii=False)
	file.close()
	print("Utilisateur ajouté")
	return 0
	

def updateUser():
	name,surname,email = input("Quel est le nom ? : "),input("Quel est le prénom ? : "),input("Quel adresse email ? : ")
	newName,newSurname,newAge,newEmail,newType = input("Quel est le nouveau nom ? : "),input("Quel est le nouveau prénom ? : "),input("Quel nouvel âge a-t-il ? : "),input("Quel nouvelle adresse email ? : "),input("Quel nouveau type de personne ? : ")
	file = open("utilisateurs.json", "r",encoding='utf-8')
	users = json.load(file)
	file.close()
	for user in users:
		if user["nom"].lower() == name.lower() and user["prénom"].lower() == surname.lower() and user["adresse email"].lower() == email.lower():
			user["nom"] = newName
			user["prénom"] = newSurname
			user["age"] = newAge
			user["adresse email"] = newEmail
			user["type"] = newType
			file = open("utilisateurs.json", "w",encoding='utf-8')
			json.dump(users, file, indent=2, ensure_ascii=False)
			file.close()
			print("Utilisateur modifié")
			return 0
	print("Utilisateur non trouvé")
	return 1

def deleteUser():
	name,surname,email = input("Quel est le nom ? : "),input("Quel est le prénom ? : "),input("Quel adresse email ? : ")
	file = open("utilisateurs.json", "r",encoding='utf-8')
	users = json.load(file)
	file.close()
	file = open("livres.json", "r",encoding='utf-8')
	books = json.load(file)
	file.close()
	i = -1
	for user in users:
		i += 1
		if user["nom"].lower() == name.lower() and user["prénom"].lower() == surname.lower() and user["adresse email"].lower() == email.lower():
			for book in books:
				if book["titre"] in user["livres"]:
					book["disponible"] = "True"

			users.pop(i)
			file = open("utilisateurs.json", "w",encoding='utf-8')
			json.dump(users, file, indent=2, ensure_ascii=False)
			file.close()
			file = open("livres.json", "w",encoding='utf-8')
			json.dump(books, file, indent=2, ensure_ascii=False)
			file.close()
			print("Utilisateur supprimé")
			return 0
	print("Utilisateur non trouvé")
	return 1

def checkUsersBook():
	file = open("utilisateurs.json", "r",encoding='utf-8')
	users = json.load(file)
	file.close()
	print("Liste des emprunts de tous les utilisateurs : ")
	for user in users:
		if len(user["livres"]) >= 1:
			print (user["nom"] + " " + user["prénom"] + " - " + str(len(user["livres"])) + " Livre(s) emprunté(s) : ", end="")
			for book in user["livres"]:
				print(book + ", ", end="")
			print("")	


print("Que désirez vous faire ?")
print("1 - Chercher un livre")
print("2 - Emprunter un livre")
print("3 - Retourner un livre")
print("4 - Gestion des livres")
print("5 - Gestion des utilisateurs")
put = input()
if put == "1":
	searchBook()
if put == "2":
	reserveBook()
if put == "3":
	dropBook()
if put == "4":
	print("")
	print("1 - Ajouter un livre")
	print("2 - Modifier un livre")
	print("3 - Supprimer un livre")
	print("4 - Afficher disponibilité des livres")
	put = input()
	if put == "1":
		addBook()
	if put == "2":
		updateBook()
	if put == "3":
		deleteBook()
	if put == "4":
		checkBookAvailable()
if put == "5":
	print("")
	print("1 - Ajouter un utilisateur")
	print("2 - Modifier un utilisateur")
	print("3 - Supprimer un utilisateur")
	print("4 - Afficher livre(s) emprunté(s) par utilisateur")
	put = input()
	if put == "1":
		addUser()
	if put == "2":
		updateUser()
	if put == "3":
		deleteUser()
	if put == "4":
		checkUsersBook()
