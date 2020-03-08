import requests
import pytest


NAME = "Ania"   # deklarujemy stałą

def test_greeting():                       # metoda musi się zaczynać od test_, wyslemy requwest do endpointu
    r = requests.get(pytest.HOST +'/greeting')    # url / endpoint phttp://18.184.234.77:8080, wrzucimy w conftest
    assert r.status_code == 200       #  to sprawdzi , czy otrzymamy rzeczywiście 200, dobrą prakt.są / oddzielnie
    # e tych testach nieoptymalne jest ciagle przepisywanie ip, dlatego go przeniesiemy
    assert r.json()['content'] == 'Hello, Stranger!'  #r json to klucz -> wiemy z kalkulatorka r.json to slownik - r.json()['content']

def test_greeting_by_name(): #  byloby ok, ale za duzo r = requests.get =(pytest.HOST +'/greeting'?name' + NAME
        r = requests.get(
            pytest.HOST + '/greeting',
            params = {'name' : NAME}      #tu wysylam query params, ktore chce dodac do URL {klucz : wartosc}
        )

        assert r.status_code == 200
        assert r.json()['content'] == f"Hello, {NAME}!"   #zeby operowac zawsze na obiekcie
