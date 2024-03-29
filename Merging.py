from fpdf import FPDF
from PyPDF2 import PdfFileReader, PdfFileWriter
import locale
import random
from Gauges import gauge, gauge_cycle
import os
from pathlib import Path

def HBB(hrsRecMnth, accRecMnth, perAutoRec, accEmp):
    Hbb_low = 4.8*hrsRecMnth + 2.4*accRecMnth*(1-perAutoRec)
    Hbb_high = 5.7*hrsRecMnth + 2.85*accRecMnth*(1-perAutoRec)
    totalHrs =8*261*accEmp
    percRedHrs = (Hbb_high/totalHrs)*100
    return Hbb_low, Hbb_high, percRedHrs, totalHrs


def avgDays(industry_type):
    if industry_type == "Utilities" or industry_type == "Telecommunications" or industry_type == "Services" or industry_type == "Retail" or \
            industry_type == "Media and Entertainment" or industry_type == "Financial Services/Banking":
        Avg_days = '7'

    elif industry_type == "Pharmaceuticals" or industry_type == "Industrial Products" or industry_type == "Aerospace":
        Avg_days = '5'

    elif industry_type == "Petroleum/Chemicals" or industry_type == "Government-Military" or industry_type == "Electronics" \
            or industry_type == "Distribution/Transportation" or industry_type == "Consumer Products/Packaged Goods" or \
            industry_type == "Automotive" or industry_type == "CROSS-INDUSTRY":
        Avg_days = '6'

    elif industry_type == "Insurance":
        Avg_days = '9'

    elif industry_type == 'Healthcare':
        Avg_days = '10'
    return Avg_days


locale.setlocale(locale.LC_ALL, 'en_US')
# name=input("Enter name: ")
company = "RGP"
#potential = input('Enter the potential: ')

days = "5"
# Avg_days = input("Average days as per industry standards: ")

Industry_type = "Services"
Avg_days = avgDays(Industry_type)

if int(days) < int(Avg_days):
    cycle_time = 'FASTER than'
elif int(days) > int(Avg_days):
    cycle_time = 'SLOWER than'
else:
    cycle_time = 'SAME as'

AR = "30"
accEmp = 200
accRecMnth = 20
hrsRecMnth = 200

if int(days)>int(Avg_days) and float(AR)<50.0:
    potential='Tremendous'
elif int(days)>=int(Avg_days) or float(AR)<=50.0:
    potential='High'
else:
    potential='Medium'

perAutoRec = float(AR)/100

Hbb_low, Hbb_high, percRedHrs, totalHrs = HBB(hrsRecMnth, accRecMnth, perAutoRec, accEmp)

# The text to be added
# text1 = 'The Future of Work is Here, '+company

text2 = company+'\nToday'

text3 = 'Based on the inputs you provided and comparing your metrics'\
   ' to industry average, we have rated your optimization potential as '+potential

text4 = 'You indicated that it currently takes your finance department '+days+' days to complete your consolidated ' \
         'monthly financial reports. This is '+cycle_time+' the median amount of time for your industry. ' \
                                                          '(Industry Average: '+Avg_days+' days. Source: APQC.org'

text5 ='You indicated that about '+AR+'% of your accounts are currently automatically reconciled. Our research suggests ' \
                                      'top performers can automate in excess of 50% of their reconciliation process.'

text6 = company.upper()+'\nTOMORROW'
text7 = locale.format_string('%d', round(int(Hbb_low), -1), grouping=True) + ' - '+ locale.format_string('%d', round(int(Hbb_high), -1), grouping=True)
text8 = '(Up to '+str(round(percRedHrs, 1))+'% of your total '+locale.format_string('%d', totalHrs, grouping=True)+' annual accounting hours!)'

text9 = 'Our RPA experts will help '+company+' every step of the way!'

gauge(percAuto=float(AR), fname='test.png')
gauge_cycle(days=int(days), avgDays=int(Avg_days) )
#fig.show()
print('a')
pdf = FPDF()
pdf.add_font('Rubik-M', '', Path("../chat/pdf_personalization/Rubik/Rubik-Medium.ttf").resolve(), True)
print('font')
pdf.add_font('Rubik-L', '', Path("../chat/pdf_personalization/Rubik/Rubik-Light.ttf").resolve(), True)
pdf.add_font('Rubik-LI', '', Path("../chat/pdf_personalization/Rubik/Rubik-LightItalic.ttf").resolve(), True )
pdf.set_auto_page_break(True, margin=0.0)
pdf.add_page()
pdf.set_font("Rubik-M", size=36.86)
pdf.set_text_color(1, 199, 177)
print('b')
# pdf.set_xy(25,106.5)
# pdf.cell(1, 20, txt=name)
pdf.set_xy(25, 226.5)
pdf.cell(160, 20, txt=company.upper(), align='C')

pdf.add_page()
pdf.set_font("Rubik-M", size=32)
pdf.set_text_color(0, 43, 73)
pdf.set_xy(10, 36)
# pdf.cell(20, 20, txt=text1)
print('c')
pdf.add_page()
pdf.set_font("Rubik-M", size=37.35)
pdf.set_text_color(0, 43, 73)
pdf.set_xy(21.1, 41.2)
pdf.multi_cell(94, 11.557, txt=text2)

pdf.set_xy(21.1, 110) # 110
pdf.set_font("Rubik-L", size=10.37)
pdf.set_text_color(36, 36, 34)
pdf.multi_cell(94, 5, txt=text3) #90

pdf.set_xy(21.1, 168)
pdf.multi_cell(94, 5, txt=text4)

pdf.set_xy(21.1, 252)
pdf.multi_cell(94, 5, txt=text5)

pdf.set_xy(125, 98)
pdf.set_font('Rubik-M', size=32)
pdf.set_text_color(0, 199, 177)
pdf.cell(88.9, 11.557, txt=potential.upper(), align='C')
pdf.set_xy(136, 145)
pdf.image('gauge.png', w=70, h=60, type='png')
pdf.set_xy(126, 170)
pdf.set_text_color(0, 43, 73)
pdf.cell(88.9, 11.557, txt=days+' Days', align='C')

pdf.set_xy(136, 225)
pdf.image('test.png',w=70, h=60, type='png')

try:
    os.remove('test.png')
    os.remove('gauge.png')
except:
    pass

pdf.add_page()
# pdf.set_font('Rubik-M', size=37.35)
pdf.set_text_color(200, 16, 46)
pdf.set_xy(25, 40)
pdf.multi_cell(0, 11.557, txt=text6, align='C')

pdf.set_font('Rubik-M',size=80)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(20, 77)
pdf.cell(0, 42, txt=text7, align='C')

pdf.set_font('Rubik-LI', size=14)
pdf.set_xy(20, 131)
pdf.cell(0, 11.577, txt=text8, align='C')

pdf.add_page()
pdf.set_font('Rubik-L', size=16)
pdf.set_text_color(0, 43, 73)
# pdf.set_xy(25, 127)
pdf.set_xy(20, 126)
pdf.cell(0, 11.557, txt=text9, align='C')

print('d')

try:
    pdf.output("dynamic.pdf")
except Exception as e:
    print(e)
print('e')

output = PdfFileWriter()

ipdf = PdfFileReader(open("PDF_Template_Main.pdf", 'rb'))
wpdf = PdfFileReader(open('dynamic.pdf', 'rb'))
watermark1 = wpdf.getPage(0)
watermark2 = wpdf.getPage(1)
watermark3 = wpdf.getPage(2)
watermark4 = wpdf.getPage(3)
watermark5 = wpdf.getPage(4)

# for i in range(ipdf.getNumPages()):
#     page = ipdf.getPage(i)
#     page.mergePage(wpdf.getPage(i))
#     output.addPage(page)

page = ipdf.getPage(0)
page.mergePage(watermark1)
output.addPage(page)

page = ipdf.getPage(1)
page.mergePage(watermark2)
output.addPage(page)

page = ipdf.getPage(2)
page.mergePage(watermark3)
output.addPage(page)

page = ipdf.getPage(3)
page.mergePage(watermark4)
output.addPage(page)

output.addPage(ipdf.getPage(4))
output.addPage(ipdf.getPage(5))
output.addPage(ipdf.getPage(6))
output.addPage(ipdf.getPage(7))
output.addPage(ipdf.getPage(8))
output.addPage(ipdf.getPage(9))

page = ipdf.getPage(10)
page.mergePage(watermark5)
output.addPage(page)

output.addPage(ipdf.getPage(11))

file = './custom_pdfs/Output_PDF_New.pdf' + str(random.randint(10000,50000)) +'.pdf'
with open(file, 'wb') as f:
    output.write(f)

print(file)
