# Kirjoita postinumerot-moduulin testit tähän tiedostoon
 
# postitoimipaikan nimellä löytyy vain yksi postinumero (Muuruvesi)
# postitoimipaikan nimellä löytyy useita postinumeroita
# postitoimipaikan nimellä ei löydy lainkaan postinumeroita.

from postinumerot import get_postal_numbers

def test_get_one_num_from_name():
    
    assert get_postal_numbers("Muuruvesi") == ["73460"]

def test_get_several_numbers():
    
    lista = get_postal_numbers("Helsinki")
    assert len(lista) >= 2

def test_get_absolutely_none():
    
    assert get_postal_numbers("Jotain") == []