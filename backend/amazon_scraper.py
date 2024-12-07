import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.amazon.in"
BASE_HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:132.0) Gecko/20100101 Firefox/132.0",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,application/json",
    "accept-language": "en-US,en;q=0.5",
    "accept-encoding": "gzip, deflate, br, zstd",
}


def scrape_amazon(query):
    product_info = getProductInfo(query)
    return product_info
    
def getProductInfo(query):
    seen_urls = set()
    page_number = 1
    #if query has space replace it with + sign
    query = query.replace(" ", "+")
    search_url = f"https://www.amazon.in/s?k={query}"
    print(search_url)
    try:
        response = requests.get(search_url, headers=BASE_HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        product_count = 0
        products = soup.find("div", attrs={"class": "s-main-slot s-result-list s-search-results sg-row"})

        for product in products.find_all("data-component-type", attrs={"s-search-result"}):
            price = product.find("span", attrs={"class": "a-price-whole"}).get_text(strip=True) if product.find("span", attrs={"class": "a-price-whole"}) else "N/A"
            if price == "N/A":
                continue
            product_link = product.find("a", attrs={"class": "a-link-normal a-text-normal"}).get('href') if product.find("a", attrs={"class": "a-link-normal a-text-normal"}) else "N/A"
            if product_link == "N/A":
                continue
            product_link = BASE_URL + product_link if not product_link.startswith("https://www.amazon.in") else product_link
            if product_link in seen_urls:
                continue
            seen_urls.add(product_link)
            product_count += 1
            if product_count == 15:
                break
            rating_count_text = product.find("span", attrs={"class": "a-size-base"}).get_text(strip=True) if product.find("span", attrs={"class": "a-size-base"}) else "N/A"
            rating_count = ''.join(filter(str.isdigit, rating_count_text)) if rating_count_text != "N/A" else "N/A"
            rating_count = int(rating_count) if rating_count.isdigit() else 0

            avg_rating_text = product.find("span", attrs={"class": "a-icon-alt"}).get_text(strip=True) if product.find("span", attrs={"class": "a-icon-alt"}) else "N/A"
            avg_rating = avg_rating_text.split(" ")[0] if avg_rating_text != "N/A" else "N/A"
            avg_rating = float(avg_rating) if avg_rating.replace(".", "").isdigit() else 0

            product_info = {
               "price": price,
                "rating_count": rating_count,
                "avg_rating": avg_rating,
                "product_name": product.find("span", attrs={"class": "a-text-normal"}).get_text(strip=True) if product.find("span", attrs={"class": "a-text-normal"}) else "N/A",
                "image_url": product.find("img", attrs={"class": "s-image"}).get('src') if product.find("img", attrs={"class": "s-image"}) else "N/A",
                "product_url": product_link,
                "logo": "https://www.amazon.com/favicon.ico"
            }
            return product_info
    except Exception as e:
        print(f"Error fetching product links: {e}")
        return []

def extract_product_info(product_url):
    try:
        response = requests.get(product_url, headers=BASE_HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # item_id = soup.find("div", attrs={"id": "desktop_accordion"}).get('data-csa-c-asin') if soup.find("div", attrs={"id": "desktop_accordion"}) else "N/A"
        # if item_id in seen_ids:
        #     return None
        # if(item_id!="N/A"):
        #     seen_ids.add(item_id)

        rating_count_text = soup.find("span", attrs={"id": "acrCustomerReviewText"}).text if soup.find("span", attrs={"id": "acrCustomerReviewText"}) else "N/A"
        rating_count = ''.join(filter(str.isdigit, rating_count_text)) if rating_count_text != "N/A" else "N/A"
        rating_count = int(rating_count) if rating_count.isdigit() else 0

        avg_rating_text = soup.find("span", attrs={"id": "acrPopover"})["title"] if soup.find("span", attrs={"id": "acrPopover"}) else "N/A"
        avg_rating = avg_rating_text.split(" ")[0] if avg_rating_text != "N/A" else "N/A"
        avg_rating = float(avg_rating) if avg_rating.replace(".", "").isdigit() else 0

        price = soup.select_one('span.a-price-whole').get_text(strip=True) if soup.select_one('span.a-price-whole') else "N/A"
        #change price to int 
        if price == "N/A":
            return None
        
        price = price.replace(",", "")
        price = price.replace(".", "")
        price = int(price) if price.isdigit() else "N/A"
        
        product_info = {
            "price": price,
            "rating_count": rating_count,
            # "item_id": item_id,
            "avg_rating": avg_rating,
            "product_name": soup.find("span", attrs={"id": "productTitle"}).get_text(strip=True) if soup.find("span", attrs={"id": "productTitle"}) else "N/A",
            "image_url": soup.find("img", attrs={"id": "landingImage"}).get('src') if soup.find("img", attrs={"id": "landingImage"}) else "N/A",
            "product_url": soup.find("link", attrs={"rel": "canonical"}).get('href') if soup.find("link", attrs={"rel": "canonical"}) else "N/A",
            "logo": "https://www.amazon.com/favicon.ico"
        }

        return product_info

    except Exception as e:
        print(f"Error extracting product info: {e}")
        return None
