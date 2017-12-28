"""
Write out a summary for the csv data provided
"""
import os
import numpy as np
import pandas as pd



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

#----START OF SCRIPT
if __name__=='__main__':
    CURR_PATH = os.path.abspath(os.path.dirname(__file__))
    OUTPUT_FILE = CURR_PATH + os.sep + 'data' + os.sep 
    csv = OUTPUT_FILE + 'session_1_data.csv'
    my_obj = SummarizeMyData()
    my_obj.read_csv(csv)
    print my_obj.data