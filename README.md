# Software Engineering for Machine Learning Assignment

Please consult the [homework assignment](https://cmu-313.github.io//assignments/hw4) for full context and instructions for this code.  


B) We have decided to use all of the features to predict the successfulness of a student except for G1, G2, and G3.
We chose not to use G1, G2, and G3 because there is a very high correlation (80%+ correlation) of these variables. Additionally, including these variables in the model led to 100% prediction rate which is too good to be true. This is because a student's past grade performance for previous semesters play a huge part in a student's future score report (the G3) because a "good" student will continue to have good grades.
Our retrained model performs better than the baseline model because we use more attributes that can help predict the successfulness of a student.