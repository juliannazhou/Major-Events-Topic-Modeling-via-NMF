import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import csv
import time
# This is the first url that I am going to work with
url='https://nei.st/2020/'
# because we would repeat a lot of operations in web scraping, I made a function to avoid writing the same code again
def yearscrape(url,year):
    # Session helps to persist certain parameters across requests but I didn't use its feature that much
    with requests.Session() as session:
        # whatever the year of news we are scraping, we start from page 1
        page_number = 1
        while True:
            # get the url
            response = session.get(url)
            # get the content of the page
            soup = BeautifulSoup(response.content,'lxml')
            # find all articles in that page
            for article in soup.find_all("article"):
                # get the headline of the article
                headline = article.h2.a.text
                print(headline)
                # get the link of the article
                link = article.find('a')['href']
                print(link)
                # get the intro of the article. Because for some articles the intro part is None, 
                # so I made if-else statement to avoid error in getting p.text
                if article.find('div', class_='entry-summary').p is None:
                    intro = "Please get it online"
                else:
                    intro = article.find('div', class_='entry-summary').p.text
                    print(intro)
                
                print()
                # then write the line of the article with its year, headline, link, intro and page (for tracking and reference) into the csv file
                csv_writer.writerow([year, headline, link, intro, page_number])
                time.sleep(.01)
            
            # get the link into the link of next page
            next_link=soup.find('div', class_="nav-previous")
            # if there's no next page for this year, then stop there
            if next_link is None:
                break
            # change the link of the next page
            url = urljoin(url, next_link.a["href"])
            # adding the page number
            page_number += 1

# open a new file to write in all the information I got about the news articles
with open('nei_scrape.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter='\t')
    # write in the first row
    csv_writer.writerow(['Year','Headline', 'Link', 'Intro', 'Page'])
    # do web scraping by years. For this website the news articles available are only from 2018 to 2020
    yearscrape('https://nei.st/2020/',2020)
    yearscrape('https://nei.st/2019/',2019)
    yearscrape('https://nei.st/2018/',2018)

# What about going into the links of the news and get the whole content as a text file?
with open('nei_scrape.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # skip the first title line
    next(csv_reader)
    # for all the rest of the lines, find each article's headline and link
    for line in csv_file.readlines():
        line = list(line.split("\t"))
        headline = (line[1])
        link = (line[2])
        # create a new text file with the headline as file name
        with open(headline+'.txt', "w") as wf:
            # using the link to reach the article page
            response = requests.get(link)
            # get the page content
            soup = BeautifulSoup(response.content,'lxml')
            # find where all the paragraphs are
            paragraphs = soup.find("article").find_all("p")
            # write all the paragraphs into the text file
            for paragraph in paragraphs:
                wf.write("   " + paragraph.text + "\n")
                

    

