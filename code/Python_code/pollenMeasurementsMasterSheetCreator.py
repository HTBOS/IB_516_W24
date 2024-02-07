###This script is meant to take all output .csv files from Fiji measurements of pollen grains and concatenate them into 1 coherent spreadsheet
##Note that this script assumes that the user is inputting in raw data to form a spreadsheet of ALL raw data. 
##This script needs minimal rewriting to process 'cleaned up' data, if desired 

#PACKAGES GO HERE
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import csv ###do I need/want to import csv? Looking at just using glob and shutil
import glob
import shutil


#Define the paths to be used (the folder containing the .csv files, and the folder to write the output to)
multipleInputFilesCheck = input('Are there multiple input folders? (y/n)') #This is to check if the user is inputting files from multiple folders, or just one folder
if multipleInputFilesCheck == 'y':
    inputpath = askdirectory(title='Select Folder containing input .csv files') # shows dialog box and return the path
    print(inputpath) 
    while True:
        moreInputFolders = input('Are there more input folders? (y/n)')
        if moreInputFolders == 'y':
            inputpath = askdirectory(title='Select Folder containing input .csv files') # shows dialog box and return the path
            print(inputpath) ##Do I want to create a newDirectory to copy the files of ALL input folders to? If so, how do I do that?
        if moreInputFolders == 'n':
            break
    
else:
    inputpath = askdirectory(title='Select Folder containing input .csv files') # shows dialog box and return the path
    print(inputpath) 

outputpath = askdirectory(title='Select Folder to contain output .csv master spreadsheet') # shows dialog box and return the path
print(outputpath) 




#Check if the MasterSheet already exists, and if not, create it
#If it does, ask the user if they want to overwrite it
##Do I need this if I'm just going to do concatenation?
if '/MasterSheet.csv' in os.listdir(outputpath):
    print('MasterSheet already exists')
    masterSheetRewrite = input('Do you want to overwrite the MasterSheet? (y/n)')
    if masterSheetRewrite == 'y':
        os.remove(outputpath + '/MasterSheet.csv')
        print('MasterSheet removed')
        with open(outputpath + '/MasterSheet.csv', 'w') as newMasterSheet:
            writer = csv.writer(newMasterSheet)
            writer.writerow(['Image', 'Pollen Grain', 'Length', 'Width', 'Area', 'Perimeter', 'Circularity', 'Major Axis Length', 'Minor Axis Length', 'Angle'])
            #NOTE that this header will need to be changed if the user is looking to utilize input data with different header(s)
    if masterSheetRewrite == 'n': 
        print('MasterSheet not removed')
        print('Exiting')
        quit()
else:
    with open(outputpath + '/MasterSheet.csv', 'w') as newMasterSheet:
        writer = csv.writer(newMasterSheet)
        writer.writerow(['Image', 'Pollen Grain', 'Length', 'Width', 'Area', 'Perimeter', 'Circularity', 'Major Axis Length', 'Minor Axis Length', 'Angle'])
        #NOTE that this header will need to be changed if the user is looking to utilize input data with different header(s)


        

#import csv files from input folder
#https://stackoverflow.com/a/44791486 - based on this code
        
allFilesin = glob.glob(inputpath + "/*.csv")
allFilesin.sort()  # glob lacks reliable ordering, so impose your own if output order matters
with open('someoutputfile.csv', 'wb') as outfile:
    for i, filename in enumerate(allFilesin):
        with open(filename, 'rb') as infile:
            if i != 0:
                infile.readline()  # Throw away header on all but first file
            # Block copy rest of file from input to output without parsing
            shutil.copyfileobj(infile, outfile)
            print(filename + " has been imported.")

print("MasterSheet Updated")