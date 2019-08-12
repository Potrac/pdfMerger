from PyPDF2 import PdfFileMerger
import argparse


parser = argparse.ArgumentParser(description='Merge pdfs')
parser.add_argument('path', nargs = '+',
                    help = 'merge pdfs')
parser.add_argument('-o', default = '',
                    help = 'output path (directory), default is current directory')
args = parser.parse_args()

pdf_paths = args.path
output_path = args.o

def pdfMerger(pdfs):
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf, bookmark = 'End of file') 
    with open(f"{output_path}pdf-merged.pdf", 'wb') as output:
        merger.write(output)
    return True

pdfMerger(pdf_paths)

