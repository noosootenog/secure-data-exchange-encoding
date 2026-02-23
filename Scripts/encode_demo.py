import base64
import urllib.parse

# Sample data
data = b"Hello, World!"  # Binary data example

# Base64 Encoding
base64_encoded = base64.b64encode(data).decode('utf-8')
print(f"Base64 Encoded: {base64_encoded}")
print(f"Size Increase: Original {len(data)} bytes -> Encoded {len(base64_encoded)} chars (~{round((len(base64_encoded) - len(data)) / len(data) * 100)}%)")

# Hex Encoding
hex_encoded = data.hex()
print(f"Hex Encoded: {hex_encoded}")

# URL Encoding
url_data = "Special chars: <>&?" 

url_encoded = urllib.parse.quote(url_data)
print(f"URL Encoded: {url_encoded}")