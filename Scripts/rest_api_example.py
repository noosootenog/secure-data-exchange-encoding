# rest_api_example.py
# This script demonstrates a mock REST API call using Base64 for authentication encoding.
# It uses the requests library to simulate an API request with encoded headers.
# For offline sim, it mocks the response; in real use, replace with actual API.

import base64
import urllib.parse
import requests  # Install if needed: pip install requests (but note: sim only)

# Mock credentials for Basic Auth
username = "testuser"
password = "secretpass"
auth_string = f"{username}:{password}"

# Base64 encode the auth string
base64_auth = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
headers = {
    'Authorization': f'Basic {base64_auth}'
}

# URL encode a query parameter for interoperability demo
query_param = "search=New York & special!"
encoded_query = urllib.parse.urlencode({'q': query_param})

# Simulate REST API call (using httpbin.org for echo response; replace with real endpoint)
api_url = f"https://httpbin.org/get?{encoded_query}"

print("Base64 Encoded Auth Header:", headers['Authorization'])
print("URL Encoded Query:", encoded_query)

# Mock response (since offline sim; in practice, uncomment requests)
mock_response = {
    "headers": headers,
    "args": {"q": query_param},
    "note": "This shows encoding integration with REST protocols like OAuth-style auth."
}
print("\nSimulated API Response:", mock_response)

# Uncomment for real call (requires internet):
# response = requests.get(api_url, headers=headers)
# print("\nReal API Response:", response.json())

print("This illustrates interoperability: Base64 for auth, URL encoding for params in HTTPS APIs.")