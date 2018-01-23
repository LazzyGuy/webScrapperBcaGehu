# Web Scrapping Script for Scrapping Multiple Result from Graphic Era Hill Result Bca course sem 5 mid term
# Site url http://14.139.239.134/MidResultHillDdn/MidResult.aspx/?rollno={Student Roll No}&course=BCA
# Poet -- Suraj Negi

import bs4  # Importing BeautifulSoup
from urllib.request import urlopen as uReq # Importing urlopen(function) from urllib.request(package) and Changing it to uReq for further use
from bs4 import BeautifulSoup as soup # Importing BeautifulSoup(function) from bs4(package) and Changing it to soup for further use

# Storing Main url in a variable
my_url = 'http://14.139.239.134/MidResultHillDdn/MidResult.aspx/?rollno=Student_Roll_No&course=BCA'

#------
#Target Roll No
# 1021412 - 1021540
#------


#Last Roll No
eRoll = 1021540


#Starting Roll No
ini_rollno = 1021411

# Opening Text File everyResult.txt for Saving Data
file = open("everyResult.txt","W")


# Loop End When Last roll no == to the prossing last Roll no

while ini_rollno!=eRoll:
    # A copy Of the original link
    dummy_url = my_url

    # Incrimenting The initial Roll No by one
    ini_rollno = ini_rollno + 1

    # Replacing the copy link with the roll no
    dummy_url = dummy_url.replace("Student_Roll_No",str(ini_rollno))

    # Requesting the url (Opening)
    uClient = uReq(dummy_url)

    # Reading the content
    page_html = uClient.read()

    # Closeing the connection
    uClient.close()

    # Parsing the content to html and saving it
    page_soup = soup(page_html,"html.parser")

    # Finding the Target content and saving the specific part
    # -- containers --> ResultSet
    containers = page_soup.findAll("div",{"id":"pnl_sem1"})

    # saving The first Item
    con = containers[0]

    # Geting the text content form source
    str = con.get_text()

    # String manipulation with the data String
    str = str.replace("\n","")
    str = str.replace("\r","")
    str = str.replace(" ","")
    str = str.replace("GraphicEraHillUniversitySocietyArea,ClementTownDehradun,Uttrakhand-248002www.gehu.ac.inSEMESTER:5COURSE:BCABRANCH:NAStatementofMarks,MidTermExamination2017(PROVISIONAL)","")

    # Writing the data int file
    file.write(str)
    file.write("\n")

file.close();
