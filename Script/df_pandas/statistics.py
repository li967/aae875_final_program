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

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def slice_data(df):
    '''
    # keep only variables that are useful
    # '''
    cols = [5,7,10,11,13,15,26,27,28,35,36]
    df1 = df.iloc[:,cols]
    
    return df1
    
    
def add_label(ax):
    ''' add data label on each bar for bar chart'''
    for p in ax.patches:
        x=p.get_bbox().get_points()[:,0]
        y=p.get_bbox().get_points()[1,1]
        ax.annotate('{:3.0f}'.format(y),(x.mean(),y),ha='center',va='bottom')
        
def sns_asthma_by_type_year(df):  
    ''' bar plot the number of survived and died people by class'''
    ax = sns.countplot(x = 'Pclass', hue = 'Survived', palette = 'Set1', data = df)
    ax.set(title = 'Passenger status (Survived/Died) against Passenger Class (sns)', 
           xlabel = 'Passenger Class', ylabel = 'Total')
    add_label(ax)
    plt.show()




if __name__ == '__main__':
    input_path = "/Users/liyuxuan/aae875_final_program/Input/RawData/"
    
    # upload data
    df = pd.read_json(input_path + 'user_data.json')
    
    # slice data wiht useful vars
    df = slice_data(df)
    print(df.colu)
    
    # plot 
    sns_asthma_by_type_year(df)
    
    