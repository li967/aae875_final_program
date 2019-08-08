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

import cleaning as cl
import input as ip
import paths as pt
import regression as reg
import statistics as st

import platform
import os


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
    # sets OS and drive letter. The user is prompted to enter the computer's
    # operating system. Example: Windows, Mac.
    # @param: none.
    # @return: cdrive
    ''' 
    print('What is your computer\'s operating system?')
    user_os = input('>:')
    user_os = user_os.lower().replace(' ','')
    
    
    if user_os == 'windows':
        cdrive = str(os.getcwd()).split(os.path.sep)[0]
        print('Nice. Your drive letter is now set to', cdrive + '\\\\')
        return cdrive
    else:
        print('Nice.')
        
        


def input_path(cdrive):
    '''
    # sets the input path and saves its value globally
    # The user is prompted to enter the input path.
    # For example, if user path is "N:\Classes\AAE875\DataAnalytics\FinalProgram\Input"
    # then Classes, AAE875, DataAnalytics, FinalProgram, Input will be entered
    # in the command line.
    # @param: cdrive
    # @return: input_path
    '''
    print('\nWhat is your input path?')
    user_path = input('>:').split(', ')
    input_path = ''
    for token in user_path:
        input_path = os.path.join(input_path, token)
    
    print('Your input path is now set to', input_path)
    
    input_path = os.path.join(cdrive, input_path)
    return input_path


def output_path(cdrive):
    '''
    # sets the output path and saves its value globally.
    # The user is prompted to enter the output path.
    # For example, if user path is "N:\Classes\AAE875\DataAnalytics\FinalProgram\Output"
    # then Classes, AAE875, DataAnalytics, FinalProgram, Output will be entered
    # in the command line.
    # @param: cdrive
    # @return: output_path
    '''
    print('\nWhat is your output path?')
    user_path = input('>:').split(', ')
    output_path = ''
    for token in user_path:
        output_path = os.path.join(output_path, token)
    
    print('Your input path is now set to', output_path)
    
    output_path = os.path.join(cdrive, output_path)
    return output_path
    

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
    print('\nWhat are the names of your data files?')
    input_list = input('>:').split(', ')
    
    print('\nWhat is the data structure you would like to work with?')
    user_dtstructure = input('>:')
    
    # test if the data structure chosen by user is valid
    while True:
        if not user_dtstructure in ['list(csv)', 'array (numpy)', 'dataframe(pandas']:
            print("I don't know how to read this data structure")
            user_dtstructure = input('>:')
        else:
            break
    
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
    
    # set OS and drive letter
    cdrive = os_and_drive_letter()

    # set input path
    input_dir = input_path(cdrive)
    
    # set output path
    output_dir = output_path(cdrive)
    
    # input the data
    input_list, user_dtstructure = input_data()
    ip.read_data(input_list, user_dtstructure, input_dir)


if __name__ == "__main__":
    
    main()

    

    
    