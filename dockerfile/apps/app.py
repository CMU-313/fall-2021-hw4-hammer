from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

@app.route('/predict')
def predict():
	#use entries from the query string here but could also use json
    # school = request.args.get('school')
    # sex = request.args.get('sex')
    age = request.args.get('age')
    # address = request.args.get('address')
    # famsize = request.args.get('famsize')
    # Pstatus = request.args.get('Pstatus')
    # Medu = request.args.get('Medu')
    # Fedu = request.args.get('Fedu')
    # Mjob = request.args.get('Mjob')
    # Fjob = request.args.get('Fjob')
    # reason = request.args.get('reason')
    # guardian = request.args.get('guardian')
    # traveltime = request.args.get('traveltime')
    # studytime = request.args.get('studytime')
    # failures = request.args.get('failures')
    # schoolsup = request.args.get('schoolsup')
    # famsup = request.args.get('famsup')
    # paid = request.args.get('paid')
    # activities = request.args.get('activities')
    # nursery = request.args.get('nursery')
    # higher = request.args.get('higher')
    # internet = request.args.get('internet')
    # romantic = request.args.get('romantic')
    # famrel = request.args.get('famrel')
    # freetime = request.args.get('freetime')
    # goout = request.args.get('goout')
    # Dalc = request.args.get('Dalc')
    # Walc = request.args.get('Walc')
    health = request.args.get('health')
    absences = request.args.get('absences')

    data = [[age],[health],[absences]]
    # data = [[school],
    #         [sex],
    #         [age],
    #         [address],
    #         [famsize],
    #         [Pstatus],
    #         [Medu],
    #         [Fedu],
    #         [Mjob],
    #         [Fjob],
    #         [reason],
    #         [guardian],
    #         [traveltime],
    #         [studytime],
    #         [failures],
    #         [schoolsup],
    #         [famsup],
    #         [paid],
    #         [activities],
    #         [nursery],
    #         [higher],
    #         [internet],
    #         [romantic],
    #         [famrel],
    #         [freetime],
    #         [goout],
    #         [Dalc],
    #         [Walc],
    #         [health],
    #         [absences]]
    query_df = pd.DataFrame({ 'age' : pd.Series(age) ,'health' : pd.Series(health) ,'absences' : pd.Series(absences)})
    # query_df = pd.DataFrame({'school': pd.Series(school), 'sex': pd.Series(sex), 'age': pd.Series(age), 'address': pd.Series(address), 'famsize': pd.Series(famsize), 'Pstatus': pd.Series(Pstatus), 'Medu': pd.Series(Medu), 'Fedu': pd.Series(Fedu), 'Mjob': pd.Series(Mjob), 'Fjob': pd.Series(Fjob), 'reason': pd.Series(reason), 'guardian': pd.Series(guardian), 'traveltime': pd.Series(traveltime), 'studytime': pd.Series(studytime), 'failures': pd.Series(failures), 'schoolsup': pd.Series(schoolsup), 'famsup': pd.Series(famsup), 'paid': pd.Series(paid), 'activities': pd.Series(activities), 'nursery': pd.Series(nursery), 'higher': pd.Series(higher), 'internet': pd.Series(internet), 'romantic': pd.Series(romantic), 'famrel': pd.Series(famrel), 'freetime': pd.Series(freetime), 'goout': pd.Series(goout), 'Dalc': pd.Series(Dalc), 'Walc': pd.Series(Walc), 'health': pd.Series(health), 'absences': pd.Series(absences)})
    query = pd.get_dummies(query_df)
    prediction = clf.predict(query)
    return jsonify(np.asscalar(prediction))


# Index(['school', 'sex', 'age', 
# '', '', '', '', 'Fedu',
#        'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime',
#        'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery',
#        'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc',
#        'Walc', 'health', 'absences'],
#       dtype='object')

if __name__ == '__main__':
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)