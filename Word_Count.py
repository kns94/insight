#This file will calculate Word count of a given file and will write the output in a file wc_result.txt

#Input: File whose count has to be calculated
#Output: File names wc_result.txt
#Method: Split words and increment count

import re
import sys
import operator
import os
from os import listdir, path

destdir="wc_input"

#It will return list of all files in the folder
files = [ f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f)) ]
#print(files)

#output file path
output_path="wc_output"

#Default File
output_file_name="wc_result.txt"
	
#Path Name
output_complete_name = os.path.join(output_path, output_file_name) 

#Open output file
output_file=open(output_complete_name,'w')

#List of words
words={}


for f in files:

	#print(f)

	#input file path
	input_path="wc_input"

	#Input File
	input_file=f

	#Path Name
	input_complete_name = os.path.join(input_path, input_file) 

	for lines in open(input_complete_name):

		#print(lines+"\n\n")
	
		#splitting line by space
		word=lines.strip().split(' ')

		for item in word:
	
			#Removing unnecesary characters
			item=re.sub('[,,.,-,!,#,$,%,@,(,),*,&,^,+,-]',' ',item)
			item=item.replace(' ','')
			item=item.lower()
	
			if(item not in words):
				words[item]=1
			else:
				words[item]=words[item]+1

	sorted_words=sorted(words.items(),key=operator.itemgetter(0))

for item,count in sorted_words:
	output_file.write(item+" ")
	output_file.write(str(count))
	output_file.write("\n")

output_file.close()
