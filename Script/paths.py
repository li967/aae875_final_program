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
        cdrive = str(os.getcwd()).split(os.path.sep)[0]
        print('Nice. Your drive letter is now set to', cdrive + '\\\\')
        return cdrive
    else: # for mac user
        print('Nice.')
        return ''

        
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
    input_dir = os.path.join(cdrive, input_path)
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
    output_dir = os.path.join(cdrive, output_path)
    return output_dir
