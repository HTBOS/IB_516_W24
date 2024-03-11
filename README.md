# IB_516_W24
### This Repo is for the project portion of IB516 taken during Winter 2024
[This is a link to this repo](https://github.com/HTBOS/IB_516_W24)

## Objectives of this project
1. Script the upload of relatively large image files such as .lif files to an accesible repository (Box will be the repository for this project)
    * Note1: This step is not always neccisary if image hosting and image processing will take place on the same machine
2. Scipt the calling of 1 or more image files from Box (or other data repository) to a local machine or whever image processing will take place
    * See Note1
3. Automate image processing in Fiji with 1 or more Macros (.ijm)
    * Note2: .ijm Macros must be installed in the copy of Fiji/ImageJ being used for image processing
4. Script the automatic uploading of comma-seperated-value files to an accesible repository
    * Similiar to Note1
5. Automate calling and editing/concatenating of .csv files 
    
6. Automate statistical processing of measurements within R/RStudio
    * Note3: This may be delayed until a better R-package is designed / intergratable for this purpose

## Progress Tracker

Objective | Progress
----------|---------
Image Uploading | 100%
Image Calling | 95%
Fiji Processing Macro(s) | 95%
CSV file Uploading | 95%
CSV file Concatenation | 100%
CSV file Cleanup | 100%
Statistical Processing | 70%

![This is a creative commons liscenced illustration of a pollen grain](https://openclipart.org/download/252936/Pollen4.svg)

## "What is the purpose of this repo?"

Simply put, this workflow is meant to facilitate automated morphological measuring of individual maize pollen grains, as well as downstream concatentation, summarizing, and simple statistical scores for each pollen sample imaged via microscopy. 

## "How do I apply this repo's contents to my own projects"?

The workflow is fairly straight forward. 

Fiji/ImageJ image processing: 
-The pollenImageImportandAnalysis.ijm ... Image J Macro needs to be placed in the .jar folder of your copy of Fiji (ImageJ, but with many useful packages included, particulary some that are used by this macro!). After that, restart Fiji and run the macro. It will ask where the micrographs to be processed are, as well as where you'd like the outputs (Masks, measurement .csv files) to be placed. 

You can run all of the python scripts in a .bash script, or execute them one at a time:
- pollenMeasurementsUniformityandParsing.py first, then pollenMeasurementsMasterSheetCreator.py, followed by MasterSheetPolishing.py, and finishing with SummaryStats.py. I recommend running each script seperately at first, as each script asks for user input to determine where the .csv files to be processed are located, as well as what folder/directory you would like the output placed in. 

At this point, that's all there is! Downstream analysis are likely to differ from project to project, so I leave the next steps to you!




