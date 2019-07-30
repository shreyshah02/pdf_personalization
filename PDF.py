from fpdf import FPDF
import pdfrw
import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

pdf = FPDF()
pdf.add_font('Rubik', '', r'C:\Windows\Fonts\Rubik-Medium.ttf', True)
pdf.add_page()
pdf.set_font("Rubik", size=15)
name=input("Enter name: ")
company=input("Enter Company Name: ")
potential = input("Enter the potential")
# industry = input("Enter Industry: ")
# week=input("Enter Week of: ")
# RdH = input("Enter the redeployable hrs: ")

text1 = company+":\nBased on the inputs you provided and comparing your metrics to industry averages, we have rated" \
                " your optimization potential as "+potential

pdf.set_xy(25,106.5)
pdf.cell(1, 20, txt=name)
pdf.set_xy(125, 106.5)
pdf.cell(1, 20, txt=company)
pdf.set_xy(25, 126.5)
pdf.multi_cell(94,5, txt=text1)
# pdf.cell(1,20,txt=industry)
# pdf.set_xy(125,126.5)
# pdf.cell(1,20,txt=week)
# pdf.set_xy(25, 156.5)
# pdf.cell(150,20,txt=RdH, align="C")

pdf.output("simple_demo.pdf")

# output = PdfFileWriter()
#
# ipdf = PdfFileReader(open("PDF_demo.pdf",'rb'))
# wpdf = PdfFileReader(open('simple_demo.pdf','rb'))
# watermark=wpdf.getPage(0)
# for i in range(ipdf.getNumPages()):
#     page = ipdf.getPage(i)
#     page.mergePage(watermark)
#     output.addPage(page)
# with open('newfile.pdf', 'wb') as f:
#     output.write(f)
