import numpy as np
import pandas as pd

import os

for dirname, _, filenames in os.walk('./titanic'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

train_data = pd.read_csv('./titanic/train.csv')
train_data.head()
#print(train_data.head())

test_data = pd.read_csv('./titanic/test.csv')
test_data.head()
#print(test_data.head())

#checking patterns
women = train_data.loc[train_data.Sex == 'female']['Survived']
rate_women = sum(women)/len(women)
print(f'{rate_women} % of women who survived')

men = train_data.loc[train_data.Sex == 'male']['Survived']
rate_men = sum(men)/len(men)
print(f'{rate_men} % of men who survived')




