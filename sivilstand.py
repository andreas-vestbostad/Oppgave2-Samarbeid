from pathlib import Path

filnavn = Path(__file__).parent / "Sivilstand.json"

with open(filnavn, encoding="utf-8") as fil:
  dictionary = json.load(fil)
