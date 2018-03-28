## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}

response = requests.get('https://oauth.reddit.com/r/python/top', headers=headers, params={'t': 'day'})
python_top = response.json()

## 3. Getting the Most Upvoted Post ##

python_top_articles = python_top['data']['children']
upvotes = [(int(article['data']['ups']), article['data']['id']) for article in python_top_articles]

most_upvoted = upvotes[0][1]

## 4. Getting Post Comments ##

response = requests.get('https://oauth.reddit.com/r/python/comments/4b7w9u', headers=headers)

comments = response.json()

## 5. Getting the Most Upvoted Comment ##

comments_list = comments[1]['data']['children']

ups_ids = [(comment['data']['ups'], comment['data']['id']) for comment in comments_list]

most_upvoted_comment = sorted(ups_ids, reverse=True)[0][1]

## 6. Upvoting a Comment ##

payload = {'dir': 1, 'id': 'd16y4ry'}

response = requests.post('https://oauth.reddit.com/api/vote', headers=headers, json=payload)

status = response.status_code