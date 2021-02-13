import os
import requests

org = "earnestdl"
repo = "project-boards"
api = "https://api.github.com"
user = os.environ.get('user')
passwd = os.environ.get('pass')

def issues():

    url = "%s/repos/%s/%s/issues" % (api,org,repo) 
    headers = {'Accept': 'application/vnd.github.v3+json'}

    resp = requests.get(url, headers=headers)

    if resp.status_code != 200:
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))

    return resp.json()

def reactions(issue):

    print('\nReactions:')

    url = "%s/repos/%s/%s/issues/%s/reactions" % (api,org,repo,issue) 
    headers = {'Accept': 'application/vnd.github.squirrel-girl-preview+json'}

    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    for reaction in resp.json():
        print('reaction: {}'.format(reaction['reaction']))



if __name__ == "__main__":

    for issue in issues():
        print('number: {} title: {}'.format(issue['number'], issue['title']))
