"""
E-Commerce Web Scraper
------------------------
Scrapes product data (title, price, description, rating, review count)
from the webscraper.io test e-commerce site, and saves everything to a CSV file.

This site is specifically built for practicing web scraping, so it's
safe and reliable to use — unlike real e-commerce sites, which often
block bots or load their content with JavaScript.

Requirements (install once):
    pip install requests beautifulsoup4
"""

import csv
import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://webscraper.io/test-sites/e-commerce/allinone"
CATEGORIES = ["computers/laptops", "computers/tablets"]
OUTPUT_FILE = "products.csv"

# Some sites block requests that don't look like they're coming from a
# real browser. Sending a User-Agent header makes our request look more
# like a normal visitor.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}


def get_last_page_number(soup):
    """
    Reads the pagination bar at the bottom of the page (e.g. the links
    numbered 1, 2, 3...) and returns the highest page number found.
    If there's no pagination bar at all, the category only has 1 page.
    """
    page_links = soup.select("ul.pagination li a")
    page_numbers = [int(link.text) for link in page_links if link.text.strip().isdigit()]
    return max(page_numbers) if page_numbers else 1


def scrape_page(category: str, page: int):
    """
    Downloads one page of a category and extracts every product on it.
    Also returns the BeautifulSoup object, so the caller can check the
    pagination bar to know how many pages exist in total.
    """
    url = f"{BASE_URL}/{category}?page={page}"
    # `timeout=15` means: if the server doesn't respond within 15 seconds,
    # give up and raise an error instead of waiting forever. Without this,
    # a single network hiccup can freeze the whole script indefinitely.
    response = requests.get(url, headers=HEADERS, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    product_cards = soup.select(".thumbnail")
    products = []

    for card in product_cards:
        title_tag = card.select_one(".title")
        price_tag = card.select_one(".price")
        description_tag = card.select_one(".description")
        review_count_tag = card.select_one(".ratings p.pull-right")
        rating_tag = card.select_one(".ratings p[data-rating]")

        # .get("title") pulls the *full* product name from the title
        # attribute, since long titles are truncated with "..." in the
        # visible text.
        title = title_tag.get("title", title_tag.text.strip()) if title_tag else "N/A"
        price = price_tag.text.strip() if price_tag else "N/A"
        description = description_tag.text.strip() if description_tag else "N/A"
        review_count = review_count_tag.text.strip() if review_count_tag else "N/A"
        rating = rating_tag.get("data-rating", "N/A") if rating_tag else "N/A"

        products.append({
            "category": category,
            "title": title,
            "price": price,
            "description": description,
            "rating": rating,
            "review_count": review_count,
        })

    return products, soup


def scrape_category(category: str):
    """
    Scrapes every page of a category. The number of pages is read from
    the first page's pagination bar, instead of guessing when to stop.
    """
    all_products = []

    print(f"  Scraping {category} — page 1...")
    products, soup = scrape_page(category, 1)
    all_products.extend(products)

    last_page = get_last_page_number(soup)
    print(f"  ({category} has {last_page} page(s) total)")

    for page in range(2, last_page + 1):
        print(f"  Scraping {category} — page {page}...")
        products, _ = scrape_page(category, page)
        all_products.extend(products)
        time.sleep(1)  # be polite — don't hammer the server with requests

    return all_products


def main():
    all_products = []

    for category in CATEGORIES:
        print(f"Starting category: {category}")
        all_products.extend(scrape_category(category))

    if not all_products:
        print("No products found. Something may have gone wrong.")
        return

    fieldnames = ["category", "title", "price", "description", "rating", "review_count"]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_products)

    print(f"\n✓ Done! Saved {len(all_products)} products to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
