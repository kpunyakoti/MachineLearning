import pandas as pd
import numpy as np

def na_data(df):
    play_data_na = (df.isnull().sum() / len(df)) * 100
    play_data_na = play_data_na.drop(play_data_na[play_data_na == 0].index).sort_values(ascending=False)[:30]
    missing_data = pd.DataFrame({'Missing Ratio' :play_data_na})
    missing_data.head(20)
    return missing_data

def cat_stats(df):
    cat_stats = pd.DataFrame(df.describe(include = [np.object]))
    cat_stats = cat_stats.T
    nadf = na_data(df)
    for i, r in nadf.iterrows():
        cat_stats.loc[i, 'Missing Ratio'] = nadf.loc[i][0]
    cat_stats.dropna(subset = ['freq'], inplace=True)
    cat_stats['distribution'] = cat_stats['freq']/cat_stats['count']*100
    cat_stats.sort_values('distribution', ascending=False, inplace=True)
    return cat_stats

def valuecounts(df, cat_cols=None, normalize=False):
    if cat_cols==None:
        desc_df = pd.DataFrame(df.describe(include = [np.object]))
        cat_cols = desc_df.columns.tolist()
        print("List of Categorical Columns:", cat_cols)
    else:
        cat_cols
    for c in cat_cols:
        print(c)
        if normalize:
            print(df[c].value_counts(normalize=True)[:10])
        else:
            print(df[c].value_counts()[:10])
        print('\n')

def chi2test(df, target, cat_cols=None):
    from scipy.stats import chi2_contingency
    from scipy.stats import chi2
    if cat_cols==None:
        cat_col_df = df.select_dtypes(include=[np.object])
        cat_cols = cat_col_df.columns
    else:
        cat_cols
    for c in cat_cols:
        ct = pd.crosstab(df[c], df[target])
        stat, p, dof, expected = chi2_contingency(ct)
        print(c,'\n')
        prob = 0.95
        critical = chi2.ppf(prob, dof)
        print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
        if abs(stat) >= critical:
            print('Dependent (reject H0)')
        else:
            print('Independent (fail to reject H0)')
            
        alpha = 1.0 - prob
        print('significance=%.3f, p=%.3f' % (alpha, p))
        if p <= alpha:
            print('Dependent (reject H0)')
        else:
            print('Independent (fail to reject H0)')
        print('\n')
        
        
############################################
#--------------CLASSIFICATION--------------#
############################################

from sklearn import linear_model
from sklearn import ensemble
from sklearn import metrics
from sklearn.model_selection import train_test_split

class ClassificationMvp():
    
    def __init__(self, X, y, multi_class=False):
        
        self.train_X, self.test_X, self.train_y, self.test_y = train_test_split(X, y, test_size=0.2, random_state=32)
                                                                               
        self.multi_class = multi_class
        if self.multi_class:
            self.model = linear_model.LogisticRegression(multi_class='ovr')
        else:
            self.model = ensemble.RandomForestClassifier()
        self.model.fit(self.train_X, self.train_y)
        
    def get_splits(self):
        return self.train_X, self.test_X, self.train_y, self.test_y
    
    def trained_model(self):
        return self.model
    
    def adjusted_preds(y_pred_proba, t):
        return [1 if y >= t else 0 for y in y_pred_proba]

    def optim_f1(actuals, pred_probs):
        model_f1_score={}
        y_acts = actuals
        for thresh in np.arange(0.3, 0.5, 0.1):
            thresh = np.round(thresh, 2)        
            y_pred_adj = adjusted_preds(pred_probs, thresh)
            model_f1_score[thresh]= metrics.f1_score(y_acts, y_pred_adj)
        model_cutoff=max(model_f1_score, key=model_f1_score.get)
        print("Max F1 score  is {1} found at threshold {0}".format(model_cutoff, model_f1_score[model_cutoff]))
        return model_cutoff
    
    def get_metrics(self, actuals, preds):
        acc = metrics.accuracy_score(actuals, preds)
        recall = metrics.recall_score(actuals, preds)
        precision = metrics.precision_score(actuals, preds)
        f1 = metrics.f1_score(actuals, preds) 
        print("Confusion Matrix:")
        print(metrics.confusion_matrix(actuals, preds))
        print("Accuracy:",acc," | Recall:",recall," | Precision :",precision, " | f1:", f1)  
    
    def multiclass_metrics(self, actuals, preds):
        acc = metrics.accuracy_score(actuals, preds)
        print("Accuracy :",acc)
        print("Confusion Matrix:")
        print(metrics.confusion_matrix(actuals, preds))
        print("Classification Report:")
        print(metrics.classification_report(actuals, preds, digits=3))
        
    def classification(self, adjusted=False):
        tr_actuals = self.train_y
        tr_preds = self.model.predict(self.train_X)
        
        test_actuals = self.test_y
        test_preds = self.model.predict(self.test_X)
        
        if self.multi_class:
            print("Train Metrics:\n")
            self.multiclass_metrics(tr_actuals, tr_preds)
            pred_probs = self.model.predict_proba(self.train_X)
                        
            print("Test Metrics:\n")
            self.multiclass_metrics(test_actuals, test_preds)
            
        else:
            if adjusted:
                print("Train Metrics:\n")
                self.get_metrics(tr_actuals, tr_preds)
                
                #get optimal threshold based on optimal F1
                tr_pred_probs = self.model.predict_proba(self.train_X)[:,1]
                test_pred_probs = self.model.predict_proba(self.test_X)[:,1]
                optimal_threshold = self.optim_f1(tr_actuals, tr_pred_probs)
                
                print('Train Metrics with Adjusted threshold:\n')
                tr_preds_adjusted = self.adjusted_preds(tr_pred_probs, optimal_threshold)
                self.get_metrics(tr_acutals, tr_preds_adjusted)
            
                print('Test Metrics with Adjusted threshold:\n')
                test_preds_adjusted = self.adjusted_preds(test_preds, optimal_threshold)
                self.get_metrics(test_acutals, test_preds_adjusted)
            else:
                print("Train Metrics:\n")
                self.get_metrics(tr_actuals, tr_preds)
                
                print("Test Metrics:\n")
                self.get_metrics(test_actuals, test_preds)
                