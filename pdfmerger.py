from PyPDF2 import PdfFileMerger
import argparse


parser = argparse.ArgumentParser(description='Merge pdfs')
parser.add_argument('path', metavar='paths', nargs='+',
                    help='merge pdfs')
args = parser.parse_args()

pdf_paths = args.path

def pdfMerger(pdfs):
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf, bookmark = 'End of file') 
    with open("C:/Users/Olivier/Desktop/pdf-merged.pdf", 'wb') as output:
        merger.write(output)
    return True

pdfMerger(pdf_paths)

