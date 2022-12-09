import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

filname = Path(__file__).parent / "Sivilstand.json"
data = []

# opner json fil og lagrer data i variable: "data"
with open(filname, encoding="utf-8") as fil:
    data = json.load(fil)

# henter ut informasjon fra json fil
data_length = len(data["dataset"]["value"])
#finner kategorier
categories = data["dataset"]["dimension"]["EkteskStatus"]["category"]["label"]
#finner antall data per kategori
data_per_category = data_length // len(categories)
#finner punkt ein må dele dataen. 
#Siden all data uavhengig av kategori ligg i ei liste må ein velge dei første x antall verdiene til kvar kategori
split_points = [i for i in range(0, data_length - 1, data_per_category)]
data_in_categories = [data["dataset"]["value"][ind:ind + data_per_category] for ind in split_points]

#finner årstall som ein brukar som x-verdiar i grafen
x = list(data["dataset"]["dimension"]["Tid"]["category"]["index"].keys())

#fyller inn manglende år og data som null.
i = 0
for year in list(range(int(min(x)),int(max(x)))):
    if x.count(year) <= 0:
        x.insert(i, year)
        data_in_categories[0].insert(i, None)
        data_in_categories[1].insert(i, None)
        data_in_categories[2].insert(i, None)
        data_in_categories[3].insert(i, None)
        data_in_categories[4].insert(i, None)
    i += 1

#tegner grafen
plt.plot(x, data_in_categories[0])
plt.plot(x, data_in_categories[1])
plt.plot(x, data_in_categories[2])
plt.plot(x, data_in_categories[3])
plt.plot(x, data_in_categories[4])

#gir navn til tittler, akser, funksjonsnavn og farge
plt.legend([list(categories.values())[0], list(categories.values())[1], list(categories.values())[2], list(categories.values())[3], list(categories.values())[4]])
plt.xlabel("Årstall")
plt.ylabel("Antall (millioner)")
plt.title(data["dataset"]["dimension"]["EkteskStatus"]["label"])

# Ordner slik at en ser kvar 10´ande verdi på x-aksen
plt.xticks(np.arange(0, len(x)+1, 10), rotation = 90)

#viser grafen
plt.show()
