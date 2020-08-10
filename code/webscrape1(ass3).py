# The python file I'm currently using to do web scrape on Nei.st
# importing the library that I am going to use in this task
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import csv
import time
# Goal: I would like to go through all of the pages of a news aggregator website
# and get several infomation of news from different major news outlets: 
# 1. the year they are posted
# 2. headline
# 3. link
# 4. intro/foreword
# 5. what page the news is on on this website (for reference)
# Then I would like to retrieve all the news articles on this website and save them as separate text files at a local space.

# The next block is commented out because I chose not to 
# create new html files locally for every page but directly work with the pages
# url='https://nei.st/2020/page/{}'
# with urllib.request.urlopen(url) as request:
#     contents = request.read()
# save it locally
# html_string = contents.decode()
# with open('nei.html', 'w', encoding="utf8") as wf:
#     wf.write(html_string)
# with open ('nei.html', 'r', encoding="utf8") as rf:
#     html = rf.read()
# soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())

# This is the first url that I am going to work with
url='https://nei.st/2020/'
# because we would repeat a lot of operations in this web scraping task, I made a function to avoid writing the same code again
def yearscrape(url,year):
    # Session helps to persist certain parameters across requests but I didn't use its feature that much
    with requests.Session() as session:
        # whatever the year of news we are scraping, we start from page 1
        page_number = 1
        while True:
            # get the url, provide the user agent string
            response = session.get(url, headers={'User-Agent':'Julianna'})
            # get the content of the page
            soup = BeautifulSoup(response.content,'lxml')
            # find all articles in that page
            for article in soup.find_all("article"):
                # get the headline of the article
                headline = article.h2.a.text
                # “/” occurs in some headlines and when creating the text file the computer thinks it's a path, leading to an error
                # Don' know other ways to handle this lol
                headline = headline.replace("/","\\")
                print(headline)
                # get the link of the article
                link = article.find('a')['href']
                print(link)
                # get the intro of the article. Because for some articles the intro part is None, 
                # so I made if-else statement to avoid error in trying to get text of a NoneType object
                if article.find('div', class_='entry-summary').p is None:
                    intro = "Please get it online"
                else:
                    intro = article.find('div', class_='entry-summary').p.text
                    print(intro)
                
                print()
                # then write the line of the article with its year, headline, link, intro and page (for tracking and reference) into the csv file
                csv_writer.writerow([year, headline, link, intro, page_number])
                time.sleep(.01)
            
            # on the current page I am on I can get the url of next page
            next_link=soup.find('div', class_="nav-previous")
            # if there's no next page for this year, then stop there
            if next_link is None:
                break
            # change the link to the link of next page
            url = urljoin(url, next_link.a["href"])
            # adding the page number
            page_number += 1

# open a new file to write in all the information I extracted for the news articles
# with open('nei_scrape2020_1.csv','w') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter='\t')
#     # write in the first row
#     csv_writer.writerow(['Year','Headline', 'Link', 'Intro', 'Page'])
#     # do web scraping by years. For this website the news articles available are from 2018 to 2020
#     yearscrape('https://nei.st/2020/',2020)
#     # yearscrape('https://nei.st/2019/',2019)
#     # yearscrape('https://nei.st/2018/',2018)
# print("Congrats! nei_scrape.csv has been created and completed.")

# Let's go into the links of the news and get the articles, and save them separately as text files
# Caution: it takes a long time to get all articles downloaded as saved!
with open('nei_scrape2020_1.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # skip the first title line
    next(csv_reader)
    # for all the rest of the lines, find each article's headline and link
    with open("articles2020.csv", "a",encoding="utf8") as wf:
        csv_writer = csv.writer(wf, lineterminator='\n')
        for line in csv_file.readlines():
            line = list(line.split("\t"))
            headline = (line[1])
            link = (line[2])
            # create a new text file with the headline as file name
            # using the link to reach the article page
            response = requests.get(link)
            # get the page content
            soup = BeautifulSoup(response.content,'lxml')
            # find where all the paragraphs are
            paragraphs = soup.find("article").find_all("p")
            # write all the paragraphs into the text file
            for paragraph in paragraphs:
                csv_writer.writerow(paragraph.text)
            # csv_writer.writerow("\n")
    # with open("articles2020.txt", "w+",encoding="utf8") as wf:
print("Congrats! Articles downloading has been completed.")
# Now I'm testing on year 2020's articles. When we are actually running the program, we should also do it with 2018 and 2019 articles.




