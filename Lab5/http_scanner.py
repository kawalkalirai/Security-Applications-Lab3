import requests

# Text for starting scan
print("Starting Scanner")

base_url = "http://localhost:3000"

# Testing Payloads
payloads = ["apple", "banana", "admin", "user"]

# GET Request
print("Testing Search Endpoint..")

for item in payloads:
    # URL I found in part 1 /rest/products/search?q=apple
    full_url = f"{base_url}/rest/products/search?q={item}"
    
    # Sends GET request
    response = requests.get(full_url)
    
    # Summary of results based on the things you asked to log
    print(f"Endpoint: {full_url}")
    print("Method: GET")
    print(f"Payload Used: {item}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Length: {len(response.text)}")
    print("-" * 30)

# POST Request
print("Testing Login Endpoint..")

for item in payloads:
    target = f"{base_url}/rest/user/login"
    
    # Login Information
    credentials = {"email": item, "password": "password123"}
    
    # Sends the POST request
    response = requests.post(target, json=credentials)
    
    # Summary of POST request
    print(f"Endpoint: {target}")
    print("Method: POST")
    print(f"Payload Used: {item}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Length: {len(response.text)}")
    print("-" * 30)
