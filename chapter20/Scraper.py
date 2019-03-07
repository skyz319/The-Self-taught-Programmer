
import urllib.request
from bs4 import BeautifulSoup

class Scraper:

    urlList = []
    def __init__(self, site):
        self.site = site

    def scrape(self):
        # 打开url并发起请求
        r = urllib.request.urlopen(self.site)
        html = r.read()
        # 解析
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)

        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                # print("\n" + url)
                self.urlList.append(str(url))

news = "http://news.baidu.com/"
scraper = Scraper(news)
scraper.scrape()

# 写入文件
with open("urlList.txt", "w") as f:
    for url in scraper.urlList:
        f.write(url + "\n")