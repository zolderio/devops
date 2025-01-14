import requests
import json

# URL for getting user profile and organizations
url = "https://app.vssps.visualstudio.com/_apis/profile/profiles/me?api-version=7.1"

access_token="" #fill in your access token

# Headers with authentication and content type
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

try:
    # Make the GET request
    response = requests.get(url, headers=headers)
    
    # Check if request was successful
    response.raise_for_status()
    
    # Parse and print the JSON response
    data = response.json()
    
    # Print user profile data
    print("User Profile:")
    print(json.dumps(data, indent=2))
    
    # Get organizations URL from profile response
    orgs_url = "https://app.vssps.visualstudio.com/_apis/accounts?memberId={}?api-version=7.1".format(data['id'])
    
    # Get organizations
    orgs_response = requests.get(orgs_url, headers=headers)
    orgs_response.raise_for_status()
    
    # Print organizations data
    print("\nOrganizations:")
    print(json.dumps(orgs_response.json(), indent=2))
    
    # Get projects for each organization
    orgs_data = orgs_response.json()
    for org in orgs_data:
        org_name = org.get('AccountName')
        print(f"\nProjects for organization {org_name}:")
        
        # Get projects for this organization
        projects_url = f"https://dev.azure.com/{org_name}/_apis/projects?api-version=7.1"
        projects_response = requests.get(projects_url, headers=headers)
        projects_response.raise_for_status()
        
        projects_data = projects_response.json()
        print(json.dumps(projects_data, indent=2))

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")