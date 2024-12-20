#Affichons la population d'Auxerre en 2008

import csv
table = []
with open('donnees_2008.csv', newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        table.append(row)

ville = "Auxerre"
population2008 = 0

for row in table[1:]: 
    if row[6].strip() == ville:
        population2008 = row[7] 

if population2008:
    print(f"La population municipale d'Auxerre en 2008 était de {population2008} habitants.")
else:
    print(f"La ville '{ville}' n'a pas été trouvée dans le fichier.")

#Affichons la population d'Auxerre en 2016

import csv
table = []
with open('donnees_2016.csv', newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        table.append(row)


ville = "Auxerre"
population2016 = 0

for row in table[1:]: 
    if row[6].strip() == ville:
        population2016 = row[7] 

if population2016:
    print(f"La population municipale d'Auxerre en 2016 était de {population2016} habitants.")
else:
    print(f"La ville '{ville}' n'a pas été trouvée dans le fichier.")

#Affichons la population d'Auxerre en 2021

import csv
table = []
with open('donnees_2021.csv', newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        table.append(row)


ville = "89024" # le code commune de la ville d'Auxerre est 89024
population2021 = 0

for row in table[1:]: 
    if row[2].strip() == ville:
        population2021 = row[5] 

if population2021:
    print(f"La population municipale d'Auxerre en 2021 était de {population2021} habitants.")
else:
    print(f"La ville '{ville}' n'a pas été trouvée dans le fichier.")

#Affichons la population d'Auxerre en 2023

import csv
table = []
with open('donnees_2023.csv', newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        table.append(row)


ville = "Auxerre"
population2023 = 0

for row in table[1:]: 
    if row[7].strip() == ville:
        population2023 = row[8] 

if population2023:
    print(f"La population municipale d'Auxerre en 2023 était de {population2023} habitants.")
else:
    print(f"La ville '{ville}' n'a pas été trouvée dans le fichier.")

#Affichons la population de Sens en 2008

import csv
table = []
with open('donnees_2008.csv', newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        table.append(row)

ville = "Sens"
population2008 = 0

for row in table[1:]: 
    if row[6].strip() == ville:
        population2008 = row[7] 

if population2008:
    print(f"La population municipale de Sens en 2008 était de {population2008} habitants.")
else:
    print(f"La ville '{ville}' n'a pas été trouvée dans le fichier.")

#Affichons la population de Sens en 2016

import csv
table = []
with open('donnees_2016.csv', newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        table.append(row)

ville = "Sens"
population2016 = 0

for row in table[1:]: 
    if row[6].strip() == ville:
        population2016 = row[7] 

if population2016:
    print(f"La population municipale de Sens en 2016 était de {population2016} habitants.")
else:
    print(f"La ville '{ville}' n'a pas été trouvée dans le fichier.")

#Affichons la population de Sens en 2021

import csv
table = []
with open('donnees_2021.csv', newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        table.append(row)

ville = "89387"
population2021 = 0

for row in table[1:]: 
    if row[2].strip() == ville:
        population2021 = row[5] 

if population2021:
    print(f"La population municipale de Sens en 2021 était de {population2021} habitants.")
else:
    print(f"La ville '{ville}' n'a pas été trouvée dans le fichier.")

#Affichons la population de Sens en 2023

import csv
table = []
with open('donnees_2023.csv', newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        table.append(row)


ville = "Sens"
population2023 = 0

for row in table[1:]: 
    if row[7].strip() == ville:
        population2023 = row[8] 

if population2023:
    print(f"La population municipale de Sens en 2023 était de {population2023} habitants.")
else:
    print(f"La ville '{ville}' n'a pas été trouvée dans le fichier.")

#Affichons la population totale du département de l'Yonne en 2008

import csv
table = []
with open('donnees_2008.csv', newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        table.append(row)

code_departement = "89"
population_total2008 = 0

for row in table[1:]:
    if row[2].strip() == code_departement: 
        population_total2008 += int(row[9]) 

print(f"La population totale du département de l'Yonne (89) en 2008 etait de {population_total2008} habitants.")

#Affichons la population totale du département de l'Yonne en 2016

import csv
table = []
with open('donnees_2016.csv', newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        table.append(row)

code_departement = "89"
population_total2016 = 0

for row in table[1:]:
    if row[2].strip() == code_departement: 
        population_total2016 += int(row[9]) 

print(f"La population totale du département de l'Yonne (89) en 2016 etait de {population_total2016} habitants.")

#Affichons la population totale du département de l'Yonne en 2021

import csv
table = []
with open('donnees_2021.csv', newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        table.append(row)

code_departement = "89"
population_total2021 = 0

for row in table[1:]:
    if row[1].strip() == code_departement: 
        population_total2021 += int(row[5]) 

print(f"La population totale du département de l'Yonne (89) en 2021 etait de {population_total2021} habitants.")

#Affichons la population totale du département de l'Yonne en 2023

import csv
table = []
with open('donnees_2023.csv', newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        table.append(row)

code_departement = "89"
population_total2023 = 0

for row in table[1:]:
    if row[2].strip() == code_departement: 
        population_total2023 += int(row[10]) 

print(f"La population totale du département de l'Yonne (89) en 2023 etait de {population_total2023} habitants.")

#Affichage du graphique

import matplotlib.pyplot as plt

année = [2008, 2016, 2021, 2023]
population_auxerre = [36856, 34846, 35554, 34778]
population_yonne = [353611, 350970, 344022, 340738] 
population_sens = [25899, 25913, 27203, 27034]

plt.figure(figsize=(10, 6))
plt.plot(année, population_auxerre, marker='o', label="Population d'Auxerre", color='blue')
#plt.plot(année, population_yonne, marker='o', label="Population de l'Yonne", color='green')
plt.plot(année, population_sens, marker='o', label="Population de Sens", color='red')

plt.title("Évolution de la population d'Auxerre et de l'Yonne", fontsize=14)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Population", fontsize=12)
plt.grid(True, linestyle='--', alpha=1)
plt.legend(fontsize=12)
plt.xticks(année)

plt.show()