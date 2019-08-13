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
import os


def slice_data(df):
    '''
    # Keep useful data only
    #
    # the "useful" vars are:
    # ['Health Service Area', 'Facility Id', 'Facility Name', 'Age Group', 
    # 'Gender', 'Race', 'Length of Stay', 'Type of Admission', 'Patient Disposition', 
    # 'Discharge Year', 'CCS Diagnosis Description', 
    # 'Payment Typology 1', 'Payment Typology 2', 'Payment Typology 3', 
    # 'Total Charges', 'Total Costs']
    #
    # @param: original dataframe
    # @return: new dataframe
    '''
    # select data as described above
    cols = [1,4,5,6,8,9,11,12,13,14,16,27,28,29,34,35]
    df = df.iloc[:,cols]
    
    return df

def filter_asthma(df):
    '''
    # filter data to those with asthma
    # @param: old dataframe
    # @return : new dataframe
    '''
    return df.loc[df['CCS Diagnosis Description'] == 'Asthma']
    
    
def add_label(ax):
    ''' add data label on each bar for bar chart'''
    for p in ax.patches:
        x=p.get_bbox().get_points()[:,0]
        y=p.get_bbox().get_points()[1,1]
        ax.annotate('{:3.0f}'.format(y),(x.mean(),y),ha='center',va='bottom')
        
def plot_asthma_by_type_year(df):  
    ''' bar plot the number of survived and died people by class'''
    ax = sns.countplot(x = 'Discharge Year', 
                       hue = 'Type of Admission', 
                       palette = 'Set1', 
                       data = df)
    
    ax.set(title = 'Type of admission with asthma conditions by year', 
           xlabel = 'Discharge Year', ylabel = 'Admissions with asthma')
    
    add_label(ax)
    plt.show()
    
    
    
def plot_payment_pie(df):
    ''' pie plot payment resources'''
    
    # grab all payment information into one column
    df_payment =pd.concat([df.loc[:,['Payment Typology 1']]
                           .rename(columns = {'Payment Typology 1':'PayType'}),
                           df.loc[:,['Payment Typology 2']]
                           .rename(columns = {'Payment Typology 2':'PayType'}),
                           df.loc[:,['Payment Typology 3']]
                           .rename(columns = {'Payment Typology 3':'PayType'})])
    
    # prepare data to plot
    labels = df_payment['PayType'].unique().tolist()
    sizes = [df_payment[df_payment.PayType == paytype]["PayType"].count() 
            for paytype in labels]
    
    # instead of percentage, show the actual number
    # tot = sum(sizes)
    # autopct = lambda x: "%d" % round(x*tot/100,2)
    
    # plot
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    
    # title
    plt.title('Payment Resources of Patients with Asthma', fontsize=20)
    
    # legend (redundant)
    # patches, texts = plt.pie(sizes)
    # plt.legend(patches, labels, loc="lower right")
    
    # produces a perfectly circular chart
    plt.axis('equal')
    
    plt.show()
    



if __name__ == '__main__':    
    # input_path = "G:\\Box Sync\\MyFiles\\875\\final_program_git\\aae875_final_program\\Input\\RawData"
    input_path = "/Users/liyuxuan/aae875_final_program/Input/RawData"
    data_name = os.path.join(input_path, 'user_data.csv')

    # upload data
    df = pd.read_csv(data_name)
    print(df.columns.values.tolist())
    # slice data with useful vars
    df = filter_asthma(slice_data(df))
    print(df.columns.values.tolist())
    print(df.head())
    
    # plot admission with asthma by admission type and year
    plot_asthma_by_type_year(df)
    
    print(df.head(10))
    
    # plot payment resource
    plot_payment_pie(df)
    
    
    