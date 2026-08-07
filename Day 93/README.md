# 🕸️ E-Commerce Web Scraper

A Python script that scrapes product data (title, price, description, rating, review count) from an e-commerce test site, and saves everything to a CSV file.

Built as part of the **100 Days of Code** Udemy course assignment (Day 93).

---

## ✨ Features

- Scrapes multiple product categories (laptops, tablets)
- Automatically detects how many pages each category has by reading the pagination bar, instead of guessing
- Pulls each product's full title, price, short description, star rating, and review count
- Sends a browser-like `User-Agent` header and waits between requests to be a polite, well-behaved scraper
- Saves all results into a single, clean `products.csv` file

---

## 🛠 Built With

- Python 3
- [requests](https://pypi.org/project/requests/) — downloads page HTML
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) — parses and searches the HTML

---

## ▶️ How to Run

1. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```
2. Run the script:
   ```bash
   python scraper.py
   ```
3. Find your results in `products.csv`

---

## 🧠 How It Works

1. `get_last_page_number()` reads the pagination bar at the bottom of a category page and returns the highest page number listed — so the script knows exactly when to stop, instead of guessing and potentially looping forever.
2. `scrape_page()` downloads one page, and for every product card found (`.thumbnail`), extracts its title, price, description, rating, and review count.
3. `scrape_category()` scrapes page 1 first, checks how many total pages exist, then loops through the rest.
4. `main()` runs this for every category in `CATEGORIES`, then writes all the collected products to `products.csv`.

---

## 💭 Reflection

*(Fill this in after building — this section is part of the assignment)*

- **How did I approach the project?**
- **What was hard? What was easy?**
- **What would I do differently next time?**
- **Biggest learning from today?**

---

## 📌 Possible Improvements

- Add retry logic for failed requests instead of crashing on the first network hiccup
- Scrape additional categories (phones, etc.)
- Store results directly into a database instead of a CSV
- Add command-line arguments to choose categories without editing the code

---

## 📄 License

Free to use for learning purposes.
