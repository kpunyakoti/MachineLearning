"""
Please change the below section
"""
PATH = "C:/Users/kpunyakoti/Desktop/Future/HelloFresh/"
import mysql.connector
connection = mysql.connector.connect(host = 'localhost', user='root', password='root', db= 'hellofresh')

current_model = 'rcv_final_20190516.pkl'

"""
Do NOT change anything else from here
"""

import pandas as pd
import numpy as np
import sklearn as sk
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import time
timestr = time.strftime("%Y%m%d")

#open current model
with open(current_model, 'rb') as model_file:
    model = pickle.load(model_file)

def prepare_trainset(ratings, ingredients):

    #clean data
    ratings['score'] = ratings['score'].astype(float)
    ingredients['Unit_weight_amount'] = ingredients['Unit_weight_amount'].astype(float)
    ingredients.drop_duplicates(inplace=True)
    
    #create ing_count
    ingredient_count = pd.DataFrame(ingredients.recipe_code.value_counts())
    ingredient_count.reset_index(inplace=True)
    ingredient_count.columns = ['recipe_code', 'ing_count']
    ingredients = pd.merge(ingredients, ingredient_count, on = 'recipe_code')

    #create ing_weight
    ing_wt = pd.DataFrame(ingredients.groupby('recipe_code')['Unit_weight_amount'].sum())
    ing_wt.reset_index(inplace=True)
    ing_wt.columns = ['recipe_code', 'ing_weight']
    ingredients = pd.merge(ingredients, ing_wt, on = 'recipe_code', how='outer')
    
    #drop cols
    drop_cols = ['Ingredient','Unit_weight_amount']
    for x in drop_cols:
        ingredients.drop(x, axis=1, inplace=True)
    
    #merge tables
    train = pd.merge(ratings, ingredients, on = 'recipe_code')
    train.drop_duplicates(inplace=True)

    train.drop('recipe_code', axis=1, inplace=True)

    return train

def reg_metrics(preds, actuals):
    rmse = np.sqrt(mean_squared_error(preds, actuals))
    r2 = r2_score(preds, actuals)
    return rmse, r2
    
def train_model():
    print("Getting new data from database")
    #retrive records from database, where new is 0 which means the records which has scores.
    ratings = pd.read_sql_query("select recipe_code, score from recipe_ratings where new = 0", connection)
    ingredients = pd.read_sql_query('select recipe_code, Ingredient, Unit_weight_amount from ingredients', connection)

    print("Preparing train set")
    train = prepare_trainset(ratings, ingredients)
    print("Train set prepared")
    y_train = train['score']
    train.drop('score', axis=1, inplace=True)

    #split data
    train_x, val_x, train_y, val_y = train_test_split(train, y_train, test_size = 0.2, random_state = 17)
    
    #train model
    model.fit(train_x, train_y)
    print('Model Training Completed')
                    
    #predict on train set
    train_preds = model.predict(train_x)
    train_rmse, train_r2 = reg_metrics(train_preds, train_y)

    #predict on validation set
    val_preds = model.predict(val_x)
    val_rmse, val_r2 = reg_metrics(val_preds, val_y)

    print('Train_Set RMSE: {}  |  R-Squared Statistic: {}'.format(train_rmse, train_r2))
    print('Val_Set RMSE: {}  |  R-Squared Statistic: {}'.format(val_rmse, val_r2))

    return model


trained_model = train_model()

trained_model_filename = 'trained_model_'+timestr+'.pkl'
# Open the file to save as pkl file
trained_model_pkl = open(trained_model_filename, 'wb')
pickle.dump(trained_model, trained_model_pkl)
# Close the pickle instances
trained_model_pkl.close()


msg = "New trained model saved as pickle file: "+trained_model_filename
print(msg)



    


