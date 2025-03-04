import requests
import passwords  # Import credentials from passwords.py

USERNAME = passwords.USERNAME
PASSWORD = passwords.PASSWORD

url = f"http://localhost:8080/basic-auth/{USERNAME}/{PASSWORD}"

response = requests.get(url, auth=(USERNAME, PASSWORD))

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
