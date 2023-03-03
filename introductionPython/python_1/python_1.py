# Déclarer une liste
reseauxSociaux = ["Instagram", "Tiktok"]

# Ajouter un élément 
reseauxSociaux.append("Snapchat")

# Enlever un élément  
reseauxSociaux.remove("Instagram")

# Afficher la liste dans la console
print (reseauxSociaux)

# Connaître la longueur de la liste
print(len(reseauxSociaux))



# Déclarer une variable
instagram = ("Instagram")

# Afficher la variable5
print(instagram)

# Connaître la longueur du string
print(len(instagram))

# Afficher la valeur dans le 3ème index de la liste [commence par 0]
print (instagram[3])

# Trier les éléments par ordre alphabétique
reseauxSociaux.sort()
print(reseauxSociaux)

# Créer/afficher/supprimer un dictionnaire
chaussure = {
    "taille" : 42,
    "marque" : "Nike",
    "race" : "berger-allemand"
}

del chaussure["race"]

print (chaussure)

# Supprimer une paire clé-valeur
del infos_labradoodle["origine"]