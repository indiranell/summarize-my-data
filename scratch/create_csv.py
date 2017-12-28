"""
Scratch script to hep with the summarize-my-data work

This script will write out a sample_data.csv file that will have random floats in the columns.
"""

import os,sys
import numpy as np
import pandas as pd

CURR_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
OUTPUT_FILE = CURR_PATH + os.sep + 'data' + os.sep 

def create_csv(num_rows,num_columns,filename):
    "Write out a csv"
    random_matrix = np.random.uniform(1,100,(num_rows,num_columns))
    random_matrix_dataframe = pd.DataFrame(random_matrix)
    random_matrix_dataframe.to_csv(OUTPUT_FILE+filename,header=None,index=False)
    print 'Created the output file: %s'%OUTPUT_FILE+filename

#----START OF SCRIPT
if __name__=='__main__':
    if len(sys.argv)>1:
        create_csv(64,1,sys.argv[1])
    else:
        print 'USAGE: python %s name_of_csv'%__file__
        print 'EXAMPLE: python %s test_data.csv'%__file__

