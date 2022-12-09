import csv
import matplotlib.pyplot as plt
filnavn = "Skilsmisser og ekteskap.csv"

# Lister for å ta vare på alle årstall og befolkningsstørrelser
aarstall = []
skilsmisser = []
ingaatt = []
x1 = []
x2 = []

with open(filnavn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    tittel = next(filinnhold)
    V = next(filinnhold)
    I = next(filinnhold)
    S = next(filinnhold)
    
    Vo = V.pop(0)
    Io = I.pop(0)
    So = S.pop(0)

    for i in V:
        aarstall.append(int(i))
    for i in I:
        if(i=='..'):
            i = 0
        ingaatt.append(int(i))
    for i in S:
        if(i=='..'):
            i = 0
        skilsmisser.append(int(i))

    print(aarstall)
    
    for l in aarstall:
        if l not in x1:
            x1.append(l+2)
        if l not in x2:
            x2.append(l-2)
            
# Tegner grafen
plt.style.use('seaborn')
plt.bar(x1,skilsmisser,4)
plt.bar(x2,ingaatt,4)
plt.title(tittel[0])
plt.legend(["Skilsmisser","Ekteskap inngått"])
