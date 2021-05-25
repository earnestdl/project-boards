from ..repo.config import org, name
import os
import requests

api = "https://api.github.com"
token = os.environ.get('token')

def issues():
    url = "%s/repos/%s/%s/issues" % (api,org,name) 
    headers = {'Accept': 'application/vnd.github.v3+json'}
    return get(url,headers)

def reactions(issue):
    url = "%s/repos/%s/%s/issues/%s/reactions" % (api,org,name,issue) 
    headers = {'Accept': 'application/vnd.github.squirrel-girl-preview+json'}
    return get(url,headers)

def cards(column):
    url = "%s/projects/columns/%s/cards" % (api,column) 
    headers = {'Accept': 'application/vnd.github.inertia-preview+json',
                'Authorization': 'Bearer ' + token }
    return get(url,headers)

def add_label(issue):
    url = "%s/repos/%s/%s/issues/%s/labels" % (api,org,name,issue) 
    headers = {'Accept': 'application/vnd.github.v3+json',
                'Authorization': 'Bearer ' + token }
    payload = '{"labels":["needs votes"]}'
    return post(url,headers,payload)


# read data from endpoint
def get(url,headers):
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise requests.ApiError('GET /tasks/ {}'.format(resp.status_code))
    return resp.json()

# write data to endpoint 
def post(url,headers,payload):
    resp = requests.post(url, headers=headers, data=payload)
    if resp.status_code != 200:
        raise requests.ApiError('GET /tasks/ {}'.format(resp.status_code))
    return resp.json()
