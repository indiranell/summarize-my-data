"""
Scratch script to hep with the summarize-my-data work

This script will write out a sample_data.csv file that will have random floats in the columns
"""

import os
import numpy as np
import pandas as pd

CURR_PATH = os.path.abspath(os.path.dirname(__file__))
OUTPUT_FILE = CURR_PATH + os.sep + 'sample_data.csv'

def create_csv(num_rows,num_columns):
    "Write out a csv"
    random_matrix = np.random.uniform(1,100,(num_rows,num_columns))
    random_matrix_dataframe = pd.DataFrame(random_matrix)
    random_matrix_dataframe.to_csv(OUTPUT_FILE)

#----START OF SCRIPT
if __name__=='__main__':
    create_csv(64,1)
