from PyPDF2 import PdfFileMerger
import sys

# author Dritsa Konstantina <dritsa.konstantina@gmail.com>

merger = PdfFileMerger()

if (len(sys.argv) != 3):
        print("usage: python 2-up-merging.py file1.pdf file2.pdf")
        sys.exit(1)
		
print ("\nFiles given as input: " + sys.argv[1] + ", " + sys.argv[2] + ".")

input1 = open(sys.argv[1], "rb")
input2 = open(sys.argv[2], "rb")

f1pages=int(raw_input("\nEnter the number of pages you want to keep from the first file: \n"))
merger.append(fileobj = input1, pages = (0,f1pages))

merger.append(input2)

finalfile=raw_input("\nEnter the name of the final file you want to create.\nFor example output.pdf\n")
suffix='.pdf'

while not finalfile.endswith(suffix):
	finalfile=raw_input("Please enter a file name with the suffix \".pdf\" \n")
	
output = open(finalfile, "wb")
merger.write(output)

