import csv
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

filnavn = Path(__file__).parent / "Befolkning.csv"

# Lister for å ta vare på alle årstall og befolkningsstørrelser
aarstall = []
befolkning = []

# Åpner fil og legger til verdier i hver liste
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    tittel = next(filinnhold)
    overskrifter = next(filinnhold)
  
    for rad in filinnhold:
        aarstall.append(int(rad[0]))
        befolkning.append(int(rad[1]))

# Tegner grafen
plt.plot(aarstall, befolkning)
plt.title(str(tittel[0]))
plt.xlabel("Årstall")
plt.ylabel("Befolking (millioner)")
plt.yticks(np.arange(0, max(befolkning), step=250000))
plt.grid()
plt.show()
