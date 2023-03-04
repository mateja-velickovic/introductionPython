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
chaussure = {}

chaussure = {
    "taille" : 42,
    "marque" : "Nike",
    "race" : "berger-allemand"
}

chaussure.pop('race')

taille = chaussure["taille"]

print(chaussure)

# Op�rateurs logqiues

# if = si | elif = sinon si | else = sinon
# and = tout est vrai | or = au moins une vraie | not = condition fausse
# == �gal | != non �gal | < moins que | <= moins que ou �gal | > plus que | >= plus que ou �gal
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
# D�claration d'une variable, indication de la liste
for info in chaussure:
    print(info)

# D�claration d'une variable, tant que x < 4 sans inculre 10
for x in range(4, 10):
    print(x)

# Tant que intA est plus petit que intB, �ncr�menter intA de 1 et afficher l'incr�mentation
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