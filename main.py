from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://giris.eba.gov.tr/EBA_GIRIS/giris.jsp")

print("1-> Login into EBA\n2->Click \"Gruplar\"\n3->Click to the group you wanna export\n4->Click \"Üyeler\"\n5->Select type (Tümü|Öğrenciler|Öğretmenler|Okul Yöneticileri)")
input("Press Enter key when finished...")

soup = BeautifulSoup(driver.page_source, "html.parser") 
members = mydivs = soup.find_all("div", {"class": "vc-memberTitle"})
memberNames = []

for member in members:
    memberNames.append(member.text)

print(len(memberNames), "person's name received.")
print("Exporting to members.csv...")

f = open("members.csv", "a")
f.write("\n".join(str(x) for x in memberNames))
f.close()
