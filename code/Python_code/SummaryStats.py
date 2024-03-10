from tkinter import Tk
from tkinter.filedialog import askdirectory
import glob
import pandas as pd

inputpath = askdirectory(title='Select Folder containing input .csv spreadsheet(s) to be cleaned up') # shows dialog box and return the path
print(inputpath)

outputpath = askdirectory(title='Select Folder to contain output .csv spreadsheet following cleaning') # shows dialog box and return the path
print(outputpath)

#in the inputpath, look for Polished_MasterSheet.csv and open it as a DataFrame
#If you want to do this for all files in the input folder, you can use glob to get a list of all the files in the input folder, and then loop through the list of files to open each one as a DataFrame
df = pd.read_csv(inputpath + '/Polished_MasterSheet.csv')

##Mask#,Area,Perim.,Circ.,Feret,MinFeret,AR,Round,Solidity,Family_ID,Individual_Plant_Number,Collection_Date,Imaging_Date,ImageProcessing_Date,Further_Data_Differentiation,Family_Individual_Note
## need to calculate the mean, median, standard deviation, kurtosis, and skewness for the Area, Perim.,Circ.,Feret,MinFeret,AR,Round, and Solidity columns for each unique value in the 'Family_Individual_Note' column
##For each column, calculate the mean, median, and standard deviation and save these values to a new DataFrame
summary_stats = pd.DataFrame(columns=['family_individual_note', 'area_Mean', 'area_Median', 'area_std_dev', 'SBC_Area', 'perimeter_Mean', 'perimeter_Median', 'perimeter_std_dev', 'SBC_Perim', 'circ_Mean', 'circ_Median', 'circ_std_dev', 'SBC_Circ', 'feret_Mean', 'feret_Median', 'feret_std_dev', 'SBC_Feret', 'minFeret_Mean', 'minFeret_Median', 'minFeret_std_dev', 'SBC_MinFeret', 'AR_Mean', 'AR_Median', 'AR_std_dev', 'SBC_AR', 'round_Mean', 'round_Median', 'round_std_dev', 'SBC_Round', 'solidity_Mean', 'solidity_Median', 'solidity_std_dev', 'SBC_Solidity'])

#Calculate the mean, median, and standard deviation for the Area column for each unique value in the 'Family_Individual_Note' column
for family_individual_note in df['Family_Individual_Note'].unique():
    #create a new DataFrame for the current family_individual_note
    current_df = df[df['Family_Individual_Note'] == family_individual_note]
    #calculate the mean, median, and standard deviation for the Area column
    area_Mean = current_df['Area'].mean()
    area_Median = current_df['Area'].median()
    area_std_dev = current_df['Area'].std()

    perimeter_Mean = current_df['Perim.'].mean()
    perimeter_Median = current_df['Perim.'].median()
    perimeter_std_dev = current_df['Perim.'].std()

    circ_Mean = current_df['Circ.'].mean()
    circ_Median = current_df['Circ.'].median()
    circ_std_dev = current_df['Circ.'].std()

    feret_Mean = current_df['Feret'].mean()
    feret_Median = current_df['Feret'].median()
    feret_std_dev = current_df['Feret'].std()

    minFeret_Mean = current_df['MinFeret'].mean()
    minFeret_Median = current_df['MinFeret'].median()
    minFeret_std_dev = current_df['MinFeret'].std()

    AR_Mean = current_df['AR'].mean()
    AR_Median = current_df['AR'].median()
    AR_std_dev = current_df['AR'].std()

    round_Mean = current_df['Round'].mean()
    round_Median = current_df['Round'].median()
    round_std_dev = current_df['Round'].std()

    solidity_Mean = current_df['Solidity'].mean()
    solidity_Median = current_df['Solidity'].median()
    solidity_std_dev = current_df['Solidity'].std()

    #capture the kurtosis and skewness for each column
    Area_kurtosis = current_df['Area'].kurtosis()
    Area_skewness = current_df['Area'].skew()

    Perim_kurtosis = current_df['Perim.'].kurtosis()
    Perim_skewness = current_df['Perim.'].skew()

    Circ_kurtosis = current_df['Circ.'].kurtosis()
    Circ_skewness = current_df['Circ.'].skew()

    Feret_kurtosis = current_df['Feret'].kurtosis()
    Feret_skewness = current_df['Feret'].skew()

    MinFeret_kurtosis = current_df['MinFeret'].kurtosis()
    MinFeret_skewness = current_df['MinFeret'].skew()

    AR_kurtosis = current_df['AR'].kurtosis()
    AR_skewness = current_df['AR'].skew()

    Round_kurtosis = current_df['Round'].kurtosis()
    Round_skewness = current_df['Round'].skew()

    Solidity_kurtosis = current_df['Solidity'].kurtosis()
    Solidity_skewness = current_df['Solidity'].skew()

    #calculate the Sarle's bimodality coefficient for each column
    SBC_Area = (Area_skewness**2 + 1) / (Area_kurtosis)  #This is one(!!!) formula for Sarle's bimodality coefficient, but may need to be checked for usage on our distributions, given that the pollen grains in our images are 'randomly sampled', but we may need to randomly sample from our resulting measurements to calculate this coefficeint correctly.
    SBC_Perim = (Perim_skewness**2 + 1) / (Perim_kurtosis)
    SBC_Circ = (Circ_skewness**2 + 1) / (Circ_kurtosis)
    SBC_Feret = (Feret_skewness**2 + 1) / (Feret_kurtosis)
    SBC_MinFeret = (MinFeret_skewness**2 + 1) / (MinFeret_kurtosis)
    SBC_AR = (AR_skewness**2 + 1) / (AR_kurtosis)
    SBC_Round = (Round_skewness**2 + 1) / (Round_kurtosis)
    SBC_Solidity = (Solidity_skewness**2 + 1) / (Solidity_kurtosis)

    
    #create a list of the current family_individual_note, mean, median, and standard deviation for all above specified columns/measures.
    summary_stats_list = [family_individual_note, area_Mean, area_Median, area_std_dev, SBC_Area, perimeter_Mean, perimeter_Median, perimeter_std_dev, SBC_Perim, circ_Mean, circ_Median, circ_std_dev, SBC_Circ, feret_Mean, feret_Median, feret_std_dev, SBC_Feret, minFeret_Mean, minFeret_Median, minFeret_std_dev, SBC_MinFeret, AR_Mean, AR_Median, AR_std_dev, SBC_AR, round_Mean, round_Median, round_std_dev, SBC_Round, solidity_Mean, solidity_Median, solidity_std_dev, SBC_Solidity]
    
    #write the list to the summary_stats DataFrame as a new row, with each item in the list in a separate column
    summary_stats.loc[len(summary_stats)] = summary_stats_list

#save the summary_stats DataFrame as a new CSV file in the output folder
summary_stats.to_csv(outputpath + '/' + 'SummaryStats.csv', index=False)

