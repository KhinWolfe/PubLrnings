from bs4 import BeautifulSoup
#import lxml
#soup = BeautifulSoup(contents, "lxml") different form of parsing html type files
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text
article_texts = []
article_links = []

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
for article in articles:
    a_tag = article.find("a")
    a_text = a_tag.getText()
    a_link = a_tag.get("href")
    article_texts.append(a_text)
    article_links.append(a_link)
article_upvotes = [int(score.getText().split()[0])  for score in soup.find_all(name="span", class_="score")]


largest = max(article_upvotes)
print(largest)
idex = article_upvotes.index(largest)
print(idex)

print(article_texts[idex])
print(article_links[idex])









#
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# print(soup.title.string)
#
# print(soup.prettify())

# print(soup.a)
# anchors = soup.find_all(name="a")
# for tag in anchors:
#     print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)
# #
# # company_url = soup.select_one(selector="#name")
# # print(company_url)
#
# heading_again = soup.select(".heading")
# print(heading_again)
