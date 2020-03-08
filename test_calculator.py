import json

import logging  #musimy skonfigurowac logger zeby powiedziec jakie info chcemy miec w logu, np.czas,sam message,czy cos jeszcze
import requests
import pytest

logging.basicConfig(
    level=logging.INFO,   #poz + format logowania
    format= '%(asctime)s - %(message)s'     #placeholdery '%()s - %()s' czas + wiadomość


)

FIRST_NUMBER = 4
SECOND_NUMBER = 2

def test_add():     # post/add   , musimy określić content type tego co wysyłamy, czyli jak wyslac header...
        r = requests.post(
            pytest.HOST + '/add',
            headers={'Content-Type':'application/json'},
            #data=json.dumps({'firstNumber': FIRST_NUMBER, 'secondNumber': SECOND_NUMBER}) # tym coś wyślemy - data, a konkretnie chcemy jsona -> czyli metoda json dumps
            #json={'firstNumber': FIRST_NUMBER, 'secondNumber': SECOND_NUMBER}
            json=_get_payload(FIRST_NUMBER, SECOND_NUMBER)

        )
        #assert r.json()['result'] == FIRST_NUMBER + SECOND_NUMBER   # r.format, ktory chcemy json , pole w klamrach []
        #3logging.info("####### Hello world!")
        _log(r)
        assert _result_is_ok(r, 'add')

def test_subtraction():  # post/add   , musimy określić content type tego co wysyłamy, czyli jak wyslac header...
    r = requests.post(
        pytest.HOST + '/subtract',
        headers={'Content-Type': 'application/json'},
        # data=json.dumps({'firstNumber': FIRST_NUMBER, 'secondNumber': SECOND_NUMBER}) # tym coś wyślemy - data, a konkretnie chcemy jsona -> czyli metoda json dumps
        #json={'firstNumber': FIRST_NUMBER, 'secondNumber': SECOND_NUMBER}
        json=_get_payload(FIRST_NUMBER, SECOND_NUMBER)
    )
    #assert r.json()['result'] == FIRST_NUMBER - SECOND_NUMBER  # r.format, ktory chcemy json , pole w klamrach []
    _log(r)
    assert _result_is_ok(r, 'subtract')
def test_multiply():  # post/add   , musimy określić content type tego co wysyłamy, czyli jak wyslac header...
    r = requests.post(
        pytest.HOST + '/multiply',
        headers={'Content-Type': 'application/json'},
        # data=json.dumps({'firstNumber': FIRST_NUMBER, 'secondNumber': SECOND_NUMBER}) # tym coś wyślemy - data, a konkretnie chcemy jsona -> czyli metoda json dumps
        #json={'firstNumber': FIRST_NUMBER, 'secondNumber': SECOND_NUMBER}
        json=_get_payload(FIRST_NUMBER,SECOND_NUMBER)
    )
    #2 assert r.json()['result'] == FIRST_NUMBER * SECOND_NUMBER  # r.format, ktory chcemy json , pole w klamrach []
    _log(r)
    assert _result_is_ok(r, 'multiply')

def _get_payload(first, second):   #podkresliniki mowią, ze jest prywatna
    return {
        'firstNumber': first,
        'secondNumber': second

    }

def _result_is_ok(resp, operation_type):
    assert resp.status_code == 200
    result = resp.json()['result']
    if operation_type == 'add':
        return result == FIRST_NUMBER + SECOND_NUMBER
    if operation_type == 'subtract':
        return result == FIRST_NUMBER - SECOND_NUMBER
    if operation_type == 'multiply':
        return result == FIRST_NUMBER * SECOND_NUMBER
    else:
        return False

def _log(resp):
    logging.info(
        f"Request {resp.request.method} "
        f"to {resp.request.url} "
        f"with payload {resp.request.body}"


    )

    logging.info(
        f'Response code: {resp.status_code}'
        f"with payload {resp.json}"
    )





