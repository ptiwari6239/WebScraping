from bs4 import BeautifulSoup
import requests

html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text)
soup= BeautifulSoup(html_text,'lxml')
jobs= soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs :
    CompName=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
    skills=job.find('span',class_='srp-skills').text.replace(' ','')
    print("Company Name " ,end='')
    print(CompName, end='\n')
    print(f'skills required {skills}')
