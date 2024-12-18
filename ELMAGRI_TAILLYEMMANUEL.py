import csv
import matplotlib.pyplot as plt

Gaz = []
Nucléaire = []
Eolien = []
Solaire = []
Hydraulique = []
Fioul = []
Charbon = []
Consommation = []

def saut_ligne(value):
    try:
        return float(value) if value else 0
    except ValueError:
        return 0

with open("RTE_2022.csv", mode='r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    
    for row in reader:
        if row[0] == "France":
            Eolien.append(saut_ligne(row[11]))
            Gaz.append(saut_ligne(row[9]))
            Nucléaire.append(saut_ligne(row[10]))
            Solaire.append(saut_ligne(row[12]))
            Hydraulique.append(saut_ligne(row[13]))
            Fioul.append(saut_ligne(row[7]))
            Charbon.append(saut_ligne(row[8]))
            Consommation.append(saut_ligne(row[4]))

total_Eolien = sum(Eolien)
total_Gaz = sum(Gaz)
total_Nucleaire = sum(Nucléaire)
total_Solaire = sum(Solaire)
total_Hydraulique = sum(Hydraulique)
total_Fioul = sum(Fioul)
total_Charbon = sum(Charbon)
total_Consommation = sum(Consommation)

labels = ['Eolien', 'Gaz', 'Nucléaire', 'Solaire', 'Hydraulique', 'Fioul', 'Charbon', 'Consommation']
sizes = [total_Eolien, total_Gaz, total_Nucleaire, total_Solaire, total_Hydraulique, total_Fioul, total_Charbon, total_Consommation]

colors = ['green', '#D8BFD8', '#FFFFE0', '#B0C4DE', '#FFBF00', '#E6A9EC', '#FFB347', 'red']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)

plt.title('Comparaison de la consommation par rapport à la production d\'énerie')

plt.axis('equal')
plt.show()


labels = ['Eolien', 'Gaz', 'Nucléaire', 'Solaire', 'Hydraulique', 'Fioul', 'Charbon']
sizes = [total_Eolien, total_Gaz, total_Nucleaire, total_Solaire, total_Hydraulique, total_Fioul, total_Charbon]

colors = ['green', '#D8BFD8', '#FFFFE0', '#B0C4DE', '#FFBF00', '#E6A9EC', '#FFB347']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)

plt.title('Production d\'énergie en 2022')

plt.axis('equal')
plt.show()

