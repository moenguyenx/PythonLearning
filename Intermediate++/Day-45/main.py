from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# url = soup.select_one(selector="p a")
# print(url.get('href'))
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

article_tags = soup.select(selector=".titleline a")

article_texts = [text.getText() for text in article_tags]
article_links = [link.get('href') for link in article_tags]
article_upvote = [int(score.getText().split()[0]) for score in soup.select(selector=".score")]

most_likes = article_upvote.index(max(article_upvote))
text = article_texts[most_likes]
link = article_links[most_likes]

print(text)
print(link)
print(f"{max(article_upvote)} likes")
