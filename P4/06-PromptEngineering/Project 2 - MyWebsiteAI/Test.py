import requests

# Correct URL (without the extra "https:/")
url = "http://keivan02.pythonanywhere.com/generate"  # Replace with your actual URL

# Include the API key and the query
data = {
    "api_key": "K1ovn39nsfs49mlsg",  # Your API key
    "query": "What is the phone number of Keivan Jamali?"
}

# Send the POST request to the Flask API
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print("API Response:", response.json())
else:
    print("Error:", response.status_code, response.text)
