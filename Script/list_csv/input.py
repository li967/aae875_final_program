################################# NY HOSPITALS #################################
#
# Title:
# Files: 
#
# Author:
# Email:
#
############################### OUTSIDE HELP CREDITS ###########################
#
# Persons: Cornelia Ilin
# Online sources:
#
############################### 80 COLUMNS WIDE ################################
import csv
import numpy as np
import pandas as pd
import os

def read_data(file_names, input_path):
    '''
    # this function reads in data (file_names)
    # @param: file_names (list), input_path
    '''
    # append input path to data name        
    read_list = [os.path.join(input_path,file) for file in file_names]
    
    # upload data
    file_list = []
    for token in read_list:
        print('Start uploading:', token)
        f = open (token, 'r')
        data = list(csv.reader(f, delimiter = ','))
        file_list.append(data)
        print('Done upload:', token)
        
    return file_list
        
def rows_and_columns(file_list):
    print('Tell me what you would like to do next?')
    for file in file_list:
        print(len(file))
    
        
 
      
               
         
     
            