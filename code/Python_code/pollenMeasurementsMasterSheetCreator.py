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
import pandas as pd


#Define the paths to be used (the folder containing the .csv files, and the folder to write the output to)
multipleInputFilesCheck = input('Are there multiple input folders? (y/n)') #This is to check if the user is inputting files from multiple folders, or just one folder
if multipleInputFilesCheck == 'y':
    inputpath = askdirectory(title='Select Folder containing input .csv files') # shows dialog box and return the path
    print(inputpath) 
    #store the inputpath in a list called inputpathList
    inputpathList = []
    inputpathList.append(inputpath)
    while True:
        moreInputFolders = input('Are there more input folders? (y/n)')
        
        if moreInputFolders == 'y':
            newDirectory = input('What do you want to name the new directory? This will be the directory that contains all the input files. If it does not exist, it will be created. ')
            #trim the inputpath to just the last folder name, and add it to the newDirectory name
            print(newDirectory)
 
            # Split the path from the current inputpath
            head_tail = os.path.split(inputpath)
            print(head_tail)

            newDirectory = head_tail[0] + '/'+ newDirectory
            print(newDirectory)
            
            os.mkdir(newDirectory)

        while moreInputFolders == 'y':
            inputpath = askdirectory(title='Select Folder containing input .csv files') # shows dialog box and return the path
            inputpathList.append(inputpath)

            #remove duplicates from the list - This should make the following checks a little quicker when there are many input folders being used
            inputpathList = list(set(inputpathList))

            #check if the inputpath has been selected previously, and if so, skip it, and ask for another inputpath
            if inputpath in inputpathList:
                print('This input folder has already been selected')
                inputpath = askdirectory(title='Select Folder containing input .csv files') # shows dialog box and return the path


            #print('Files copied to new directory')
            moreInputFolders = input('Are there more input folders? (y/n)')

        if moreInputFolders == 'n':
            #copy all files in input path to a new directory for all input paths
            # for all files in the input path, copy them to the new directory
            for inputpath in inputpathList:
                for file in glob.glob(inputpath + '/*.csv'):
                    shutil.copy(file, newDirectory)
            break
    
else:
    inputpath = askdirectory(title='Select Folder containing input .csv files') # shows dialog box and return the path
    print(inputpath) 

if multipleInputFilesCheck == 'y':
    outputpath = newDirectory 
    print(outputpath)

else:
    outputpath = askdirectory(title='Select Folder to contain output .csv master spreadsheet') # shows dialog box and return the path
    print(outputpath)  


#Check if the MasterSheet already exists, and if not, create it
#If it does exist, ask the user if they want to overwrite it
if 'MasterSheet.csv' in os.listdir(outputpath):
    print('MasterSheet already exists')
    masterSheetRewrite = input('Do you want to overwrite the MasterSheet? (y/n)')
    if masterSheetRewrite == 'y':
        os.remove(outputpath + '/MasterSheet.csv')
        print('MasterSheet removed')
        with open(outputpath + '/MasterSheet.csv', 'w') as newMasterSheet:
            writer = csv.writer(newMasterSheet)
            writer.writerow(['_','Area','Perim.','Circ.','Feret','FeretX','FeretY','FeretAngle','MinFeret','AR','Round','Solidity','Family_ID','Individual_Plant_Number','Collection_Date','Imaging_Date','ImageProcessing_Date','Further_Data_Differentiation'])
            #NOTE that this header will need to be changed if the user is looking to utilize input data with different header(s)
    if masterSheetRewrite == 'n': 
        print('MasterSheet not removed')
        print('Exiting')
        quit()
else:
    with open(outputpath + '/MasterSheet.csv', 'w') as newMasterSheet:
        writer = csv.writer(newMasterSheet)
        #writer.writerow(['Image', 'Pollen Grain', 'Length', 'Width', 'Area', 'Perimeter', 'Circularity', 'Major Axis Length', 'Minor Axis Length', 'Angle'])
        writer.writerow(['_','Area','Perim.','Circ.','Feret','FeretX','FeretY','FeretAngle','MinFeret','AR','Round','Solidity','Family_ID','Individual_Plant_Number','Collection_Date','Imaging_Date','ImageProcessing_Date','Further_Data_Differentiation'])
        #NOTE that this header will need to be changed if the user is looking to utilize input data with different header(s)


        

#import csv files from input folder
#https://stackoverflow.com/a/44791486 - based on this code
        
allFilesin = glob.glob(inputpath + "/*.csv")
#allFilesin.sort()  # glob lacks reliable ordering, so impose your own if output order matters
MasterSheetdf = pd.concat((pd.read_csv(file) for file in allFilesin), ignore_index=True)
#save the resulting data frame as a .csv file in the output folder
MasterSheetdf.to_csv(outputpath + '/MasterSheet.csv', index=False)



print("MasterSheet Updated")