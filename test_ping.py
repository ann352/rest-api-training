import requests


def test_ping():                       # metoda musi się zaczynać od test_, wyslemy requwest do endpointu
    r = requests.get('http://18.184.234.77:8080/ping')    # url / endpoint, wrzucimy to w zmienną r to response z requestu
    assert r.status_code == 200       # i to sprawdzi , czy otrzymamy rzeczywiście 200
    assert r.text == "pong"           # wyciągamy respons body -> r.text sprawdzę, czy zwróci nam tekst, bo nie żądamy content-type jsona


def test_ping_accept_json():
    r = requests.get('http://18.184.234.77:8080/ping',
                     headers = {"Accept":"application/json"})  # endpoint + nagłówki, słownik z parametrami
    assert r.status_code == 200
    assert "application/json" in r.headers [ "content-type"]  # dopieramy się do konkretnych pól tablicy z headerami
    assert r.text == '{"reply":"pong!"}'  #sprawdzę, czy zwróci nam tekst, który powinien zwrócić