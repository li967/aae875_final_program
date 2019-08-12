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

def reject_outliers(data, m=2):
    return data[abs(data - np.mean(data)) < m * np.std(data)]

# https://stackoverflow.com/questions/11686720/is-there-a-numpy-builtin-to-reject-outliers-from-a-list