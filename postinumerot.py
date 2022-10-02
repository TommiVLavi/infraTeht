import code
import json
from typing import Optional

def get_postal_numbers(paikka: str) -> list:
    with open('postinumerot.json') as material:
        sisalto = material.read()

    postinumerot = json.loads(sisalto)
    koodit = []

    if paikka.upper() == "SMARTPOST" or paikka.upper() == "SMART POST":
        for koodi, nimi in postinumerot.items():
            if nimi == "SMARTPOST" or "SMART POST":
                koodit.append(koodi)
    else:
        for koodi, nimi in postinumerot.items():
            if nimi == paikka.upper():
                koodit.append(koodi)
    
    if koodit:
        koodit.sort()
        print(', '.join(koodit))
        print(len(koodit))
    else:
        print("Tuntematon postitoimipaikka")

    return koodit


if __name__== '__main__':
    paikka = input("Kirjoita postitoimipaikka: ")
    get_postal_numbers(paikka)