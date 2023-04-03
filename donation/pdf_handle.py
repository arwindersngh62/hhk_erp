from reportlab.pdfgen import canvas

from num2words import num2words
# creates the pdf file
def hello(f_name,rec_no,name,amount,mode,date):
    c = canvas.Canvas(f_name)
    c.drawInlineImage("donform.jpeg", 40, 20,510,770)
    c.drawString(75,637,rec_no)
    c.drawString(75, 530, name)
    #c.drawString(475, 637, date_rec)
    c.drawString(265, 492, amount)
    c.drawString(170, 474, (str(num2words(amount))).capitalize())
    c.drawString(320, 318, 'U80211PB2017NPL046830')
    c.drawString(320, 285, 'AAECH2743L')
    c.drawString(320, 255, '8437833465')
    c.drawString(95, 318, mode)
    c.drawString(95, 284, date)
    c.save()
def hello1(f_name,rec_no,name,amount,mode,date,date_rec):
    print(f_name,rec_no,name,amount,mode,date,date_rec)
    c = canvas.Canvas(f_name)
    c.drawInlineImage("donform.jpeg", 40, 20,510,770)
    c.drawString(75,637,str(rec_no))
    c.drawString(75, 530, name)
    #c.drawString(475, 637, str(date_rec))
    c.drawString(265, 492, str(amount)   )
    c.drawString(170, 474, (str(num2words(amount))).capitalize())
    c.drawString(320, 318, 'U80211PB2017NPL046830')
    c.drawString(320, 285, 'AAECH2743L')
    c.drawString(320, 255, '8437833465')
    c.drawString(95, 318, mode)
    c.drawString(95, 284, str(date))
    c.save()
hello1("Harinder Kaur1003.pdf","1003","Harinder Kaur","5000","INET","2021-03-24","2021-03-27")