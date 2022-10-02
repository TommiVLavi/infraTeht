import code
import json
from typing import Optional

def get_postal_numbers(paikka: str) -> list:
    with open('postinumerot.json') as material:
        sisalto = material.read()

    postinumerot = json.loads(sisalto)


    
    koodit = []

    for koodi, nimi in postinumerot.items():
        if nimi == paikka.upper():
            koodit.append(koodi)
    
    if koodit:
        koodit.sort()
        print(', '.join(koodit))
    else:
        print("Tuntematon postitoimipaikka")

    return koodit


if __name__== '__main__':
    paikka = input("Kirjoita postitoimipaikka: ")
    get_postal_numbers(paikka)