################################# NY HOSPITALS #################################
#
# Title: AAE 875 Final Program
# Files: paths.py, cleaning.py, input.py, paths.py, regression.py, statistics.py 
#
# Author: Yuxuan Li
# Email:  li967@wisc.edu
#
############################### OUTSIDE HELP CREDITS ###########################
#
# Persons: Cornelia Ilin
# Online sources:
#
############################### 80 COLUMNS WIDE ################################


#import modules here

import paths as pt


from df_pandas import df_main as d
from list_csv import list_main as l

import platform
import os
import pandas as pd


'''
#
# The main.py script holds the user input and response formation for a data 
# analyst chatboot that collects user input and responds appropriately. 
#
'''

def welcome_prompt():
    '''
    # prints the welcome prompt.
    # @param: none.
    '''
    print("Hi, I'm Freddie, what is your name?")

    user_name  = input(">:")
    if user_name == 'C.Ilin':
        user_name = 'Cornelia'
        
    return(user_name)    



def greetings(user_name):
    '''
    # Freddie gets the user name and asks what he can do.
    # @ param: user_name.
    '''
    print("\nNice to meet you %s. How can I help you today?" % user_name)   
    input('>:')
    print('\nOk, I can help you with this.')



def os_and_drive_letter():
    '''
    # sets OS and drive letter. 
    # 1) The user is prompted to enter the computer's operating system. 
    #    Example: Windows, Mac.
    # 2) Sets the drive letter depending on the specified OS
    # @param: none
    # @return: cdrive
    '''
    return pt.operating_system()
    
    
def set_input_output_path(cdrive):
    '''
    # Get input output path from user, and set path
    # Example:
    # USER PATH: C:\\classes\aae875\python
    # USER INPUT: "classes, aae875, python"
    # @param: none.
    # @return: (input_path, output_path)
    ''' 
    
    return(pt.input_path(cdrive), pt.output_path(cdrive))
    

def input_data():
    '''
    # inputs the raw data. The user is prompted to enter the name of the data
    # files (in csv format). For example: SPARCS2014.csv, SPARCS2015.csv,
    # SCARCS2016.csv
    # inputs the data structure. The user is prompted to enter the desired data
    # structure. Available options are: list(csv), array (numpy), dataframe(pandas)
    # if the user enters a data structure other than the ones listed above, Freddie
    # responds "I don't know how to read this data structure"
    # @param: none
    # @return: (a list of input data names, one of three data structure)
    '''
    # get data file names
    print('\nWhat are the names of your data files?')
    input_list = input('>:').split(', ')
    
    # get preferred data structure
    print('\nWhat is the data structure you would like to work with?')
    user_dtstructure = pt.data_structure_test()
    print('\nOk, good choice.')
    
    return (input_list, user_dtstructure) 
    
def data_cleaning(data_list, user_dtstructure, user_name, file_names):
    '''
    # checking data shapes, cleaning, merging
    # calling different modules depend on user-chosen data structure
    # @param: a list of data
    # @return: cleaned, missing/outlier dropped, merged dataframe
    '''
    # greeting and chatthing
    print(user_name + ', tell me what you would like to do next?')
    input(">:") # user asking for data shape
    print('Let me check... oh... this data is really big,', user_name)
    
    # calling different package depend on data structure
    # cleaning data
    if user_dtstructure == 'dataframe':
        # call df_main, return cleaned, merged data
        user_data = d.data_cleaning(data_list, user_dtstructure, user_name, file_names)
    
    # Chatting, ask if user want do more data cleaning    
    input('>:')
    print('\nYes, unless you want to do more data cleaning?')
    input('>:')
        
    # End of data cleaning. Return the merged dataframe
    return user_data
        
        

def summary_stats(df, user_dtstructure, user_name):
    '''
    # summary stats plotting
    # @param: user_data (one dataframe)
    # @return:??
	'''
    if user_dtstructure == 'dataframe':
        d.summary_stats(df,user_name)
    
    
    
    
def linear_model():
    '''
    # do linear_models
    '''
    pass 
        

    
######## runs main script ########
##################################

def main():
    # print welcome prompts
    user_name = welcome_prompt()

    # print greetings; get user name
    greetings(user_name)
    
    # get user os and set drive letter (for windows)
    cdrive = os_and_drive_letter()
    
    # set input path and output path
    input_dir, output_dir = set_input_output_path(cdrive)
    
    # input the data
    # get file names and preferred data structrue
    input_list, user_dtstructure = input_data()    
    if user_dtstructure == 'dataframe':
        data_list = d.input_data(input_list, input_dir)
    
    # checking data shape, deleting outliers, merging
    user_data = data_cleaning(data_list, user_dtstructure, user_name, input_list)
    
    # stat description
    summary_stats(user_data, user_dtstructure, user_name)
    
    # regression
    linear_model()
    
    del output_dir
    

if __name__ == "__main__":
    
    # data = pd.read_csv('G:\\BoxSync\\MyFiles\\875\\final_program_git\\aae875_final_program\\Input\\RawData\\SPARCS2014.csv')
    '''
    f = open ('G:\\BoxSync\\MyFiles\\875\\final_program_git\\aae875_final_program\\Input\\RawData\\SPARCS2014.csv', 'r')
    data.head()
    data = list(csv.reader(f, delimiter = ','))
    file_list.append(data)
    '''
    main()