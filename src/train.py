import numpy as np
import math
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score, mean_squared_error

def modelTraining(models, X_train, y_train, X_test, y_test):
    for modelName, model in models.items():
        model.fit(X=X_train, y=y_train)
        print(f'{modelName} training complete')
