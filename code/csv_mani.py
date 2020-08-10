import csv
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import time
# with open ("nei_scrape19.csv",'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')
#     lines = list(csv_reader)
#     for line in lines[(48*15):]:
#         line[0] = "2019-07-31"
#     for line in lines[(48*14):(48*15)]:
#         line[0] = "2019-08-10"
#     for line in lines[(48*13):(48*14)]:
#         line[0] = "2019-08-20"
#     for line in lines[(48*12):(48*13)]:
#         line[0] = "2019-08-31"
#     for line in lines[(48*11):(48*12)]:
#         line[0] = "2019-09-10"
#     for line in lines[(48*10):(48*11)]:
#         line[0] = "2019-09-20"
#     for line in lines[(48*9):(48*10)]:
#         line[0] = "2019-09-30"
#     for line in lines[(48*8):(48*9)]:
#         line[0] = "2019-10-10"
#     for line in lines[(48*7):(48*8)]:
#         line[0] = "2019-10-20"
#     for line in lines[(48*6):(48*7)]:
#         line[0] = "2019-10-31"
#     for line in lines[(48*5):(48*6)]:
#         line[0] = "2019-11-10"       
#     for line in lines[(48*4):(48*5)]:
#         line[0] = "2019-11-20"
#     for line in lines[(48*3):(48*4)]:
#         line[0] = "2019-11-30"
#     for line in lines[(48*2):(48*3)]:
#         line[0] = "2019-12-10"
#     for line in lines[48:(48*2)]:
#         line[0] = "2019-12-20"
#     for line in lines[1:48]:
#         line[0] = "2019-12-31"              

# with open ("nei_scrape19.csv",'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')
#     lines = list(csv_reader)
#     for line in lines[(68*10):741]:
#         line[0] = "2020-01-10"
#     for line in lines[(68*9):(68*10)]:
#         line[0] = "2020-01-20"
#     for line in lines[(68*8):(68*9)]:
#         line[0] = "2020-01-31"
#     for line in lines[(68*7):(68*8)]:
#         line[0] = "2020-02-10"
#     for line in lines[(68*6):(68*7)]:
#         line[0] = "2020-02-20"
#     for line in lines[(68*5):(68*6)]:
#         line[0] = "2020-02-29"       
#     for line in lines[(68*4):(68*5)]:
#         line[0] = "2020-03-10"
#     for line in lines[(68*3):(68*4)]:
#         line[0] = "2020-03-20"
#     for line in lines[(68*2):(68*3)]:
#         line[0] = "2020-03-31"
#     for line in lines[68:(68*2)]:
#         line[0] = "2020-04-10"
#     for line in lines[1:68]:
#         line[0] = "2020-04-20"     

# with open("nei_scrape19_wt.csv",'w') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter='\t')
#     csv_writer.writerows(lines)
    
# text manipulation
with open("articles20.txt", "r") as rf:
    data = rf.read()
with open("articles19.txt","r") as rf:
    data2 = rf.read()
        
data += "\n"
data += data2
with open ("nei_articles.txt", "w") as wf:
    wf.write(data)

# # csv manipulation
# with open("nei_scrape20_wt.csv","r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')
#     lines_qian = list(csv_reader)
#     lines_qian = lines_qian[1:]
# with open("nei_scrape19_wt.csv", "r") as rf:
#     csv_read = csv.reader(rf, delimiter='\t')
#     lines_hou = list(csv_read)
#     lines_hou = lines_hou[1:]

# lines_qian += lines_hou
# with open("nei_scrape_wt.csv","w") as csv_writer:
#     csv_writer = csv.writer(csv_writer, delimiter='\t')
#     csv_writer.writerow(['Year','Headline', 'Link', 'Intro', 'Page'])
#     csv_writer.writerows(lines_qian)

# web-scraping
# with open("hei7.txt", "w+",encoding="utf8") as wf:
#     # create a new text file with the headline as file name
#     # using the link to reach the article page
#     response = requests.get("https://nei.st/medium/caixin/cw900d")
#     # get the page content
#     soup = BeautifulSoup(response.content,'lxml')
#     # find where all the paragraphs are
#     paragraphs = soup.find("article").find_all("p")
#     # write all the paragraphs into the text file
#     for paragraph in paragraphs:
#         wf.write(paragraph.text)
#     wf.write("\n")

        

