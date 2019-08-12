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
# Persons: 
# Online sources:
#
############################### 80 COLUMNS WIDE ################################

from df_pandas import input as dip
from df_pandas import cleaning as dcl
from df_pandas import statistics as dst
from df_pandas import regression as dreg

import pandas as pd

def input_data(input_list, input_dir, user_name):
    '''
    # input data as dataframe (in pandas), put into a list
    # @ param: input file name list, input_dir, user_name (for chatting)
    # @return: a list of dataframes
    '''
    data_list = dip.read_data(input_list, input_dir, user_name)
    return data_list

def data_cleaning(data_list, user_dtstructure, user_name, file_names):
    '''
    # chatting with user, cleaning data and report human-readable results
    # called by main.py
    # calling other modules in df_pandas 
    '''
    # get numbers of rows and columns
    nrow, ncol = dcl.rows_and_columns(data_list)
    print('You have %(nrow)d inpatient discharges and %(ncol)d variables\
     that document these observations.' %{
         'nrow':nrow, 'ncol':ncol})
    # chatting
    input(">:")
    input(">:")
    
    
    # drop missing values
    print('\nNo problem, I can help you with this. Let\'s clean the data first.')
    print('Would you like to drop observations with missing values?')
    input(":>")
    
    data_list = dcl.drop_missing_values(data_list) # drop missings
    nrow, ncol = dcl.rows_and_columns(data_list)   # update data shape after dropping
    print("\nI have removed all the missing values in your data.") # chatting
    print('You now have %(pat)d million inpatient discharges and %(var)d \
    that document these observations.' %{
        'pat':nrow, 'var':ncol})                   # chatting
    input(">:")
    
    # remove data outliers
    print("Right... would you like to remove data outliers?") 
    input(">:")
    
    data_list = dcl.drop_outliers(data_list)     # drop outliers using IQR boundary
    nrow, ncol = dcl.rows_and_columns(data_list) # update data shape after dropping
    print('\nI have removed all outliers in your data.')
    print('You now have %(pat)d inpatient discharges and %(var)d variables\
    that document these observations.'  %{
        'pat':nrow, 'var':ncol})                 # chatting
    input(">:")
    input(">:")
    
    # deal with not-matching column names 
    print('I am afraid this is not the best way to move forward.', end = ' ')
    print('The variable names in your data are not consistent over time.')
    data_colnames = dcl.compare_colnames(data_list, file_names) # get var names
    
    
    print('Let me put these in a table for you. Please see below:')
    print(data_colnames) # reporting variable names over year
    input('>:')# chatting, user require to align names
    
    print('Sure thing! I will use a dictionary for this. Processing...')
    data_list = dcl.align_colnames(data_list, data_colnames) # update col names
    data_colnames = dcl.compare_colnames(data_list, file_names) # get new names
    print('Variable names match those in year 2016 now. Please see below:')
    print(data_colnames)
    
    # merge data
    user_data = pd.concat(data_list)
    
    return user_data
        
        
def summary_stats(df, user_name):
    '''
    # summary stats plotting
    # @param: user_data (one dataframe)
    # @return:??
    '''
    
    # cut down unuseful variabls first (for quickly running)
    df = dst.slice_data(df)
    
    # chatting
    print('\nSure thing! I can plot some grphs for you.', end=' ')
    print('What do you want to know more precisely?')
    input('>:') # user ask asthma by type and year
    print('\nThis is a very interesting question,',user_name, end=' ')
    print('Let me prepare some graphs for you...')
    
    # plot number of asthma by admission type and year
    print('Here is what I found:')
    dst.plot_asthma_by_type_year(df)
    input('>:') # user command on graph
    
    # chatting
    print('\nIndeed, very interesting. Would you like me to plot some more graphs?')
    input('>:') # user ask for payment source
    print('\nIt seems there are 10 types of payment sources.', end = ' ')
    print('I think a pie chart is more appropriate here. Do you agree?')
    input('>:')
    
    # plot payment source in pie chart
    print('Interesting results again. Please see below what I found in the data:')
    dst.plot_payment_pie(df)
    input('>:')
    
    