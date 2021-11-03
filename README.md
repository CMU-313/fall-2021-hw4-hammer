# API Documentation
## How to call the API
In order to call the API, you must make an HTTP GET request. This can be done in several ways, such as sending a cURL command using the command line or using the requests library in Python.

Here is code for a sample API request using the Python requests library:
```
requests.get('http://localhost:5000/predict', params=
{
	'school': 0,
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
	'absences': 6
} )
```

## Prerequisite data
The field `params` contains given information requested from the user. All included fields are required, and the user must input a value for all fields. The model will then use all of the inputted information to make the best prediction. The fields include:
* `school`: student's school (binary: `0` - Gabriel Pereira or `1` - Mousinho da Silveira)
* `age`: student's age (numeric: from 15 to 22)
* `famsize`: family size (binary: `0` - less or equal to 3 or `1` - greater than 3)
* `reason`:  reason to choose this school (nominal: `0` - close to home, `1` - school reputation, `2` - course preference or `3` - other)
* `traveltime`: home to school travel time (numeric: `1` - <15 min., `2` - 15 to 30 min., `3` - 30 min. to 1 hour, or `4` - >1 hour)
* `studytime`: weekly study time (numeric: `1` - <2 hours, `2` - 2 to 5 hours, `3` - 5 to 10 hours, or `4` - >10 hours)
* `failures`: number of past class failures (numeric: `n` if 1<=`n`<3, else `4`)
* `schoolsup`: extra educational support (binary: `0` - yes or `1` - no)
* `famsup`: family educational support (binary: `0` - yes or `1` - no)
* `paid`: extra paid classes within the course subject (binary: `0` - yes or `1` - no)
* `activities`: extra-curricular activities (binary: `0` - yes or `1` - no)
* `higher`: wants to take higher education (binary: `0` - yes or `1` - no)
* `freetime`: free time after school (numeric: from `1` - very low to `5` - very high)
* `Walc`: weekend alcohol consumption (numeric: from `1` - very low to `5` - very high)
* `absences`: Number of school absences (numeric: from `0` to `93`)

## Preconditions for the service
Preconditions for the service includes ensuring that the Docker executes successfully, and each field must receive the correct type of input. For example, in the new model, all fields take a nonnegative integer value as an input.

## How to understand output
The service should return a value that represents the resulting prediction when an applicant’s data is inputted. This is a boolean value, with 0 representing not accepted and 1 as accepted. The output is currently 81.01% accurate, which was calculated by averaging the returned accuracies of three sets of data after running them on the model.

# Our new model
We have decided to use all of the features to predict the successfulness of a student except for `sex`, `address`, `Pstatus`, `Medu`, `Fedu`, `Mjob`, `Fjob`, `nursery`, `internet`, `romantic`, `famrel`, `guardian`, `goout`, `Dalc`, `health`, `G1`, `G2`, and `G3`.
  
We chose not to use `G1`, `G2`, and `G3` because there is a very high correlation (80%+ correlation) of these variables. Additionally, including these variables in the model led to a 100% prediction rate which is too good to be true. This is because a student's past grade performance for previous semesters plays a huge part in a student's future score report (the `G3`) because a "good" student will continue to have good grades. Crucially, `G1` and `G2 `are grades when the student is already admitted into the school so this is data we would not typically have for students in the actual application process. The rest of these excluded features seem to be very personal to each applicant and would be some privacy violations like health or romantic relationships. Although overall health may help indicate the successfulness of a student, health could also include certain chronic disabilities that are very private to a person's life.

Our retrained model performs better than the baseline model because we use more attributes that can help predict the successfulness of a student. We verified that our model is better than the baseline model because we performed a 3-fold stratified cross-validation. For each of the tests we found accuracy, precision, recall, and F1-score for the old and new model. The precision is ____. Recall is _____. Accuracy is ____. Therefore, for our models, aggregating the results of these three attributes on the new model, we got a total score of 1.898362, while the old model received a score of 1.883704. Since, the three attributes (precision, recall, and accuracy) have a max value of 1, the results of models get better as the average score gets closer to 3. Since our model’s score is closer to 3, we say our model is better than the baseline model.

# Deployment instructions
`(from /dockerfile directory)`
[Comment: make sure that user is currently in `/dockerfile` directory]

`docker build --no-cache -t ml:latest .`
[`docker build`: builds the docker]
[`--no-cache`: makes sure that program does not reuse previous work or data and starts from scratch when built]
[`-t`: tags the latest version built; in this case, `ml:latest`]

`docker run -d -p 5000:5000 ml`
[`docker run`: runs the docker]
[`-d`: detach, which runs the container in the background and prints the container ID]
[`-p`: publish]
[`5000:5000`: docker port number]

(move to `/dockerfile/apps`)
[Comment: make sure that user moves to /dockerfile/apps directory]

`python3 test_api_call.py`
[`python3`: runs `test_api_call.py` using python3]

# Explanation and justification of testing
For testing, our group wrote code that inputs data points with known results so testers can ensure that the API returns the correct result. In each test, the values for each field are inputted, with the student’s acceptance to graduate school as a known value. The API should return what the model is expected to return, and multiple tests will run on the API.

Using known values, testers can make sure that the returned result is accurate in terms of applicant qualifications. The data is also applicable to the tests because they are realistic and do not include edge cases, corner cases, or invalid values. Therefore, the test cases used should ensure that the program returns the expected result and that it functions as intended.