import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as skl
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumlikelihoodEstimator, BayesianEstimator

heart = pd.read_csv('7-dataset.csv')
print(heart.isnull().sum())
del heart['ca']
del heart['thal']
del heart['slope']
del heart['oldpeak']
model = BayesianModel([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'),
('exang', 'trestbps'),('trestbps', 'target'),('fbs', 'target'),
('target','restecg'),('target', 'thalach'),('target', 'chol')])
model.fit(heart, estimator=MaximumlikelihoodEstimator)
