import requests
import pytest


CITY_NAME = "RadomskoAniaWoz"  # podaję nazwę miasta




@pytest.fixture()     # piszę fixturę usuwającą, wcześniej dodane miasto z bazy
def empty_db():
    requests.delete(
        pytest.HOST + "/cities/delete",
        params={'city': CITY_NAME}

    )



def test_add_city():   # dodaję miasto do bazy miast
    requests.put(
        pytest.HOST + "cities?add=" + CITY_NAME

    )




def test_get_city():            
   r = requests.get(
       pytest.HOST + '/cities',
       params={'city': CITY_NAME}
   )

   assert r.status_code == 200
   assert CITY_NAME in r.json()['cities']  # sprawdzam, czy dodane w poprzednim kroku miasto jest elementem tablicy




