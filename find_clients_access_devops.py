import json
import os
import subprocess
from typing import List, Dict
import requests

def refresh_token_and_check_devops(client_id: str) -> bool:
    """
    Refreshes token for a client and checks if it has DevOps access
    Returns True if the client has DevOps access
    """
    auth_file = os.path.expanduser('.roadtools_auth')
    org = 'acidburn0873'
    project = 'test'
    
    # Run roadtx command
    refresh_command = [
        'roadtx', 'refreshtokento',
        '-c', client_id,
        '-r', '499b84ac-1321-427f-aa17-267ca6975798/.default'
    ]
    
    try:
        # Execute roadtx command
        subprocess.run(refresh_command, check=True, capture_output=True)
        
        # Read the new access token
        with open(auth_file, 'r') as f:
            auth_config = json.load(f)
            access_token = auth_config.get('accessToken')
            
        if not access_token:
            print(f"[!] No access token found for {client_id}")
            return False
            
        # Test DevOps access
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
        # Use the specific endpoint you provided
        url = f"https://dev.azure.com/{org}/{project}/_apis/git/repositories?api-version=7.1"
        print(f"[*] Testing URL: {url}")
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print(f"[+] Success! Client {client_id} has DevOps access")
            # Print the repositories found (optional)
            try:
                repos = response.json()
                print(f"[+] Found {repos.get('count', 0)} repositories")
            except json.JSONDecodeError:
                print("[!] Could not parse repository data")
            return True
        else:
            print(f"[-] Client {client_id} does not have DevOps access (Status: {response.status_code})")
            print(f"[-] Response: {response.text}")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"[!] Error refreshing token for {client_id}: {e}")
        return False
    except Exception as e:
        print(f"[!] Unexpected error for {client_id}: {e}")
        return False

def main():
    # List of client IDs to check
    # Read client IDs from foci.csv
    clients = []
    with open('foci.csv', 'r') as f:
        # Skip header row
        next(f)
        for line in f:
            client_id = line.split(',')[0].strip()
            clients.append(client_id)
    successful_clients = []
    
    print("[*] Starting DevOps access check for all clients...")
    print(f"[*] Testing against organization: zolder")
    print(f"[*] Testing against project: o365 scripts")
    
    for client in clients:
        print(f"\n[*] Testing client: {client}")
        if refresh_token_and_check_devops(client):
            successful_clients.append(client)
    
    print("\n=== Summary ===")
    print(f"Total clients checked: {len(clients)}")
    print(f"Clients with DevOps access: {len(successful_clients)}")
    
    if successful_clients:
        print("\nSuccessful clients:")
        for client in successful_clients:
            print(f"- {client}")
        
        # Save successful clients to file
        with open('devops_capable_clients.txt', 'w') as f:
            for client in successful_clients:
                f.write(f"{client}\n")
        print("\nSuccessful clients have been saved to 'devops_capable_clients.txt'")

if __name__ == '__main__':
    main()