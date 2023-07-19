import requests

parameters = {"limit":3}

response = requests.get("https://fakestoreapi.com/products",params=parameters)


print(response.json())



