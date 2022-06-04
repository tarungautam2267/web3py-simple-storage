import numpy as np
import csv
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

#read Cleveland Heart Disease data 
heartDisease = pd.read_csv('7-dataset.csv') 
heartDisease = heartDisease.replace('?',np.nan) 
#display the data 
print('Few examples from the dataset are given below') 
print(heartDisease.head()) 
#Model Bayesian Network 
Model=BayesianModel([('age','trestbps'),('age','fbs'), ('sex','trestbps'),('exang','trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','restecg'), ('heartdisease','thalach'),('heartdisease','chol')]) 
#Learning CPDs using Maximum Likelihood Estimators 
print('\n Learning CPD using Maximum likelihood estimators') 
Model.fit(heartDisease,estimator=MaximumLikelihoodEstimator) 
# Inferencing with Bayesian Network 
print('\n Inferencing with Bayesian Network:') 
HeartDisease_infer = VariableElimination(Model)
#computing the Probability of HeartDisease given Age 
print('\n 1. Probability of HeartDisease given Age=30') 
q=HeartDisease_infer.query(variables=['heartdisease'],evidence={'age':28}) 
print(q['heartdisease']) 
#computing the Probability of HeartDisease given cholesterol 
print('\n 2. Probability of HeartDisease given cholesterol=100') 
q=HeartDisease_infer.query(variables=['heartdisease'],evidence={'chol':100}) 
print(q['heartdisease'])