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



def read_data(file_names, data_structure, input_path):
    '''
    # this function reads in data (file_names)
    # the desired data structure is provided by the user
    # the desired data structure can be list(csv), array (numpy), dataframe(pandas)
    # @param: file_names, data_structure, input_path
    '''
    
    read_list = []
    for index, token in enumerate(file_names):
        read_list.append(input_path + token)
        

    if data_structure == 'list(csv)':
        print(read_list)
    elif data_structure == 'array(numpy)':
        print(-1)
    elif data_structure == 'dataframe(pandas)':
        print(-1)
    
 
      
               
         
     
            