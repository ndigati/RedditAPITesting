import praw
import requests

words = ['i.imgur']
imgur_links = []
image_names = []
user_agent = ("Picture downloading by /u/Crazy_duck28"
              "testing praw")
r = praw.Reddit(user_agent=user_agent)
subreddit = r.get_subreddit(input('Enter name of subreddit: '))
for submission in subreddit.get_hot(limit=10):
    has_imgur = any(string in submission.url for string in words)
    if submission.url not in imgur_links and has_imgur:
        imgur_links.append(submission.url)
        image_names.append(submission.id)

if len(imgur_links) == 0:
    print("Sorry no images found on that subreddits top 10")

i = 0
for url in imgur_links:
    f = open(str(i) + '.jpg', 'wb')
    f.write(requests.get(url).content)
    f.close()
    i += 1


