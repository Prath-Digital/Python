import requests
import json
from bs4 import BeautifulSoup

def fetch_webpage():
    url = input("Enter the URL (e.g., http://example.com): ")
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    return response.text

def fetch_api():
    url = input("Enter the API URL (e.g., https://jsonplaceholder.typicode.com/posts): ")
    response = requests.get(url)
    data = json.loads(response.text)
    if data and isinstance(data, list):
        first_post = data[0]
        print(f"Title: {first_post.get('title', 'No title')}")
        print(f"Body: {first_post.get('body', 'No body')}")
    else:
        print("No data found or invalid response.")

def fetch_with_query():
    url = input("Enter the base URL: ")
    query = input("Enter query parameters (e.g., ?search=python): ")
    response = requests.get(url + query)
    print(f"Response: {response.text}")

def parse_html():
    html = input("Enter the HTML content as a string: ")
    soup = BeautifulSoup(html, 'html.parser')
    h1_content = soup.find_all('h1')
    p_content = soup.find_all('p')
    print("h1 content:", [tag.text for tag in h1_content])
    print("p content:", [tag.text for tag in p_content])

def extract_hyperlinks():
    url = input("Enter the webpage URL: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        text = link.text
        print(f"URL: {href}, Text: {text}")

def extract_table():
    url = input("Enter the webpage URL: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    for table in tables:
        headers = [th.text for th in table.find_all('th')]
        rows = [[td.text for td in tr.find_all('td')] for tr in table.find_all('tr')]
        print("Headers:", headers)
        print("Rows:", rows)

def extract_images():
    url = input("Enter the webpage URL: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    for img in images:
        src = img.get('src')
        alt = img.get('alt')
        print(f"Src: {src}, Alt: {alt}")

def extract_section():
    url = input("Enter the webpage URL: ")
    class_name = input("Enter the class name (e.g., content): ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    section = soup.select(f'div.{class_name}')
    for div in section:
        print("Content:", div.text)

def scrape_news():
    url = input("Enter the news/blog URL: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = soup.find_all('article') or soup.find_all('div', class_='post')
    data = []
    for post in posts:
        title = post.find('h2') or post.find('h1')
        link = post.find('a')
        if title and link:
            data.append([title.text, link.get('href')])
    with open('output.csv', 'w') as f:
        for row in data:
            f.write(','.join(row) + '\n')
    print("Data saved to output.csv")

def scrape_product():
    url = input("Enter the product listing URL: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('div', class_='product') or soup.find_all('li')
    for product in products:
        name = product.find('h3') or product.find('a')
        price = product.find('span', class_='price')
        print(f"Name: {name.text if name else 'No name'}, Price: {price.text if price else 'No price'}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Fetch webpage content and status code")
        print("2. Fetch API data and print first post")
        print("3. Fetch with query parameters")
        print("4. Parse HTML and extract h1/p tags")
        print("5. Extract hyperlinks")
        print("6. Extract table data")
        print("7. Extract image tags")
        print("8. Extract specific section")
        print("9. Scrape news/blog posts")
        print("10. Scrape product listing")
        print("0. Exit")
        choice = input("Enter your choice (0-10): ")
        
        if choice == '1':
            fetch_webpage()
        elif choice == '2':
            fetch_api()
        elif choice == '3':
            fetch_with_query()
        elif choice == '4':
            parse_html()
        elif choice == '5':
            extract_hyperlinks()
        elif choice == '6':
            extract_table()
        elif choice == '7':
            extract_images()
        elif choice == '8':
            extract_section()
        elif choice == '9':
            scrape_news()
        elif choice == '10':
            scrape_product()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()