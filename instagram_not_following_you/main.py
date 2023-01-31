import json

followers = []

with open('following.json') as file:
    following_json = json.load(file)

for following in following_json['relationships_following']:
    followers.append(following['string_list_data'][0]['value'])

with open('followers.json') as file:
    followers_json = json.load(file)

for follower in followers_json['relationships_followers']:
    profile = follower['string_list_data'][0]['value']
    if profile in followers:
        followers.remove(profile)

for user in sorted(followers):
    print(user)
