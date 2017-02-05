import requests

feed_url = "https://localhost:8080/feedPost?x=101010101&y=0"
classify_url = "https://localhost:8080/classifyPost?title=101010101"

r_feed = requests.post(feed_url)
print(dir(r_feed))
print(str(r_feed.content))

r_classify = requests.post(classify_url)
print(dir(r_classify))
print(str(r_classify.content))
