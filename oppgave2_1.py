import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

filname = Path(__file__).parent / "Sivilstand.json"
data = []

with open(filname, encoding="utf-8") as fil:
    data = json.load(fil)

data_length = len(data["dataset"]["value"])
categories = data["dataset"]["dimension"]["EkteskStatus"]["category"]["label"]
data_per_category = data_length // len(categories)

split_points = [i for i in range(0, data_length - 1, data_per_category)]
data_in_categories = [data["dataset"]["value"][ind:ind + data_per_category] for ind in split_points]

x = list(data["dataset"]["dimension"]["Tid"]["category"]["index"].keys())

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

plt.plot(x, data_in_categories[0])
plt.plot(x, data_in_categories[1])
plt.plot(x, data_in_categories[2])
plt.plot(x, data_in_categories[3])
plt.plot(x, data_in_categories[4])
plt.legend([list(categories.values())[0], list(categories.values())[1], list(categories.values())[2], list(categories.values())[3], list(categories.values())[4]])
plt.xlabel("Årstall")
plt.ylabel("Antall (millioner)")
plt.xticks(rotation = 90)
plt.xticks(np.arange(0, len(x)+1, 10))
plt.show()
