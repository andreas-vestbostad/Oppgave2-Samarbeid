import csv
import matplotlib.pyplot as plt
import numpy as np
import json
from pathlib import Path

csv_fil = Path(__file__).parent / "Befolkning.csv"
json_fil = Path(__file__).parent / "Sivilstand.json"

# Lister for å ta vare på alle årstall, befolkningsstørrelser og json fil
aarstall = []
befolkning = []
innhold = []

# Åpner csv-fil og legger til verdier i hver liste
with open(csv_fil, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    tittel = next(filinnhold)
    overskrifter = next(filinnhold)
  
    for rad in filinnhold:
        aarstall.append(int(rad[0]))
        befolkning.append(int(rad[1]))

with open(json_fil, encoding="utf-8") as fil:
    innhold = json.load(fil)

innhold_lengde = len(innhold["dataset"]["value"])
kategorier = innhold["dataset"]["dimension"]["EkteskStatus"]["category"]["label"]
innhold_per_kategori = innhold_lengde // len(kategorier)
skille_punkt = [i for i in range(0, innhold_lengde - 1, innhold_per_kategori)]
innhold_i_kategori = [innhold["dataset"]["value"][ind:ind + innhold_per_kategori] for ind in skille_punkt]

x = list(innhold["dataset"]["dimension"]["Tid"]["category"]["index"].keys())
aarstall  = [str(x) for x in aarstall]

i = 0
for year in list(range(int(min(x)),int(max(x)))):
    if x.count(year) <= 0:
        x.insert(i, year)
        innhold_i_kategori[0].insert(i, None)
        innhold_i_kategori[1].insert(i, None)
        innhold_i_kategori[2].insert(i, None)
        innhold_i_kategori[3].insert(i, None)
        innhold_i_kategori[4].insert(i, None)
    i += 1

i = 0
for year in list(range(x[0],int(x[len(x)-1]))):
    if aarstall.count(year) <= 0:
        aarstall.insert(i, year)
        befolkning.insert(i, None)
    i += 1

# Tegner grafen
plt.plot(aarstall, befolkning)
plt.plot(x, innhold_i_kategori[0])
plt.plot(x, innhold_i_kategori[1])
plt.plot(x, innhold_i_kategori[2])
plt.plot(x, innhold_i_kategori[3])
plt.plot(x, innhold_i_kategori[4])
plt.legend(["Befolkning", list(kategorier.values())[0], list(kategorier.values())[1], list(kategorier.values())[2], list(kategorier.values())[3], list(kategorier.values())[4]])
plt.title("Befolkning og Sivilstand")
plt.xlabel("Årstall")
plt.ylabel("Antall (millioner)")
plt.xticks(np.arange(0, len(x)+1, 10))
plt.xticks(rotation = 75)
plt.grid()
plt.show()
