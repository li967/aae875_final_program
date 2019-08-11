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

import os
import platform


def operating_system():
    '''
    # sets OS and drive letter. 
    # 1) The user is prompted to enter the computer's operating system. 
    #    Example: Windows, Mac.
    # 2) Sets the drive letter depending on the specified OS
    # @param: none
    '''
    # get os from user
    print('What is your computer\'s operating system?')
    user_os = input('>:')
    user_os = user_os.lower().replace(' ','')
    
    # set drives letter (for windows user)
    if user_os == 'windows':
        cdrive = str(os.getcwd()).split(os.path.sep)[0] + '\\'
        print('Nice. Your drive letter is now set to', cdrive)
        return cdrive
    else: # for mac user
        print('Nice. Your innitial working directory is now set to /Users')
        return '/Users/'

        
def input_path_conversation():
    '''
    # this function takes input path info provided by user 
    # Example:
    # USER PATH: C:\\classes\aae875\python
    # USER INPUT: "classes, aae875, python"
    # @param: none
    # @return: input_path
    '''
    # get input path from user
    print('\nWhat is your input path?')
    user_path = input('>:').split(', ')
    
    # join input path (depending on the OS)
    input_path = ''
    for token in user_path:
        input_path = os.path.join(input_path, token)
    
    # print checing information 
    print('Your input path is now set to', input_path)
    
    # return input_path
    return input_path
    
 
 
def output_path_conversation():
    '''
    # this function takes output path info provided by user
    # Example:
    # USER PATH: C:\\classes\aae875\python
    # USER INPUT: "classes, aae875, python"
    # @param: none
    # @return: output_path
    '''
    # get input path from user
    print('\nWhat is your output path?')
    user_path = input('>:').split(', ')
    
    # join output path (depending on OS)
    output_path = ''
    for token in user_path:
        output_path = os.path.join(output_path, token)
    
    # print checking information and return
    print('Your output path is now set to', output_path)      
    return output_path


def input_path(cdrive):
    '''
    # this function join the driver letter and input path
    # @param: none
    # @return: input_dir
    ''' 
    # call functions to get user inpupt path
    input_path = input_path_conversation()
    
    # merge the drive and input path and return
    input_dir = cdrive + input_path
    return input_dir
    


def output_path(cdrive):
    '''
    # this function join the drive letter and output path
    # @param: none
    # @return: output_dir
    '''
    # call functions to get user output path
    output_path = output_path_conversation()
    
    # merge the drive and input path and return
    output_dir = cdrive + output_path
    return output_dir

def data_structure_test():
    '''
    # get user-preferred data structure
    # test if the data structure chosen by user is valid, and 
    # return the matched structure (EX: input list(csv), return list)
    # if the user input structure is not valid, prompt to re-enter
    #
    # Available sutrctures:
    # list or list(csv), array or array(numpy), dataframe or datafroma(pandas)
    # @return: user_dtstructure (cleaned)
    '''
    # get data structure
    user_dtstructure = input('>:')
    
    # test if user_dtstructure is valid, if not, prompt to re-enter
    while True:
        # match the structures (remove the parentheses)
        user_dtstructure.lower()
        user_dtstructure = user_dtstructure.split('(')[0]
        if user_dtstructure in ['panda', 'pandas','df']:
            user_dtstructure = 'dataframe'
        if user_dtstructure in ['csv', 'l']:
            user_dtstructure = 'list'
        if user_dtstructure in ['numpy', 'num']:
            user_dtstructure = 'array'
        
        # test
        if not user_dtstructure in ['list', 'array', 'dataframe']:
            print("I don't know how to read this data structure.")
            print("Please try list, array or dataframe.")
            user_dtstructure = input('>:')
        else:
            break
    
    return user_dtstructure