import requests

req = requests.get("http://127.0.0.1:8000/blog/api/v1/post/5/")

post = req.json()

print(post["title"], post["content"])
