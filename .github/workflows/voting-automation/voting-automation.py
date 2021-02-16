from settings import *
import os
import requests

api = "https://api.github.com"
user = os.environ.get('user')
passwd = os.environ.get('pass')
token = os.environ.get('token')

def issues():
    url = "%s/repos/%s/%s/issues" % (api,org,repo) 
    headers = {'Accept': 'application/vnd.github.v3+json'}
    return request(url,headers)

def reactions(issue):
    url = "%s/repos/%s/%s/issues/%s/reactions" % (api,org,repo,issue) 
    headers = {'Accept': 'application/vnd.github.squirrel-girl-preview+json'}
    return request(url,headers)

def projects():
    url = "%s/repos/%s/%s/projects" % (api,org,repo) 
    headers = {'Accept': 'application/vnd.github.inertia-preview+json',
                'Authorization': 'Bearer ' + token }
    return request(url,headers)
    
def request(url,headers):
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    return resp.json()


if __name__ == "__main__":

    for issue in issues():
        print('number: {}\ntitle: {}'.format(issue['number'], issue['title']))

    print('\n')

    for reaction in reactions(1):    
        print('reaction: {}'.format(reaction['content']))

    print('\n')

    for project in projects():
        print('number: {}\ntitle: {}'.format(project['number'], project['name']))
