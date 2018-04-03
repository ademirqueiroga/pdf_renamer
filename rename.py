import os
import sys
import PyPDF2

def process(source, dest):
    with open(source, 'rb') as sourceFile:
        pdfReader = PyPDF2.PdfFileReader(sourceFile)
        print 'Pages: {}'.format(pdfReader.numPages)
        for i in range(pdfReader.numPages):
            page = pdfReader.getPage(i)
            fields = page.extractText().splitlines()
            fileName = fields[18].lower()
            print fileName

            with open(dest + fileName + '.pdf', 'wb') as newFile:
                pdfWriter = PyPDF2.PdfFileWriter()
                pdfWriter.addPage(page)
                pdfWriter.write(newFile)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Invalid arguments."
        print "Usage: python rename.py <source.pdf> <dest_folder>"
    else:
        source = sys.argv[1]
        dest = sys.argv[2]
        if not os.path.exists(dest):
            os.makedirs(dest)
        if dest[-1] != '/':
            dest += '/'
        process(source, dest)
