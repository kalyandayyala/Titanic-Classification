

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.simplefilter('ignore')

df= pd.read_csv('train.csv')
df_test=pd.read_csv('test.csv')

df.head()

df.info()

df.describe()

df.isna().sum(),df_test.isna().sum()

df.columns,df_test.columns

df.drop(['Cabin'],axis=1,inplace=True)
df_test.drop(['Cabin'],axis=1,inplace=True)

# Imoutation techinique
## 1 mean value imoutation

"""# imputation techinique
## 1 mean value imoutation
"""

# plt.hist(df.Age)
sns.distplot(df.Age)

sns.distplot(df_test.Age)

df.Age.isnull().sum()

df['Age_mean']=df['Age'].fillna(df['Age'].mean())
df_test['Age_mean']=df_test['Age'].fillna(df['Age'].mean())

df[['Age_mean','Age']]

import seaborn as sns
sns.distplot(df['Age'])
sns.distplot(df['Age_mean'],color='r')

sns.distplot(df_test['Age'])
sns.distplot(df_test['Age_mean'],color='r')

df.info()
df.drop('Age',axis=1,inplace=True)

df_test.info()
df_test.drop('Age',axis=1,inplace=True)

df.info(),df_test.info()

"""## 3. mode value imputation

### use in categorical value

"""

df[df['Embarked'].isnull()]

df['Embarked'].unique()

mode=df['Embarked'].mode()[0]

mode

df['Embarked_mode']=df['Embarked'].fillna(mode)

df['Embarked_mode'].isnull().sum()

df.drop(['Embarked','Ticket','Name'],inplace=True,axis=1)

df.columns

df.info()

df.rename({'Embarked_mode':'Embarked','Age_mean':'Age'},inplace=True,axis=1)
df

df_test.rename({'Age_mean':'Age'},inplace=True,axis=1)

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

df.info()

df['Embarked'].unique()

df_test.info()

df_test['Sex'] = df_test['Sex'].map({'male': 0, 'female': 1})
df_test['Embarked'] = df_test['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
df_test.info()

sns.distplot(df_test['Fare'])

import numpy as np
dfFare=np.log(df_test['Fare'])

FareMode=df_test['Fare'].median()

df['Fare']=df['Fare'].fillna(FareMode)
df_test['Fare']=df_test['Fare'].fillna(FareMode)

df_test.info()

df.columns

df_test.columns

x=df[[ 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
y=df['Survived']

sns.heatmap(df.corr())

sns.histplot(data=df,x='Age',

             kde=True,hue='Survived')

sns.histplot(data=df,x='Pclass',

             kde=True,hue='Survived')

sns.histplot(data=df,x='Fare',

             kde=True,hue='Survived',bins =20)

sns.histplot(data=df,x='Sex',
             kde=True,hue='Survived')

sns.histplot(data=df,x='Embarked',
             y='Survived',
             kde=True,bins=2)

"""### We can see that fare, Sex is highly corelated to survived column irrespective of their Age. We Observe that The Increase in Fare is directly relate of survival.we Also see that ratio of survival of Female is more than male.We Also see that Age Group of 20-40 has larger survival rate than other group so our model shoud  work best if we treat Age As Categorical Varible and model should be non linear and Should be able to categorise the data

"""

# Split the data into training and validation sets
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_val)

from sklearn.metrics import accuracy_score
accuracy_score(y_pred,y_val)

x_test=df_test[[ 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
y_testPred=model.predict(x_test)

y_testPred

submmision=df_test.join(pd.DataFrame(y_testPred))

submmision.rename({0:'Survived'},axis=1,inplace=True)

submmision[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare','Survived']]

submmision['Sex'] = submmision['Sex'].map({0:'male', 1:'female'})
submmision['Embarked'] = submmision['Embarked'].map({0:'S', 1:'C', 2:'Q'})

submmision[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked','Survived']]

df.corr()



