import requests
import pytest
from dockerfile.apps.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_client(client):
    r = client.get('/')
    print("\n====== Result TEST_CLIENT ======")
    print(r.data)
    print("TEST PASSED!")

def test_predict(client):
    a = requests.get('http://localhost:5000/predict', params = 
                    {'Walc': 1,
                    'absences': 2,
                    'activities': 1,
                    'age': 15,
                    'failures': 0,
                    'famsize': 0,
                    'famsup': 1,
                    'freetime': 2,
                    'higher': 1,
                    'paid': 1,
                    'reason': 1,
                    'school': 0,
                    'schoolsup': 0,
                    'studytime': 3,
                    'traveltime': 1})
    assert(a.content == b'0\n')

    r = requests.get('http://localhost:5000/predict', params=
                    {'school': 0, 'age': 18, 'famsize': 0,
                    'reason': 0, 'traveltime': 2, 'studytime': 2,
                    'failures': 0, 'schoolsup': 1, 'famsup': 0,
                    'paid': 0, 'activities': 0, 'higher': 1,
                    'freetime': 3, 'Walc': 1, 'absences': 6})
    assert(r.content == b'0\n')
    print(r.content)

    d = requests.get('http://localhost:5000/predict', params=
                    {'school': "GP", 'age': 1, 'famsize': "LE3",
                    'reason': "reputation", 'traveltime': 1, 'studytime': 3,
                    'failures': 0,'schoolsup': "no", 'famsup': "yes",
                    'paid': "yes", 'activities': "yes", 'higher': "yes", 
                    'freetime': 2, 'Walc': 1, 'absences': 2})
    assert(d.content == b'0\n')
    print(d.content)

    print("\n====== Result TEST_PREDICT ======")
    print("TEST PASSED!")


# test case 1
a = requests.get('http://localhost:5000/predict', params=
{'school': 0,
  'age': 18,
  'famsize': 0,
  'reason': 0,
  'traveltime': 2,
  'studytime': 2,
  'failures': 0,
  'schoolsup': 1,
  'famsup': 0,
  'paid': 0,
  'activities': 0,
  'higher': 1,
  'freetime': 3,
  'Walc': 1,
  'absences': 6})
assert(a.content == b'0\n')

# test case 2
b = requests.get('http://localhost:5000/predict', params=
{'school': 1,
  'age': 18,
  'famsize': 0,
  'reason': 3,
  'traveltime': 1,
  'studytime': 3,
  'failures': 0,
  'schoolsup': 1,
  'famsup': 1,
  'paid': 1,
  'activities': 1,
  'higher': 1,
  'freetime': 2,
  'Walc': 2,
  'absences': 5})
assert(b.content == b'0\n')

# test case 3
c = requests.get('http://localhost:5000/predict', params=
{'school': 1,
  'age': 22,
  'famsize': 1,
  'reason': 2,
  'traveltime': 3,
  'studytime': 3,
  'failures': 0,
  'schoolsup': 1,
  'famsup': 1,
  'paid': 1,
  'activities': 1,
  'higher': 0,
  'freetime': 1,
  'Walc': 1,
  'absences': 0})
assert(c.content == b'0\n')