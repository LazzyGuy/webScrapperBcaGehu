import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#http://14.139.239.134/MidResultHillDdn/StudentPanel.aspx


my_url = 'http://14.139.239.134/MidResultHillDdn/MidResult.aspx/?rollno=xxx&course=BCA'

#Starting rollno 1021412
sRoll = 1021412
#Ending rollno 1021539
eRoll = 1021540

ini_rollno = 1021411

#everyResult

file = open("everyResult.","w")

i=0
while i<127:
     
     dummy_url = my_url
     ini_rollno = ini_rollno + 1
     a = str(ini_rollno)
     dummy_url = dummy_url.replace("xxx",a)
     dummy_url = dummy_url.replace(" ","")
     uClient = uReq(dummy_url)
     page_html = uClient.read()
     uClient.close()
     page_soup = soup(page_html,"html.parser")
     containers = page_soup.findAll("div",{"id":"pnl_sem1"})
     con = containers[0]
     str1 = con.get_text()
     str1 = str1.replace("\n","")
     str1 = str1.replace("\r","")
     str1 = str1.replace(" ","")
     str1 = str1.replace("GraphicEraHillUniversitySocietyArea,ClementTownDehradun,Uttrakhand-248002www.gehu.ac.inSEMESTER:5COURSE:BCABRANCH:NAStatementofMarks,MidTermExamination2017(PROVISIONAL)","")
     file.write(str1)
     file.write("\n")
     i = i+1
file.close()
