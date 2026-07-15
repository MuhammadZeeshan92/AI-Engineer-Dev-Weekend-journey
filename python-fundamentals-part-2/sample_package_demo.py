# ==========================================
# Third-Party Package Example
# ==========================================

import requests

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Successfully connected to GitHub API!")
else:
    print("Request failed.")