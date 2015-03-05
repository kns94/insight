#This file will calculate Median of all lines and will store it in a file med_result.txt

#Input: \wc_input\[All files] 
#Output: File named \wc_output\med_result.txt
#Method: Count words and calculate median

import re
import sys
import operator
import os
from os import listdir, path


def median(mylist):

	#Standard method to calculate median, sort the list and return middle value! 
	sorts = sorted(mylist)
	length = len(sorts)
	if not length % 2:
		return (sorts[int(length / 2)] + sorts[int(length / 2 - 1)]) / 2.0
	return sorts[int(length / 2)]

destdir="wc_input"

#It will return list of all files in the folder
files = [ f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f)) ]

#Sort Files
sorted_files=sorted(files)
#print(sorted_files)

#output file path
output_path="wc_output"

#Default File
output_file_name="med_result.txt"
	
#Path Name
output_complete_name = os.path.join(output_path, output_file_name) 

#Open output file
output_file=open(output_complete_name,'w')

#Length of lines will be added here! 
medianlist=[]

for f in files:

	#print(f)

	#input file path
	input_path="wc_input"

	#Input File
	input_file=f

	#Path Name
	input_complete_name = os.path.join(input_path, input_file) 


	for lines in open(input_complete_name):

		#splitting line by space
		word=lines.strip().split(' ')

		wordcount=0

		#Calculating word count in each line
		for item in word:
			wordcount=wordcount+1

		#Adding word count in list
		medianlist.append(wordcount)

		#Calculating median using median function
		med=float(median(medianlist))

		output_file.write(str(med))
		output_file.write("\n")

output_file.close()
