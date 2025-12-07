import requests
from bs4 import BeautifulSoup
from database import save_product

BASE = "https://books.toscrape.com/"

def scrape_books():
    url = BASE
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    books = soup.select(".product_pod")

    for b in books:
        title = b.h3.a["title"]
        price = b.select_one(".price_color").text.strip()
        stock = b.select_one(".availability").text.strip()
        # The href is often relative to 'catalogue/', so we need to ensure correct URL
        href = b.h3.a["href"]
        if not href.startswith("http"):
            # On homepage, links to books are relative to 'catalogue/'
            if not href.startswith("catalogue/"):
                href = "catalogue/" + href
            product_url = BASE + href
        else:
            product_url = href

        save_product(title, price, stock, product_url)
    
    print("Scraping completed.")
