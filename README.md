# Oppgave2-Samarbeid
Oppgåve 2 sammarbeid IT Heildag Haust 2022

Dette programmet bruker Matplotlib til å tegne grafer fra data gitt i CSV og JSON filer.

# Krav
For å kunne kjøre dette programmet trenger du følgende:

Python 3.6 eller nyere
Matplotlib 3.2 eller nyere
JSON og CSV-moduler for Python

# Installasjon

Installer Python på din maskin.

Installer Matplotlib ved å kjøre følgende kommando i en terminal:

Copy code
pip install matplotlib
Installer JSON- og CSV-modulene ved å kjøre følgende kommando i en terminal:
Copy code
pip install json csv
Last ned og installer dette programmet ved å klone Git-repositoriet eller laste ned og pakke ut ZIP-filen.

# Bruk
Åpne en terminal og naviger til mappen der programmet er installert.

Kjør programmet ved å skrive følgende kommando:

Copy code
python matplotlib_graf_generator.py <data-fil> <graf-type>
Erstatt <data-fil> med navnet på datafilen (enten en CSV-fil eller en JSON-fil), og erstatt <graf-type> med en av følgende verdier:

linje: Tegner en linjegraf
søyler: Tegner en søylegraf
pie: Tegner en pai-diagram
Eksempel:

Copy code
python matplotlib_graf_generator.py data.csv linje
