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

#git grafen ein predefined stil
plt.style.use("seaborn")

#tegner grafen
fig, axs = plt.subplots(2,3)

axs[0, 0].plot(x, data_in_categories[0])
axs[0, 0].set_title(list(categories.values())[0])
axs[0, 0].set_xticks(np.arange(0, len(x)+1, 50))
axs[0, 0].set_xlabel("Årstall")
axs[0, 0].set_ylabel("Antall (millioner)")
plt.setp(axs[0, 0].get_xticklabels(),rotation=45)

axs[0, 1].plot(x, data_in_categories[1], 'tab:orange')
axs[0, 1].set_title(list(categories.values())[1])
axs[0, 1].set_xticks(np.arange(0, len(x)+1, 50))
axs[0, 1].set_xlabel("Årstall")
axs[0, 1].set_ylabel("Antall (millioner)")
plt.setp(axs[0, 1].get_xticklabels(),rotation=45)

axs[0, 2].plot(x, data_in_categories[2], 'tab:blue')
axs[0, 2].set_title(list(categories.values())[2])
axs[0, 2].set_xticks(np.arange(0, len(x)+1, 50), rotation = 90)
axs[0, 2].set_xlabel("Årstall")
axs[0, 2].set_ylabel("Antall")
plt.setp(axs[0, 2].get_xticklabels(),rotation=45)

axs[1, 0].plot(x, data_in_categories[3], 'tab:green')
axs[1, 0].set_title(list(categories.values())[3])
axs[1, 0].set_xticks(np.arange(0, len(x)+1, 50), rotation = 90)
axs[1, 0].set_xlabel("Årstall")
axs[1, 0].set_ylabel("Antall")
plt.setp(axs[1, 0].get_xticklabels(),rotation=45)

axs[1, 1].plot(x, data_in_categories[4], 'tab:red')
axs[1, 1].set_title(list(categories.values())[4])
axs[1, 1].set_xticks(np.arange(0, len(x)+1, 50), rotation = 90)
axs[1, 1].set_xlabel("Årstall")
axs[1, 1].set_ylabel("Antall")
plt.setp(axs[1, 1].get_xticklabels(),rotation=45)

axs[1, 2].plot(x, data_in_categories[0])
axs[1, 2].plot(x, data_in_categories[1], 'tab:orange')
axs[1, 2].plot(x, data_in_categories[2], 'tab:blue')
axs[1, 2].plot(x, data_in_categories[3], 'tab:green')
axs[1, 2].plot(x, data_in_categories[4], 'tab:red')
axs[1, 2].set_title("Sivilstand")
axs[1, 2].set_xticks(np.arange(0, len(x)+1, 50), rotation = 300)
axs[1, 2].set_xlabel("Årstall")
axs[1, 2].set_ylabel("Antall (millioner)")
plt.setp(axs[1, 2].get_xticklabels(),rotation=45)

#meir mellomrom mellom grafer
plt.tight_layout()

#viser grafen
plt.show()
