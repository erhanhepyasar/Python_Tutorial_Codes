import requests

x = requests.get("http://www.ibb.gov.tr")

print(x.text)