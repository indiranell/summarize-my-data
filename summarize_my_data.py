"""
Identify outliers in the csv data provided
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor
from scipy.stats import iqr

class SummarizeMyData(object):
    "Class to summarize data"

    def __init__(self,csv=None):
        "The initializer"
        self.data = ''
        if csv is not None:
            self.read_csv(csv)

    def read_csv(self,csv):
        "Read a given csv and store it in a dataframe"
        self.data = pd.read_csv(csv)

        return self.data

    def detect_outlier_modified_zscore(self):
        "Use the modified to detect an outlier in the series"
        threshold = 3.5
        median = self.data.iloc[:,0].median()
        sigma = self.data.iloc[:,0].std()
        modified_zscores = [value for value in self.data.iloc[:,0] if 0.6745 * (value - median)/sigma > threshold]

        return modified_zscores

    def detect_outlier_lof(self):
        "Detect outliers using the LOF algorithm"
        #Src: http://scikit-learn.org/stable/auto_examples/neighbors/plot_lof.html#sphx-glr-auto-examples-neighbors-plot-lof-py
        num_neighbours = max(3,int(len(self.data)/10))
        second_dimension = pd.DataFrame([0 for i in range(0,len(self.data))])
        my_data = pd.concat([second_dimension,self.data], axis=1, join='inner')
        clf = LocalOutlierFactor(n_neighbors=num_neighbours)
        y_pred = clf.fit_predict(my_data)
        outliers = [val for val,outlier_score in zip(self.data.iloc[:,0],y_pred) if outlier_score == -1]
    
        return outliers
            

    def detect_outlier_iqr(self,my_list):
        "Detect outliers using the IQR method"
        #Src: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.iqr.html
        my_iqr = iqr(my_list)
        quartile_25, quartile_75 = np.percentile(my_list,[25,75])
        lower_bound = quartile_25 - (1.5 *  my_iqr)
        upper_bound = quartile_75 + (1.5 * my_iqr)

        return [value for value in self.data.iloc[:,0] if (value < lower_bound or value > upper_bound)]


    def plot_data(self):
        "Convenience method to visualize the data"
        self.data.plot(style='b.',title='Data in the csv')
        plt.show()


#----START OF SCRIPT
if __name__=='__main__':
    CURR_PATH = os.path.abspath(os.path.dirname(__file__))
    OUTPUT_FILE = CURR_PATH + os.sep + 'data' + os.sep 
    csv = OUTPUT_FILE + 'example_outlier_data.csv'
    my_obj = SummarizeMyData()
    my_obj.read_csv(csv)
    print "\nOutliers detected by Modified z-score: ",my_obj.detect_outlier_modified_zscore()
    print "\n\nOutliers detected by Local Outlier Factor (LOF): ", my_obj.detect_outlier_lof()
    print "\n\nOutliers detected by InterQuartile Range (IQR): ", my_obj.detect_outlier_iqr(my_obj.data.iloc[:,0].values)
    my_obj.plot_data()
