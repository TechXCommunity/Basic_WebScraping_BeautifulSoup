import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com"

# step 1 :- Get the HTML
r = requests.get(url)
htmlContent = r.content
print(htmlContent)
# Step 2:- parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

# Step 3:-HTML tree traversal
# get the title of the HTML page
title = soup.title
print(type(title.string))

# commonly used types of objects :-
# 1- Tag
# 2- Navigable string
# 3-BeautifulSoup
# 4-Comment
# Get all the paragraphs from the page
paras = soup.findAll('p')
print(paras)
# Get all the anchor tags from the page
anchors= soup.findAll('a')
print(anchors)
# finding the first paragraph in the html page
print(soup.find('p'))
# get classes of any html page
print(soup.find('p')['class'])
# Find all the elements with class lead
print(soup.find_all("p",class_="lead"))
# Get the text from the tags/soup
print(soup.find('p').get_text())
# Get all the Links on the page
all_links=set()
for link in anchors:
    if(link.get('href') !='#'):# so that it excludes bound
        linkText="https://www.codewithharry.com"+link.get('href')
        all_links.add(link)
        print(linkText)











