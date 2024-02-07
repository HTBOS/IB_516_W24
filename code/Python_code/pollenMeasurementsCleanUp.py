import pandas as pd

#Use user input to determine input and output paths

#Make this iterate through all files in the input folder.

# Read the CSV file
df = pd.read_csv('/c:/GIT/IB_516_W24/code/Python_code/pollenMeasurementsCleanUp.csv')

# Add the new columns
##CHECK THIS NOTATION
df['Family_ID'] = ''
df['Individual_Plant_Number'] = ''
df['Collection_Date'] = ''
df['Imaging_Date'] = ''
df['ImageProcessing_Date'] = ''

# Save the modified DataFrame back to the CSV file
df.to_csv('/c:/GIT/IB_516_W24/code/Python_code/pollenMeasurementsCleanUp.csv', index=False)

##Do I need to add a print statement to confirm that the new columns have been added?
##From here, import data from input file name
