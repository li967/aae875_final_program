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

from list_csv import cleaning as ccl
from list_csv import input as cip
from list_csv import regression as creg
from list_csv import statistics as cst

from df_pandas import cleaning as dcl
from df_pandas import input as dip
from df_pandas import regression as dreg
from df_pandas import statistics as dst

import platform
import os
import pandas as pd
from lib2to3.fixer_util import Comma
from df_pandas.cleaning import data_colnames
from df_pandas.input import file_names


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
    command = input('>:')
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
    print(user_name + ', tell me what you would like to do next?')
    command = input(">:")
    print('Let me check... oh... this data is really big,', user_name)
    
    if user_dtstructure == 'dataframe':
        # get numbers of rows and columns
        nrow, ncol = dcl.rows_and_columns(data_list)
        print('You have %(nrow)d inpatient discharges and %(ncol)d variables\
         that document these observations.' %{
             'nrow':nrow, 'ncol':ncol})
        # chatting
        command = input(">:")
        command = input(">:")


        # drop missing values
        print('\nNo problem, I can help you with this. Let\'s clean the data first.')
        print('Would you like to drop observations with missing values?')
        command = input(":>")
        
        data_list = dcl.drop_missing_values(data_list) # drop missings
        nrow, ncol = dcl.rows_and_columns(data_list)   # update data shape after dropping
        print("\nI have removed all the missing values in your data.") # chatting
        print('You now have %(pat)d million inpatient discharges and %(var)d \
that document these observations.' %{
            'pat':nrow, 'var':ncol})                   # chatting
        command = input(">:")
        
        # remove data outliers
        print("Right... would you like to remove data outliers?") 
        command = input(">:")
        
        data_list = dcl.drop_outliers(data_list)     # drop outliers using IQR boundary
        nrow, ncol = dcl.rows_and_columns(data_list) # update data shape after dropping
        print('\nI have removed all outliers in your data.')
        print('You now have %(pat)d inpatient discharges and %(var)d variables\
 that document these observations.'  %{
            'pat':nrow, 'var':ncol})                 # chatting
        command = input(">:")
        command = input(">:")
        
        # deal with not-matching column names 
        print('I am afraid this is not the best way to move forward.', end = ' ')
        print('The variable names in your data are not consistent over time.')
        data_colnames = dcl.compare_colnames(data_list, file_names) # get var names
        
        
        print('Let me put these in a table for you. Please see below:')
        print(data_colnames) # reporting variable names over year
        command = input('>:')# chatting, user require to align names
        
        print('Sure thing! I will use a dictionary for this. Processing...')
        data_list = dcl.align_colnames(data_list, data_colnames) # update col names
        data_colnames = dcl.compare_colnames(data_list, file_names) # get new names
        print('Variable names match those in year 2016 now. Please see below:')
        print(data_colnames)
        
        # merge data
        user_data = pd.concat(data_list)
    
    # Chatting, ask if user want do more data cleaning    
    command = input('>:')
    print('\nYes, unless you want to do more data cleaning?')
    command = input('>:')
        
    # End of data cleaning. Return the merged dataframe
    return user_data
        
        

def summary_stats(user_data):
    '''
    # summary stats plotting
    # @param: user_data (one dataframe)
    # @return:??
	'''
    pass 
    
def linear_model():
    '''
    # your comments here
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
    input_list, user_dtstructure = input_data()
    if user_dtstructure == 'list': # for user choosing csv/list
        # read data
        file_list = cip.read_data(input_list, input_dir)
        # how many rows and columns
        ccl.rows_and_columns(file_list)
    if user_dtstructure == 'dataframe': # for user choosing dataframe
        # read data
        data_list = dip.read_data(input_list, input_dir, user_name)
    
    
    # checking data shape, deleting outliers, merging
    user_data = data_cleaning(data_list, user_dtstructure, user_name, input_list)
    
    # stat description
    summary_stats(user_data)
    

if __name__ == "__main__":
    
    # data = pd.read_csv('G:\\BoxSync\\MyFiles\\875\\final_program_git\\aae875_final_program\\Input\\RawData\\SPARCS2014.csv')
    '''
    f = open ('G:\\BoxSync\\MyFiles\\875\\final_program_git\\aae875_final_program\\Input\\RawData\\SPARCS2014.csv', 'r')
    data.head()
    data = list(csv.reader(f, delimiter = ','))
    file_list.append(data)
    '''
    main()