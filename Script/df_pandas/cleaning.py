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

from df_pandas import input as ip

def rows_and_columns(data_list):
    '''
    # get number of rows and cols in each dataframe in the data list
    # return the sum of row numbers and the maximum of col numbers. 
    # @param: data_list (a list of dataframe)
    # @return: (sum_nrow, max_ncol)
    '''
    nrow = sum([data.shape[0] for data in data_list])
    ncol = max([data.shape[1] for data in data_list])
    
    return nrow, ncol


if __name__ == '__main__':
    #input_path = "G:\\Box Sync\\MyFiles\\875\\final_program_git\\aae875_final_program\\Input\\RawData"
    input_path = "/Users/liyuxuan/aae875_final_program/Input/RawData/"
    file_names = ['SPARCS2014.csv', 'SPARCS2015.csv', 'SPARCS2016.csv']
    
    data_list = ip.read_data(file_names, input_path)
    rows_and_columns(data_list)

    