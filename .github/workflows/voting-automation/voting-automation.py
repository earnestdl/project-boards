from settings import *
import os
import requests

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
    
def columns(project):
    url = "%s/projects/%s/columns" % (api,project) 
    headers = {'Accept': 'application/vnd.github.inertia-preview+json',
                'Authorization': 'Bearer ' + token }
    return request(url,headers)

def cards(column):
    url = "%s/projects/columns/%s/cards" % (api,column) 
    headers = {'Accept': 'application/vnd.github.inertia-preview+json',
                'Authorization': 'Bearer ' + token }
    return request(url,headers)

def request(url,headers):
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    return resp.json()


if __name__ == "__main__":

    print('\nList cards in the In Progress column:')
    for card in cards(col_in_progress):  

        uvote=0
        dvote=0
        issue = card['content_url'].split('/')[-1]

        print("\nIssue: %s" % issue)

        for reaction in reactions(issue):
            if reaction['content'] == '+1':
                uvote=uvote+1
            elif reaction['content'] == '-1':
                dvote=dvote+1

        print('Upvotes: %d' % uvote)
        print('Downvotes: %d' % dvote)
