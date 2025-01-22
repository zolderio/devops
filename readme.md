
# Azure DevOps Access Testing Scripts

A collection of scripts to go with out blog over at https://zolder.io/ 

## Scripts Overview

### find_clients_access_devops.py
A script that tests multiple client IDs for Azure DevOps access. It:
- Reads client IDs from a `foci.csv` file
- Refreshes authentication tokens for each client
- Tests access to Azure DevOps repositories
- Generates a summary of clients with successful access
- Saves successful clients to `devops_capable_clients.txt`

Key features:
- Token refresh using `roadtx` command
- Azure DevOps API integration
- Detailed logging and error handling
- Batch processing of multiple clients

### get_profile_org_repos.py
A utility script for retrieving Azure DevOps profile and organization information. It:
- Fetches user profile data
- Lists all organizations accessible to the user
- Retrieves projects for each organization
- Provides detailed JSON output of the organizational structure

### make_pat_usingtoken.py
A script for generating Personal Access Tokens (PATs) in Azure DevOps. It:
- Creates a new PAT using an existing access token
- Sets a 30-day validity period
- Configures token scope and display name
- Returns the newly created PAT details

## Prerequisites
- Python 3.x
- Required Python packages:
  - requests
  - json
- Valid Azure DevOps credentials
- RoadTools installed for token refresh functionality

## Usage
1. Ensure all required dependencies are installed
2. Configure the necessary credentials and tokens
3. Run the desired script based on your needs

## Configuration
- Update organization names in respective scripts
- Set appropriate access tokens where required
- Modify API endpoints if necessary

## Output Files
- `devops_capable_clients.txt`: List of clients with successful DevOps access
- `foci.csv`: Input file containing client IDs to test (required for find_clients_access_devops.py)
