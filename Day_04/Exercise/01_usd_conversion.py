import requests
# Send a GET request to a free joke API
site = "https://open.er-api.com/v6/latest/USD"
response = requests.get(site)
# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
    # joke = response.json()
    for x,y in data['rates'].items():
        print(x,y)
else:
    print("Failed. Server said:", response.status_code)