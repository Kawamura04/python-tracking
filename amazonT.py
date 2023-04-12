import requests
from bs4 import BeautifulSoup

amazonURL = "https://www.amazon.co.jp/%E6%97%A5%E7%AB%8B-%E3%82%AA%E3%83%BC%E3%83%96%E3%83%B3%E3%83%AC%E3%83%B3%E3%82%B8-18L-%E3%83%9B%E3%83%AF%E3%82%A4%E3%83%88HITACHI-MRO-F5Y-W/dp/B08S7F5D54/ref=sr_1_6?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=137QW7P45L489&keywords=%E6%97%A5%E7%AB%8B+%E9%9B%BB%E5%AD%90%E3%83%AC%E3%83%B3%E3%82%B8&qid=1681233637&sprefix=%E6%97%A5%E7%AB%8B+%E9%9B%BB%E5%AD%90%E3%83%AC%E3%83%B3%E3%82%B8%2Caps%2C180&sr=8-6"

def amazonTrackingPrice():
    amazonPage = requests.get(amazonURL)
    soup = BeautifulSoup(amazonPage.content, "html.parser")
    # print(soup)

    title = soup.find(id="productTitle").get_text()
    price = soup.find("span", class_="a-price-whole").get_text()
    convertedPrice = price[1:6].replace(",", "")

    

    print(title)
    print(price)
    print(convertedPrice)
amazonTrackingPrice()