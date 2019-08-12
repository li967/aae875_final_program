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
# 1. convert dataframe to float: 
# https://blog.csdn.net/qxqxqzzz/article/details/88356678
#
############################### 80 COLUMNS WIDE ################################

from df_pandas import statistics as dst


import statsmodels.api as sm
import pandas as pd
import os
import numpy as np

def convert_to_float(df):
    '''
    # convert all data to float for regression 
    # It seems like string should convert to float as well
    # @param: old dataframe
    # @return: new dataframe
    '''
    col = list(df.columns) # get col names
    df[col] = df[col].apply(pd.to_numeric, errors='coerce').fillna(0.0)
    data = pd.DataFrame(df, dtype='float')
    return data

def get_independent_vars():
    '''
    # prompt user to give the independent variables for regression 
    # split into a list
    # @param: none
    # @return: a list of independent variable name
    '''
    print('Please tell me all the independent variables. ', end = '')
    print('Use comma to seperate variables with capitalized each var name.')
    print('Ex: Indi Var1, Indi Var2, Indi Var3')
    user_input = input('>:').split(', ')
    
    return user_input

def get_dependent_var():
    '''
    # prompt user to give the dependent variables for regression
    # return the single string
    '''
    print('Please tell me the dependent variable you are interest in')
    return input('>:')
    
    
def lm(y, X, data):
    lhs = data[y]
    rhs = data[X]
    
    
    model = sm.OLS(lhs.astype(float), rhs.astype(float)).fit()
    print(model.summary())
    return model

def lm_from_input(data):
    '''
    # prompt user to enter the dependent and indepent variables 
    # do the regression and report
    # @param: dataframe
    # @return: fitted model
    '''
    lhs = data[get_dependent_var()]   # get denpendent variables
    rhs = data[get_independent_vars()]# get independent variables
    
    # do the regression 
    model = sm.OLS(lhs.astype(float), rhs.astype(float)).fit()
    print(model.summary())
    return model
    

if __name__ == '__main__':
    # uoload data
    # input_path = "G:\\Box Sync\\MyFiles\\875\\final_program_git\\aae875_final_program\\Input\\RawData"
    input_path = "/Users/liyuxuan/aae875_final_program/Input/RawData"
    data_name = os.path.join(input_path, 'user_data.csv')

    # upload data
    print('Upload data...')
    df = pd.read_csv(data_name, low_memory = False)
    print(df.columns.values.tolist())
    # slice data with useful vars
    print('Slicing data...')
    df = dst.slice_data(df)
    print(df.columns.values.tolist())
    print(df.head())
    
    # convert all data to foat
    df = convert_to_float(df)
    
    # test lm
    model1 = lm('Length of Stay',[
        "Gender", "Race", "Type of Admission", "Patient Disposition", 
        "Health Service Area", "Facility Id", "Discharge Year"], df)
    