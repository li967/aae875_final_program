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
# 1. Memory error
# https://blog.csdn.net/weixin_39750084/article/details/81501395
#
############################### 80 COLUMNS WIDE ################################
import csv
import numpy as np
import pandas as pd
import os

input_path = "G:\\Box Sync\\MyFiles\\875\\final_program_git\\aae875_final_program\\Input\\RawData"
file_names = ['SPARCS2014.csv', 'SPARCS2015.csv', 'SPARCS2016.csv']

def read_data(file_names, input_path, i):
    '''
    # this function reads in data (file_names)
    # @param: file_names (list), input_path
    '''
    # append input path to data name        
    read_list = [os.path.join(input_path,file) for file in file_names]
    # data_list = [] # a list to store all the data
    # data = pd.read_csv(read_list[i],low_memory=False)
    
    # read data (by chunk in loops)(to avoid MemoryError)  
    data = pd.read_csv(read_list[i], sep=',',engine = 'python',iterator=True)
    # loop sets
    loop = True
    chunkSize = 1000
    chunks = []
    index=0
    # start loop
    print('Start read file', read_list[i], 'by chunk.')
    print('Chunk size:', chunkSize)
    while loop:
        try:
            print(index)
            chunk = data.get_chunk(chunkSize)
            chunks.append(chunk)
            index+=1
    
        except StopIteration:
            loop = False
            print("Iteration is stopped.")
    # merge chunks
    print('Uploaded', read_list[i])
    print('Start merge chunks')
    data = pd.concat(chunks, ignore_index= True)
    print('Merge over.')
    
    return data

        
def rows_and_columns(file_list):
    print('Tell me what you would like to do next?')
    for file in file_list:
        print(len(file))
    
    
if __name__ == '__main__':
    #data2014 = read_data(file_names, input_path,0)
    #data2015 = read_data(file_names, input_path,1)
    data2016 = read_data(file_names, input_path,2)
    
    # print('out function test', data2014.shape, data2015.shape,data2016.shape)
    

    for i in data2016:
        print(type(data2016[i][0]))
    
        
 
      
               
         
     
            