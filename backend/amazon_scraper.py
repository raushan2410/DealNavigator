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
    results = []
    product_links = getlinks(query)
    #save the product links in a file 
    with open("product_links.txt", "w") as file:
        for link in product_links:
            file.write(link + "\n")
    
    for link in product_links:
        product_data = extract_product_info(link)
        if product_data:
            results.append(product_data)

    return results
    
def getlinks(query):
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
        product_links = []
        link_count = 0
        for a_tag in soup.find_all("a", attrs={"class": "a-link-normal s-no-outline"}):
            full_url = BASE_URL + a_tag['href'] if "https" not in a_tag['href'] else a_tag['href']
            if full_url not in seen_urls:
                seen_urls.add(full_url)
                product_links.append(full_url)
                link_count += 1
                if link_count == 10:
                    break

        #save the product links in a file
        # with open("product_links.txt", "w") as file:
        #     for link in product_links:
        #         file.write(link + "\n")
        return product_links

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
