import requests
import passwords  # Import credentials

# GitHub API URL for authenticated user
GITHUB_API_URL = "https://api.github.com/user"

# Authenticate using GitHub username and personal access token
response = requests.get(GITHUB_API_URL, auth=(passwords.USERNAME, passwords.TOKEN))

# Check response status
if response.status_code == 200:
    print("Authenticated successfully!")
    print("User Data:", response.json())  # Print user info
else:
    print("Authentication failed:", response.status_code, response.text)
