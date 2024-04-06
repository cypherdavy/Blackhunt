python
# Save this script as find_vulnerabilities.py
# Use Python3
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import PyInquirer

def find_vulnerabilities(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Write your code here to scan for vulnerabilities using multiple programming languages
        # This code will be highly customized based on the specific vulnerabilities you are looking for
        # It could involve scanning for SQL injection, XSS, CSRF, etc.
        # Make sure to handle different programming languages and frameworks properly
        # Be careful with the scanning techniques as some may be illegal in certain contexts

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Ask user for website URL
questions = [
    {
        'type': 'input',
        'name': 'url',
        'message': 'Enter the URL of the website to scan:'
    }
]

answers = PyInquirer.prompt(questions)
website_url = answers['url']

# Validate the URL
parsed_url = urlparse(website_url)
if parsed_url.scheme == '' or parsed_url.netloc == '':
    print("Invalid URL. Please enter a valid URL.")
else:
    find_vulnerabilities(website_url)

