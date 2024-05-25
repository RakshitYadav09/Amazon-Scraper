from bs4 import BeautifulSoup
import csv

# Load the HTML file
file_path = r'C:\code\Amazon Scraper\Amazon.in_samsung phones.html'  # Update with your file path
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Define the lists to store the extracted data
product_names = []
prices = []
ratings = []
links = []

# Extract product details
for product in soup.select('.s-main-slot .s-result-item'):
    # Extract product name
    name_tag = product.select_one('h2 a span')
    product_name = name_tag.text.strip() if name_tag else ''
    
    # Extract price
    price_tag = product.select_one('.a-price-whole')
    price = price_tag.text.replace(',', '').strip() if price_tag else ''
    
    # Extract rating
    rating_tag = product.select_one('.a-icon-alt')
    rating = rating_tag.text.strip() if rating_tag else ''
    
    # Extract product link
    link_tag = product.select_one('h2 a')
    link = link_tag['href'].strip() if link_tag else ''
    
    # Only add the product if all fields are present
    if product_name and price and rating and link:
        product_names.append(product_name)
        prices.append(price)
        ratings.append(rating)
        links.append(link)

# Combine the data into a list of dictionaries
products = [
    {'product_name': product_names[i], 'price': prices[i], 'rating': ratings[i], 'link': links[i]}
    for i in range(len(product_names))
]

# Define the CSV file path
csv_file_path = r'C:\code\Amazon Scraper\samsung_phones.csv'  # Update with your save path

# Define the headers for the CSV
headers = ['product_name', 'price', 'rating', 'link']

# Write the data to the CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(products)

print(f"Data saved to {csv_file_path}")
