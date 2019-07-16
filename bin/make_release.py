import datetime
import json
import os
import requests


# repository info
repo = "https://api.github.com/repos/shiltemann/training-material/releases"
gh_token = os.environ['GH_TOKEN_RELEASES']


# create release name from today's date
now = datetime.datetime.now()
release_name = str(now.year) + "-" + str(now.month) + "-" + str(now.day)

# prepare the release
release = {
  "tag_name": release_name,
  "target_commitish": "master",
  "name": release_name,
  "body": "Monthly release of the GTN materials",
  "draft": False,
  "prerelease": False
}

# push the release
r = requests.post(repo, json=release, headers={'Authorization': 'token %s' % gh_token})

# print the response
print(r.text)
