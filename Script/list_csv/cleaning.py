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
        data = [row[0:29]+row[31:37] for row in data]
        # get row number of missing values
        missing_rnum = set()
        for index, row in enumerate(data):
            for cell in row: 
                if cell == '':
                    missing_rnum.add(index)
        print(data[0:10])
        # drop missing values
        print(missing_rnum)
        missing_rnum = list(missing_rnum)
        missing_rnum.sort()
        print(missing_rnum)
        for rnum in missing_rnum:
            data.pop(rnum)

    return data_list

def drop_outliers(data_list):
    '''
    # Build up IQR cretiera for outliers based on each datasets,
    # For each dataset in data_list, drop outliers
    # Return a list with new datasets (without outliers)
    # @param: data_list
    # @return: new_data_list
    '''
    # get IQR boundaries for each column in each dataset
    Q1  = [data.quantile(0.25) for data in data_list]
    Q3  = [data.quantile(0.75) for data in data_list]
    IQR = [Q3[i] - Q1[i] for i in range(len(Q1))]
    upperb = [Q1[i] - 1.5 * IQR[i] for i in range(len(IQR))]
    lowerb = [Q3[i] + 1.5 * IQR[i] for i in range(len(IQR))]

    
    # drop outliers
    new_data_list = []
    for i, data in enumerate(data_list):
        data_out = data[~ (data > lowerb[i]) | (data < upperb[i])]
        new_data_list.append(data_out)
        
    return new_data_list

def compare_colnames(data_list, file_names):
    '''
    # compare variable names in multiple datasets
    # output a table for comparing
    # @param: data_list
    # @return: data_colnames (a dataframe of all data names)
    '''
    data_colnames = pd.DataFrame([data.columns.values.tolist() for data in data_list])
    data_colnames = data_colnames.T
    data_colnames.columns = file_names
    return data_colnames

def align_colnames(data_list, data_colnames):
    '''
    # align inconsistent var names with the 2016 data
    # @param: data_list
    # @param: new_data_list
    '''
    # put var names standards in dictionaries
    std = {}
    for i in range(data_colnames.shape[0]):
        std.update({str(data_colnames.iloc[i,0]):str(data_colnames.iloc[i,2])})
        
    # rename datasets using dictionaries
    new_data_list = [data.rename(columns = std) for data in data_list]
    
    return new_data_list
    
    

    
    
if __name__ == '__main__':
    #input_path = "G:\\Box Sync\\MyFiles\\875\\final_program_git\\aae875_final_program\\Input\\RawData"
    input_path = "/Users/liyuxuan/aae875_final_program/Input/RawData/"
    file_names = ['SPARCS2014.csv', 'SPARCS2015.csv', 'SPARCS2016.csv']
    # upload sample data
    from list_sample import data_list as data_list
    # data_list = ip.read_data(file_names, input_path)
    
    # test rows and cols
    print('raw data shape', rows_and_columns(data_list))
    # test drop missing value
    data_list = drop_missing_values(data_list)
    print('Drop missing', rows_and_columns(data_list))
    # test outliers
    data_list = drop_outliers(data_list)
    print('Outlier', rows_and_columns(data_list))
    
    # data col names
    data_colnames = compare_colnames(data_list, file_names) #compare raw
    print(data_colnames)
    data_list = align_colnames(data_list, data_colnames)    #rename
    data_colnames = compare_colnames(data_list, file_names) #compare new
    print(data_colnames)
    
    # merge data
    user_data = pd.concat(data_list)
    # output cleaned data to json
    Export = user_data.to_csv(input_path +'user_data.csv')
    # merge data
    user_data_sample = user_data.sample(3000)
    Export = user_data_sample.to_csv(input_path +'user_data_sample.csv')
    
    