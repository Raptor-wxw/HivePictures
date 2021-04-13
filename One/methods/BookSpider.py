import pymysql
import requests
from bs4 import BeautifulSoup

headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                  '/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image'
              '/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7',
}


def search_list(keyword):
    url = 'https://b-ok.global/s/?q=%s&language=chinese'
    r = requests.get(url % keyword, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    s = soup.find('div', id='searchResultBox')
    for i in s.find_all('table', style="width:100%;height:100%;"):
        # print(i.prettify())
        book_href = i.find('a', style="text-decoration: underline;").attrs['href']   # 书详情链接
        book_name = i.find('a', style="text-decoration: underline;").string    # 书名
        book_author = i.find('a', class_="color1").string  # 作者
        details = i.find('td', style="vertical-align: bottom;")
        book_year = details.find('div', class_="bookProperty property_year").find('div', class_="property_value").string    # 年代
        book_languages = details.find('div', class_="bookProperty property_language").find('div', class_="property_value").string   # 语言
        book_size = details.find('div', class_="bookProperty property__file").find('div', class_="property_value").string   # 大小
        get_detail(book_href)
        return 0


def get_detail(href):
    url = 'https://b-ok.global'
    r = requests.get(url + href, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.prettify())
    download_href = soup.find('a', class_="btn btn-primary dlButton addDownloadedBook").attrs['href']   # 下载链接 （有误）
    # print(download_href)
    recommend_href = soup.find('div', id="bMosaicBox").a.attrs['href']  # 推荐链接
    recommend_image = soup.find('div', id="bMosaicBox").img.attrs['src']    # 推荐封面


search_list('我爱你')
