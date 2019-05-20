# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 13:04:34 2019

@author: ibrir
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np

rows = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness','Insulin ','BMI','DiabetesPedigreeFunction',
        'Age','Outcome']
# loading training data
df = pd.read_csv("diabetes.csv", names=rows)
df.head()
X = np.array(df.ix[:, 1:8]) 	
y = np.array(df['Outcome'])     
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
l=[]
l=[]

choix=input("\n Enter the different values of attributes for classify with knn :      ")
Pregnancies = input('Pregnancies :')
l.append(Pregnancies)
Glucose = input('Glucose :')
l.append(Glucose)
BloodPressure = input('BloodPressure :')
l.append(BloodPressure)
SkinThickness = input('SkinThickness :')
l.append(SkinThickness)
Insulin= input('Insulin :')
l.append(Insulin)
BMI= input('BMI :')
l.append(BMI)
DiabetesPedigreeFunction= input('DiabetesPedigreeFunction :')
l.append(DiabetesPedigreeFunction)
Age= input('Age :')
l.append(int(Age))


print(l)
pred = knn.predict(np.array([l])[:,1:8])
print ("Class ==>> : :   ",pred[0])
choix=input("Do you want to find the accuracy in this data !!     ")
if choix=='yes':     
  plt.style.use('ggplot')
X = df.drop('Outcome',axis=1).values
y = df['Outcome'].values
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42, stratify=y)
neighbors = np.arange(1,9)
train_accuracy =np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

for i,k in enumerate(neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    train_accuracy[i] = knn.score(X_train, y_train) 
    test_accuracy[i] = knn.score(X_test, y_test) 
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train,y_train)
print('The accuracy ==>> : ',knn.score(X_test,y_test))
