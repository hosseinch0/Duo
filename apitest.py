import requests

req = requests.get("http://127.0.0.1:8000/blog/api/v1/post/2/")

post = req.json()
print(post)
# print(post["title"], post["content"])
