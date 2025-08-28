# Web Scraping Guide with Python

## Q1: What is web scraping, and why is it used in Python programming?
Web scraping is the process of automatically extracting data from websites. In Python, it's used due to its powerful libraries like `requests` and `BeautifulSoup`, which make it easy to fetch and parse web content for tasks like data analysis, research, or automation.

## Q2: How is web scraping different from APIs for extracting data from websites?
Web scraping extracts data directly from a website's HTML, often without official access, while APIs provide structured data through a controlled interface. Scraping is more flexible but can be less reliable and may violate terms of service, unlike APIs which are designed for data access.

## Q3: What are the ethical considerations and legal implications of web scraping?
Ethically, scraping should respect website terms, avoid overloading servers, and protect user privacy. Legally, it can breach copyright, terms of service, or data protection laws (e.g., GDPR) if done without permission or excessively.

## Q4: Provide examples of real-world applications where web scraping is commonly used.
- Monitoring prices on e-commerce sites for competitive analysis.
- Gathering news articles for sentiment analysis.
- Collecting job listings for employment trend studies.
- Extracting real estate data for market research.

## Q5: What is the requests library in Python, and what is its primary purpose?
The `requests` library is a Python HTTP library used to send HTTP requests to websites, simplifying the process of fetching web content like HTML pages for scraping or API calls.

## Q6: How do you send an HTTP GET request using the requests library? Provide an example.
You can send a GET request using `requests.get()`. Here's an example:

```python
import requests
response = requests.get('https://example.com')
print(response.text)
```

## Q7: Explain the difference between GET, POST, and DELETE requests in the requests library.
- **GET**: Retrieves data from a server (e.g., `requests.get()`).
- **POST**: Sends data to a server to create/update (e.g., `requests.post()`).
- **DELETE**: Removes data from a server (e.g., `requests.delete()`).

## Q8: How can you handle response status codes (e.g., 200, 404) using the requests library?
Check the `response.status_code` attribute. Example:

```python
import requests
response = requests.get('https://example.com')
if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not found!")
```

## Q9: What is the BeautifulSoup library, and how is it used in web scraping?
BeautifulSoup is a Python library for parsing HTML and XML documents. It's used in web scraping to navigate and extract data from the parsed content using Python code.

## Q10: Explain the purpose of a parser in BeautifulSoup and list commonly used parsers.
A parser in BeautifulSoup converts raw HTML into a navigable structure. Commonly used parsers are:
- `html.parser` (Python's built-in parser).
- `lxml` (fast, external dependency).
- `html5lib` (more lenient, mimics browser parsing).

## Q11: How can you extract specific HTML elements (e.g., <title>, <div>) using BeautifulSoup? Provide an example.
You can use `find()` or `find_all()` with tag names. Example:

```python
from bs4 import BeautifulSoup
html = "<html><title>My Page</title><div>Hello</div></html>"
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('title').text  # Extracts "My Page"
div = soup.find('div').text     # Extracts "Hello"
print(title, div)
```

## Q12: Explain how to use BeautifulSoup to navigate and search the DOM tree for specific data.
Use methods like `find()`, `find_all()`, `.contents`, `.parent`, or `.next_sibling` to navigate. Example:

```python
from bs4 import BeautifulSoup
html = "<div><p>First</p><p>Second</p></div>"
soup = BeautifulSoup(html, 'html.parser')
paragraphs = soup.find_all('p')  # Finds all <p> tags
for p in paragraphs:
    print(p.text)  # Prints "First" and "Second"
```