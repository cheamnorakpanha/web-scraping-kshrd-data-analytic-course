import re
import requests
from bs4 import BeautifulSoup

url = "https://www.kshrd.com.kh/advanced-course/data-analytics"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

# Basic page information
print("Status code: ", response.status_code)
print("HTML length: ", len(response.text))
print("Contains 'Data Analytics':", "Data Analytics" in response.text)
print("Contains '__NEXT_DATA__':", "__NEXT_DATA__" in response.text)

# Save HTML for manual inspection
with open("page.html", "w", encoding="utf-8") as f:
    f.write(response.text)
    
print("HTML saved to page.html")

soup = BeautifulSoup(response.text, "html.parser")

# Page Title
print("Title: ", soup.title.text)

# Find JavaScript files loaded by the page
print("JavaScript Files:")

for script in soup.find_all("script"):
    src = script.get("src")
    
    if src:
        print(src)
        
# Search for API-like URLsin the HTML
print("Possible API Endpoints: ")

api_patterns = [
    r'/api/[^\s"\']+',
    r'https://[^\s"\']+',
    r'http://[^\s"\']+'
]

found = set()

for pattern in api_patterns:
    matches = re.findall(pattern, response.text)
    
    for match in matches:
        found.add(match)
        
for item in sorted(found):
    print(item)