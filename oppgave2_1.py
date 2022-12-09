#Importerer nødvendige bibliotek
import csv
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

#Finner filen ved hjelp av pathlib
filnavn = Path(__file__).parent / "Befolkning.csv"

# Lister for å ta vare på alle årstall og befolkningsstørrelser
aarstall = []
befolkning = []

# Åpner fil og legger til verdier i hver liste
with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    #Hopper over første linje i filen og legger til linjen i variabelen "tittel"
    tittel = next(filinnhold)
    #Hopper over andre linje i filen og legger til linjen i variabelen "overskrifter"
    overskrifter = next(filinnhold)
    
    #Loop som går gjennom hver line i filen og legger den første kolonnen til i "aarstall", og den andre kollenen til i "befolkning"
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
