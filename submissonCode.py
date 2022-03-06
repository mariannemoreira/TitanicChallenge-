from sklearn.ensemble import RandomForestClassifier
import pandas as pd

train_data = pd.read_csv('./titanic/train.csv')
test_data = pd.read_csv('./titanic/test.csv')
y = train_data['Survived']

features = ['Pclass', 'Sex', 'SibSp', 'Parch']
x = pd.get_dummies(train_data[features])
x_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(x, y)
predictions = model.predict(x_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('submission.csv', index=False)
print('Your submission was succesfully saved!')
