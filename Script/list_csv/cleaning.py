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

from list_csv import input as ip
import pandas as pd
import numpy as np

def rows_and_columns(data_list):
    '''
    # get number of rows and cols in each dataframe in the data list
    # return the sum of row numbers and the maximum of col numbers. 
    # @param: data_list (a list of nested lists)
    # @return: (sum_nrow, max_ncol)
    '''
    nrow = sum([len(data) for data in data_list]) - 3 # disgard 3 headers
    ncol = max([len(data[0]) for data in data_list])
    
    return nrow, ncol

def drop_missing_values(data_list):
    '''
    # For each dataset in data_list, drop missing values
    # return a list with new datasets (without missing values)
    # @param:  data_list
    # @return: new_data_list
    '''
    
    for data in data_list:
        # drop unuseful variables (which contains too many missings)
        data = [row[0:29]+row[32:37] for row in data]

        # get row number of missing values
        missing_rnum = set()
        for index, row in enumerate(data):
            if row[27] == '':
                row[27] = 'NA'
            if row [28] == '':
                row[28] = 'NA'
            for cell in row: 
                if cell == '':
                    missing_rnum.add(index)
        # drop missing values
        missing_rnum = list(missing_rnum)
        missing_rnum.sort()
        for rnum in missing_rnum:
            data.pop(rnum)

    return data_list

def convert_var_to_float(data_list, varname):
    '''
    # for data in nested list, convert one variable to float
    # @param: data_list, varname
    # @return: new_data_list
    '''
    for data in data_list:
        # get header line
        loc = data[0].index(varname)
        # change
        for row in data[1:]:
            row[loc] = float(row[loc])
    return data_list
        

def drop_outliers(data_list):
    '''
    # Build up IQR cretiera for outliers based on each datasets,
    # For each dataset in data_list, drop outliers
    # Return a list with new datasets (without outliers)
    # @param: data_list
    # @return: new_data_list
    '''
    # get IQR boundaries for Length of Stay
    lgth_bound = [] 
    for data in data_list:
        
        # get length of stay data and sort
        loc = data[0].index("Length of Stay")
        lgth = [row[loc] for row in data[1:]]
        lgth.sort()
        
        # get IQR boundaries 
        q1loc= int(len(lgth)/4) # location for first quantile
        q3loc= 3 * q1loc        # location for third quantile
        q1 = lgth[q1loc]        # get 1st quantile
        q3 = lgth[q3loc]        # get 3rd quantile
        upperb = q1 - 1.5 * (q3 - q1)
        lowerb = q3 + 1.5 * (q3 - q1) # get boundaries for outliers
        print(q1loc, q3loc,q1,q3,lowerb,upperb)
        lgth_bound.append((lowerb,upperb))
        
    # remove outliers using IQR boundaries
    new_data_list = []
    for i, data in enumerate(data_list):
        loc = data[0].index("Length of Stay")
        print(loc)
        header = [data[0]]
        upperb = lgth_bound[i][1]
        lowerb = lgth_bound[i][0]
        print(upperb,lowerb,header)
        data_out = [row for row in data[1:] if (lowerb<=row[loc]<=upperb)]
        data_out = header + data_out
        new_data_list.append(data_out)
        
    return new_data_list


def compare_colnames(data_list, file_names):
    '''
    # compare variable names in multiple datasets
    # output a table for comparing
    # @param: data_list
    # @return: data_colnames (a dataframe of all data names)
    '''
    data_col = {}
    for i, data in enumerate(data_list):
        data_col.update({i:list(data[0][:37])})
    data_colnames = pd.DataFrame(data_col)
    
    return data_colnames


def align_colnames(data_list, data_colnames):
    '''
    # align inconsistent var names with the 2016 data
    # @param: data_list
    # @param: new_data_list
    '''
    data_list[0][0] = data_list[2][0]
    
    return data_list

def merge_data(data_list):
    '''
    # merge 3 data set into a long one
    # @param: data_list (a list of nested lists)
    # @return: data (a nested list)
    '''
    user_data = data_list[0][:] + data_list[1][1:] + data_list[2][1:]
    return user_data
    

    
    
if __name__ == '__main__':
    print("test1")
    #input_path = "G:\\Box Sync\\MyFiles\\875\\final_program_git\\aae875_final_program\\Input\\RawData"
    input_path = "/Users/liyuxuan/aae875_final_program/Input/RawData/"
    file_names = ['SPARCS2014.csv', 'SPARCS2015.csv', 'SPARCS2016.csv']
    # upload sample data
    print('Start...')
    from list_sample import data_list as data_list
    # data_list = ip.read_data(file_names, input_path)
    print('Over...')
    
    
    # test rows and cols
    print('raw data shape', rows_and_columns(data_list))
    # test drop missing value
    data_list = drop_missing_values(data_list)
    print('Drop missing', rows_and_columns(data_list))
    
    # convert length of stay, total cost, total charge to integer
    data_list = convert_var_to_float(data_list, 'Length of Stay')
    data_list = convert_var_to_float(data_list, "Total Charges")
    data_list = convert_var_to_float(data_list, "Total Costs")
    print('Convert',rows_and_columns(data_list))
    '''
    # test outliers
    data_list = drop_outliers(data_list)
    print('Outlier', rows_and_columns(data_list))
    print(data_list)
    '''
    
    # data col names
    data_colnames = compare_colnames(data_list, file_names) #compare raw
    print(data_colnames)
    
    
    data_list = align_colnames(data_list, data_colnames)    #rename
    data_colnames = compare_colnames(data_list, file_names) #compare new
    print(data_colnames)
    
    # merge data
    user_data = merge_data(data_list)
    
    # save cleaned list
    with open('list_clean.py', 'w') as f:
        f.write('user_data = %s' % user_data)
    
    '''
    # output cleaned data to json
    Export = user_data.to_csv(input_path +'user_data.csv')
    # merge data
    user_data_sample = user_data.sample(3000)
    Export = user_data_sample.to_csv(input_path +'user_data_sample.csv')
    '''
    
    