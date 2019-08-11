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


'''
#
# The main.py script holds the user input and response formation for a data analyst 
# chatboot that collects user input and responds appropriately. 
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
    print('\nOk, good choice.', end = '')
        
    return (input_list, user_dtstructure) 
    
def data_cleaning():
    '''
    # your comments here
    '''
    pass


def summary_stats():
    '''
    # your comments here
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
    
    # if user choose to work with csv
    if user_dtstructure == 'list':
        # read data
        file_list = cip.read_data(input_list, input_dir)
        # how many rows and columns
        cip.rows_and_columns(file_list)
    if user_dtstructure == 'dataframe':
        file_list = dip.read_data(input_list, input_dir)


if __name__ == "__main__":
    
    # data = pd.read_csv('G:\\BoxSync\\MyFiles\\875\\final_program_git\\aae875_final_program\\Input\\RawData\\SPARCS2014.csv')
    '''
    f = open ('G:\\BoxSync\\MyFiles\\875\\final_program_git\\aae875_final_program\\Input\\RawData\\SPARCS2014.csv', 'r')
    data.head()
    data = list(csv.reader(f, delimiter = ','))
    file_list.append(data)
    '''
    main()