import os
import re
import glob

path="Inputfile"
path1="outputfile"

def Remove_Stop_Word(stopwords):
	"""
	"""
	for Inpfile in glob.glob(os.path.join(path,'*')):
		output_file_name=Inpfile.rsplit("\\",1)[1]
		review_file=open(Inpfile,'r').read().split()
		filter_file=[]
		for word in review_file:
			if re.sub('[^[A-Za-z0-9]+'," ",word) not in stopwords:
				filter_file.append(word)
		final_path=os.path.join(path1,output_file_name)
		with open(final_path,"w") as fp:
			fp.write(' '.join(filter_file))

if __name__ == '__main__':
	with open("stopwords.txt","r") as stopword_file:
		Remove_Stop_Word(list(map(lambda x: x.strip("\n").lower(),stopword_file.readline())))
								

