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
import csv
import os

def read_data(file_names, input_path):
    '''
    # this function reads in data (file_names)
    # @param: file_names (list), input_path
    '''
    # append input path to data name        
    read_list = [os.path.join(input_path,file) for file in file_names]
    
    # upload data
    file_list = []
    for token in read_list:
        print('Start uploading:', token)
        with open(token,'r') as f:
            data = list(csv.reader(f, delimiter = ','))
            for row in data:
                row[10] = str(row[10])
                row[35] = str(row[35])
                row[36] = str(row[36])
            file_list.append(data)
        print('Done upload:', token)
        
    return file_list
        
    
if __name__ == '__main__':
    #input_path = "G:\\Box Sync\\MyFiles\\875\\final_program_git\\aae875_final_program\\Input\\RawData"
    input_path = "/Users/liyuxuan/aae875_final_program/Input/RawData/"
    file_names = ['SPARCS2014.csv', 'SPARCS2015.csv', 'SPARCS2016.csv']
    
    data_list = read_data(file_names, input_path)
    print(data_list[0][0:10])
    
    # save list
    with open('list_full.py', 'w') as f:
        f.write('data_list = %s' % data_list)
      
               
         
     
            