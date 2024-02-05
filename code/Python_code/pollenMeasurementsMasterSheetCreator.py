###This script is meant to take all output .csv files from Fiji measurements of pollen grains and concatenate them into 1 coherent spreadsheet
##Note that this script assumes that the user is inputting in raw data to form a spreadsheet of ALL raw data. 
##This script needs minimal rewriting to process 'cleaned up' data, if desired 

#PACKAGES GO HERE
from tkinter import Tk
from tkinter.filedialog import askdirectory



#Define the paths to be used (the folder containing the .csv files, and the folder to write the output to)
inputpath = askdirectory(title='Select Folder containing input .csv files') # shows dialog box and return the path
print(inputpath) 

outputpath = askdirectory(title='Select Folder to contain output .csv master spreadsheet') # shows dialog box and return the path
print(outputpath) 


#Check if the MasterSheet already exists, and if not, create it
if '/MasterSheet.csv' in os.listdir(outputpath):
    print('MasterSheet already exists')
    masterSheetRewrite = input('Do you want to overwrite the MasterSheet? (y/n)')
    if masterSheetRewrite == 'y':
        os.remove(outputpath + '/MasterSheet.csv')
        print('MasterSheet removed')
        with open(outputpath + '/MasterSheet.csv', 'w') as newMasterSheet:
            writer = csv.writer(newMasterSheet)
            writer.writerow(['Image', 'Pollen Grain', 'Length', 'Width', 'Area', 'Perimeter', 'Circularity', 'Major Axis Length', 'Minor Axis Length', 'Angle'])
    if masterSheetRewrite == 'n': 
        print('MasterSheet not removed')
        print('Exiting')
        quit()
else:
    with open(outputpath + '/MasterSheet.csv', 'w') as newMasterSheet:
        writer = csv.writer(newMasterSheet)
        writer.writerow(['Image', 'Pollen Grain', 'Length', 'Width', 'Area', 'Perimeter', 'Circularity', 'Major Axis Length', 'Minor Axis Length', 'Angle'])




#If it does, ask the user if they want to overwrite it

#Create list of .csv files to be concatenated


