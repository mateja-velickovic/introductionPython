# D�clarer une liste
reseauxSociaux = ["Instagram", "Tiktok"]

# Ajouter un �l�ment 
reseauxSociaux.append("Snapchat")

# Enlever un �l�ment  
reseauxSociaux.remove("Instagram")

# Afficher la liste dans la console
print (reseauxSociaux)

# Conna�tre la longueur de la liste
print(len(reseauxSociaux))



# D�clarer une variable
instagram = ("Instagram")

# Afficher la variable5
print(instagram)

# Conna�tre la longueur du string
print(len(instagram))

# Afficher la valeur dans le 3�me index de la liste [commence par 0]
print (instagram[3])

# Trier les �l�ments par ordre alphab�tique
reseauxSociaux.sort()
print(reseauxSociaux)

# Cr�er/afficher/supprimer un dictionnaire
chaussure = {
    "taille" : 42,
    "marque" : "Nike",
    "race" : "berger-allemand"
}

del chaussure["race"]

print (chaussure)

# Supprimer une paire cl�-valeur
del infos_labradoodle["origine"]