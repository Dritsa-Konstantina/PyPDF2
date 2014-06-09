from PyPDF2 import PdfFileReader
import sys

# This code demonstrates the usage of the getDocumentInfo method.
# author1 = Dritsa Konstantina <dritsa.konstantina@gmail.com>
# author2 = Papakitsos Ioannis <ioannispapak@gmail.com>

if (len(sys.argv) != 2):
    print("usage: python pdf_info.py file1.pdf")
    sys.exit(1)
		
print ("\nFile given as input: " + sys.argv[1] + ".")

input1 = PdfFileReader(open(sys.argv[1], "rb"))

while True:
    ans=raw_input("""
What would you like to know about the file you inserted?
1.Title
2.Author
3.Subject
4.Creator
5.Producer
6.Creation date
7.Date of last modification
8.Exit/Quit
""")
    
    if ans=="1": 
        print input1.getDocumentInfo().title
    elif ans=="2":
        print input1.getDocumentInfo().author 
    elif ans=="3":
        print input1.getDocumentInfo().subject 
    elif ans=="4":
        print input1.getDocumentInfo().creator
    elif ans=="5":
        print input1.getDocumentInfo().producer
    elif ans=="6":
        print input1.getDocumentInfo().creationDate
    elif ans=="7":
        print input1.getDocumentInfo().modDate
    elif ans=="8":
        sys.exit(1) 
    else:
        print("\nNot Valid Choice. Try again.")

