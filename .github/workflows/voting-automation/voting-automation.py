import os
import requests

org = "earnestdl"
repo = "project-boards"
api = "https://api.github.com"
user = os.environ.get('user')
passwd = os.environ.get('pass')

def get_issues():

    print('\nIssues:')

    url = "%s/repos/%s/%s/issues" % (api,org,repo) 
    headers = {'Accept': 'application/vnd.github.v3+json'}

    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    for issue in resp.json():
        print('number: {} title: {}'.format(issue['number'], issue['title']))


if __name__ == "__main__":
    get_issues()
