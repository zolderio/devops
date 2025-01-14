import requests
import json
from datetime import datetime, timedelta


organization = "acidburn0873"  # Replace with your organization name
url = f"https://vssps.dev.azure.com/{organization}/_apis/tokens/pats?api-version=7.1-preview.1"
valid_to = (datetime.utcnow() + timedelta(days=30)).isoformat() + 'Z'

# PAT request payload
payload = {
    "displayName": "new_token",
    "scope": "app_token",
    "validTo": valid_to,
    "allOrgs": False
}

access_token="" #fill in your access token

# Headers with authentication and content type
headers = {
    'Authorization': f'Bearer {access_token}',  # Replace your_access_token with the actual token
    'Content-Type': 'application/json'
}

try:
    # Make the POST request
    response = requests.post(url, headers=headers, json=payload)
    
    # Check if request was successful
    response.raise_for_status()
    
    # Parse and print the JSON response
    data = response.json()
    print(json.dumps(data, indent=2))

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")