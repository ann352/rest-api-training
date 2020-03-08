import requests
import pytest

ACCOUNT_NAME = "Aniaaa003"

@pytest.fixture()  #przed każdym testem wyczyscimy to co jest
def empty_db():  #wysyłamy requesty więc import bibloioteke requests
    requests.delete(
        pytest.HOST + "/accounts/delete",     # import pytest  , musi być / -> "/accounts/delete
        params = {'account': ACCOUNT_NAME}

    )


def test_account_e2e(empty_db): #testy sprawdzające funkcjonalności e2e, definicja bez podkreslnika, odwolam sie do ogolnej metody z innego pliku, ale do prywatnych nie
    # given         #bdd
    _create_account()
    # when
    _withdraw_from_account(200)
    # and
    _pay_to_account(300)
    # then
    assert _get_balance() == 1100

    #zeby pare razy wykonac test uzyjemy fixture

def _create_account():
    requests.put(  #put, bo wpłacamy
        pytest.HOST + "/accounts/create",
        json={"name" : ACCOUNT_NAME}

    )

def _withdraw_from_account(ammount):
    requests.post(
        pytest.HOST + "/accounts/withdraw", #url
        params={"account" : ACCOUNT_NAME},           #przekazemy jako parametr slownik
        json={"amount": ammount}

    )


def _pay_to_account(ammount):
    requests.post(
        pytest.HOST + "/accounts/pay",  # url
        params={"account": ACCOUNT_NAME},  # przekazemy jako parametr slownik
        json={"amount": ammount}

    )

def _get_balance():
    r = requests.get(
        pytest.HOST + "/accounts", # musze podac dla tego parametru wartosc url?
        params= {"account" : ACCOUNT_NAME}   #teraz z r musimy wyciągnąć wartość pola, bedziemy przeskakiwac z obiektu pola, do obiektu i pola...
    )

    return r.json()['accounts'][0]['balance']['accountBalance']