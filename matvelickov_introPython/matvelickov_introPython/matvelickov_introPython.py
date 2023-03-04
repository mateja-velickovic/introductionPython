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
chaussure = {}

chaussure = {
    "taille" : 42,
    "marque" : "Nike",
    "race" : "berger-allemand"
}

chaussure.pop('race')

taille = chaussure["taille"]

print(chaussure)

# Opérateurs logqiues

# if = si | elif = sinon si | else = sinon
# and = tout est vrai | or = au moins une vraie | not = condition fausse
# == égal | != non égal | < moins que | <= moins que ou égal | > plus que | >= plus que ou égal
a = True
b = False

# Si a est vrai mais b est faux
if a and not b:
  # alors
  print("1")

# Sinon si a ou b est vrai
elif a or b:
  # alors
  print("2")
  
# Sinon
else:
  print("3")

races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
# Déclaration d'une variable, indication de la liste
for info in chaussure:
    print(info)

# Déclaration d'une variable, tant que x < 4 sans inculre 10
for x in range(4, 10):
    print(x)

# Tant que intA est plus petit que intB, încrémenter intA de 1 et afficher l'incrémentation
intA = 0
intB = 25

while intA < intB:
    intA += 1
    print(intA)

# Fonction avec valeurs a+b, qui retourne la valeur de a+b
def calcul(a,b):
    c = a+b
    return c

print (calcul(1,2))