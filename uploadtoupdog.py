import requests

url = 'http://10.1.10.176/upload'
proxies = {"http": "http://127.0.0.1:8080"}

file = open("output.sh", "rb")

r = requests.post(url, files = {"form_field_name": file}, proxies=proxies)

