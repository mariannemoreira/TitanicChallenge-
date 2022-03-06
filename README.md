# TitanicChallenge-
Titanic - Machine Learning from Disaster

Use machine learning to create a model that predicts which passengers survived the Titanic shipwreck.

 We will you use the Titanic passenger data (name, age, price of ticket, etc) to try to predict who will survive and who will die.
 
 There are three files: (1) train.csv, (2) test.csv, and (3) gender_submission.csv.
(1) Train.csv - Contains the details of a subset of the passengers on board (891 passengers, to be exact -- where each passenger gets a different row in the table). 
(2) Test.csv - Using the patterns you find in train.csv, you have to predict whether the other 418 passengers on board (in test.csv) survived.
(3)The gender_submission.csv - This file is provided as an example that shows how you should structure your predictions. It predicts that all female passengers survived, and all male passengers died. 
Your hypotheses regarding survival will probably be different, which will lead to a different submission file.

Your submission file should have:

- a "PassengerId" column containing the IDs of each passenger from test.csv.
- a "Survived" column (that you will create!) with a "1" for the rows where you think the passenger survived, and a "0" where you predict that the passenger died.
