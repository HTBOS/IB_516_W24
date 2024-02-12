from tkinter import Tk
from tkinter.filedialog import askdirectory
import glob
import pandas as pd

inputpath = askdirectory(title='Select Folder containing input .csv spreadsheets to be cleaned up') # shows dialog box and return the path
print(inputpath)

outputpath = askdirectory(title='Select Folder to contain output .csv spreadsheets to be cleaned up') # shows dialog box and return the path
print(outputpath)

#Create list of files in input folder 
inputFiles = glob.glob(inputpath + '/*.csv')

#for each file in the list, add the new columns and save the modified DataFrame back to the CSV file
for file in inputFiles:
    df = pd.read_csv(file)
    df['Family_ID'] = ''   
    df['Individual_Plant_Number'] = ''
    df['Collection_Date'] = ''
    df['Imaging_Date'] = ''
    df['ImageProcessing_Date'] = ''
    df.to_csv(outputpath + '/pollenMeasurementsCleanUp.csv', index=False)

print('All files have been cleaned up and saved to the output folder')


