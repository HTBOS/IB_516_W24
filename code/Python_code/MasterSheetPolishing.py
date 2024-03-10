from tkinter import Tk
from tkinter.filedialog import askdirectory
import glob
import pandas as pd

inputpath = askdirectory(title='Select Folder containing input .csv spreadsheet(s) to be cleaned up') # shows dialog box and return the path
print(inputpath)

outputpath = askdirectory(title='Select Folder to contain output .csv spreadsheet following cleaning') # shows dialog box and return the path
print(outputpath)

#in the inputpath, look for MasterSheet.csv and open it as a DataFrame
#If you want to do this for all files in the input folder, you can use glob to get a list of all the files in the input folder, and then loop through the list of files to open each one as a DataFrame
df = pd.read_csv(inputpath + '/MasterSheet.csv')

#for each file, remove these columns from the DataFrame: FeretX, FeretY, FeretAngle
df = df.drop(columns=['FeretX', 'FeretY', 'FeretAngle'])

#create new column called 'Family_Individual_Note' and populate it with the contents of the 'Family_ID', 'Individual_Plant_Number', and 'Further_Data_Differentiation' columns
df['Family_Individual_Note'] = ""

#for each row, populate the 'Family_Individual_Note' column with the contents of the 'Family_ID', 'Individual_Plant_Number', and 'Further_Data_Differentiation' columns by using the .join() function
for index, row in df.iterrows():
    df.at[index, 'Family_Individual_Note'] = '_'.join([str(row['Family_ID']), str(row['Individual_Plant_Number']), str(row['Further_Data_Differentiation'])])


#save the modified DataFrame as a new CSV file in the output folder
df.to_csv(outputpath + '/' + 'Polished_MasterSheet.csv', index=False)

print('The MasterSheet has had the desired columns dropped, and has been saved to the output folder')

## At 3:48pm, 03/08/2024, I ran this code successfully for the first time. I felt true bliss. 