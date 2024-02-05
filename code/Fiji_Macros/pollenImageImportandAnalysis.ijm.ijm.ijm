/*
 * This Macro is meant to import all images in a folder and process them one at a time - Processing includes enhancing the contrast of an image, thresholding the image locally, ensuring that the image is binary, segmentation of neighbouring objects by application of a watershed algorithm, followed by the analysis of objects and the production of a summary .csv file. This summary should then be saved to another(?) output directory in order to summarize the measurements for downstream applications. 
 */
 
/*
 * Based on template to process multiple images in a folder
 */

#@ File (label = "Input directory", style = "directory") input
#@ File (label = "Output directory", style = "directory") output
#@ String (label = "File suffix", value = ".lif") suffix
	//File suffix will needs to be user defined, and should be specific to the input file(s) to be processed

processFolder(input);
	// this defines a function to scan folders/subfolders/files to find files with correct suffix

function processFolder(input) {
	list = getFileList(input);
	list = Array.sort(list);
	for (i = 0; i < list.length; i++) {
		if(File.isDirectory(input + File.separator + list[i]))
			processFolder(input + File.separator + list[i]);
		if(endsWith(list[i], suffix))
			processFile(input, output, list[i]);
	}
}	//This is also a good place to check that your list captures all of the files you're interested in processing - NOTE Is it better to include a 'blacklist' of files that have already been processed previously and skip those to prevent 're'-processing OR to have multiple input folder, but a shared output folder? 

function processFile(input, output, file) {
	// Do the processing here by adding your own code.
	// Leave the print statements until things work, then remove them.
	run("Bio-Formats Importer", "open=file] color_mode=Default rois_import=	[ROI manager] view=Hyperstack stack_order=XYCZT use_virtual_stack series_1");

	//NOTE do I want to add a filter at any point? Gaussian? Other? 
	run("Enhance Contrast...", "saturated=0.35 equalize");

	run("8-bit");
	//Some input files will already be 8-bit, but this checks that the file is 8-bit, and if it isn't, converts it to an 8-bit image for the following thresholding

	run("Auto Local Threshold", "method=Bernsen radius=15 parameter_1=0 parameter_2=0"); //If you're unsure about which thresholding method is best for you image, consider trying the 'try all' setting found in the 'auto local threshold' function - NOTE Check this for lif images 

	setOption("BlackBackground", false);
	run("Convert to Mask");
	//Ensures that our image is binary, as required by 'Analyze Particles' function

	run("Analyze Particles...", "size=1500-15000 circularity=0.60-1.00 display exclude clear include");
	//Size, Circularity, and other parameters should be defined by user BEFORE this macro is run - For maize pollen, size = 1500-15000 and circularity .60-1.00 has proven to capture almost all pollen grains present, with the exception of cases where pollen grains are very close together and the watershed segmentation cannot seperate these objects. Size can also be defined in pixel units in cases where there is not (correct) metadata to aid in the conversion of pixels to other units of measurement (ie; microns) 
	
	if (isOpen("Results")) {
		name = getTitle()
  		selectWindow("Results");
  		saveAs("Measurements", name +, output + ".results.csv");
 		run("Close");

	//CHECK THIS FUNCTIONS FUNCTION

	print("Processing: " + input + File.separator + file);
	print("Saving to: " + output);
}



