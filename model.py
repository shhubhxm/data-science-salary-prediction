#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:56:42 2021

@author: vyass
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('eda_data.csv')

# choose relevant columns
df.columns
df_model =df[['avg_salary','Rating','Size','Type of ownership','Industry','Sector','Revenue','num_comp','hourly','employer_provided','job_state','same_state','age','python_yn','spark','aws','excel','job_simp','seniority','desc_len']]

# get dummy data
df_dum = pd.get_dummies(df_model)

# train,test split(train , test, valid)
from sklearn.model_selection import train_test_split

X = df_dum.drop('avg_salary',axis=1)
y = df_dum.avg_salary.values

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

## Models

# 1.Linear Regression
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)

model = sm.OLS(y,X_sm)
model.fit().summary()


from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train,y_train)

np.mean(cross_val_score(lm,X_train,y_train,scoring='neg_mean_absolute_error',cv= 3))


# 2.lasso regression
lm_l = Lasso(alpha=.13)
lm_l.fit(X_train,y_train)
np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))

alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3)))
    
plt.plot(alpha,error)

err = tuple(zip(alpha,error))
df_err = pd.DataFrame(err, columns = ['alpha','error'])
df_err[df_err.error == max(df_err.error)]
 

# 3.random forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 3))


#Tune models GridesearchCV
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error',cv=3)
gs.fit(X_train,y_train)
gs.best_estimator_
#gs.best_score_


#Testensemmble
tpred_lm = lm.predict(X_test)
tpred_lm1 = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error

mean_absolute_error(y_test,tpred_lm)
mean_absolute_error(y_test,tpred_lm1)
mean_absolute_error(y_test,tpred_rf)


mean_absolute_error(y_test,(tpred_lm+tpred_rf)/2)