import requests
r = requests.get('http://localhost:5000/predict', params=

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
  
print(r.content)
