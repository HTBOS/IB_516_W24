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
    #read in the CSV file as a DataFrame
    df = pd.read_csv(file)

    #save filename as string literal
    #We'll trim this down to just the file name, without the path, to use as the file name for the output file after grabbing some useful information.
    filename = str(file)
    print(filename)

    #add new columns to the DataFrame
    df['Family_ID'] = ''   
    df['Individual_Plant_Number'] = ''
    df['Collection_Date'] = ''
    df['Imaging_Date'] = ''
    df['ImageProcessing_Date'] = ''
    df['Further_Data_Differentiation'] = ''
    #df.to_csv(inputFiles + '/pollenMeasurementsCleanUp.csv', index=False)
    #save the modified DataFrame as a new CSV file in the output folder

#for each file in the list, add info to the new columns from the file name and save the modified DataFrame back to the CSV file
# example file name: "fC34_i2_c000024_i022224HB_p030624_Nkuwaraha"
#for file in inputFiles:
    
    #for 'Family_ID' column, populate with the first part of the file name, starting with 'f' 
    df['Family_ID'] = file.split('_')[1].split('f')[1]
    #print("The family ID is:", str(file.split('_')[1].split('f')[1]))

    #for 'Individual_Plant_Number' column, populate with the second part of the file name, starting with 'in'
    df['Individual_Plant_Number'] = file.split('_')[2].split('in')[1]
    #print("The individual plant number is:", str(file.split('_')[2].split('in')[1]))

    #for 'Collection_Date' column, populate with the third part of the file name, starting with 'c'
    df['Collection_Date'] = file.split('_')[3].split('c')[1]
    #print("The Date of Collection is:", str(file.split('_')[3].split('c')[1]))

    #for 'Imaging_Date' column, populate with the fourth part of the file name, starting with 'im'
    df['Imaging_Date'] = file.split('_')[4].split('im')[1]  
    #print("The Date of Imaging is:", str(file.split('_')[4].split('im')[1]))

    #for 'ImageProcessing_Date' column, populate with the fifth part of the file name, starting with 'p'
    df['ImageProcessing_Date'] = file.split('_')[5].split('p')[1]
    #print("The Date of Image Processing is:", str(file.split('_')[5].split('p')[1]))

    #for 'Further_Data_Differentiation' column, populate with the sixth part of the file name
    #check if there is an 'N' in the file name, if so, populate with the part of the file name after the 'Note'
    if 'N' in file.split('_')[6]:
        df['Further_Data_Differentiation'] = file.split('_')[6].split('Note')[1]
        print("There is a note to reference:", str(file.split('_')[6].split('Note')[1]))

    #print(file.split('_')[0])
    #print(file.split('_')[1])
    #print(file.split('_')[2])
    #print(file.split('_')[3])
    #print(file.split('_')[4])
    #print(file.split('_')[5])
    #print(file.split('_')[6])

    #replace specific headers with versions that can be interpreted by R (ie; "Sample_ID" instead of "Sample ID")
    df.columns = df.columns.str.replace(' ', '_')  #replace spaces with underscores
    df.columns = df.columns.str.replace('-', '_')  #replace dashes with underscores

    #save the dataframe to a new CSV file in the output folder and include the file name from the input
    if 'N' in file.split('_')[6]:
        #print("NOTES")

        #trim the file name down to just the file name, without the path
        filenametrimmed = file.split('/')[-1].split('_')[0]
        filenametrimmed = file.split("_", 1)[1]
        #print(str(filenametrimmed)+ " has notes")

        #print(str(outputpath + '/' + 'pollenMeasurementsUniform_' + filenametrimmed))
        df.to_csv(outputpath + '/' + 'pollenMeasurementsUniform_' + filenametrimmed, index=False)
    else:
        #print("NO NOTES")
        #trim the file name down to just the file name, without the path
        filenametrimmed = file.split('/')[-1].split('_')[0]
        filenametrimmed = file.split("_", 1)[1]
        #print(str(filenametrimmed)+ " has no notes")
        #print(str(outputpath + '/' + 'pollenMeasurementsUniform_' + filenametrimmed))
        df.to_csv(outputpath + '/' + 'pollenMeasurementsUniform_' + filenametrimmed, index=False)





print('All files have been cleaned up and saved to the output folder')


