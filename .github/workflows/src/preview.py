import os
from api.github import pulls

print('\nEnumerating Open Pull Requests:')
for pull in pulls(open):

    os.system("ls -l ../../..")

    print("\nTitle: %s" % (pull['title']))
    print("Number: %s" % (pull['number']))
    print("State: %s" % (pull['state']))
    print("Body: %s" % (pull['body']))
    print("Head Branch:  %s" % (pull['head']['ref']))
    print("Base Branch: %s" % (pull['base']['ref']))
    print("URL: %s" % (pull['url']))

# test for additional pull request from 'pull-requests' branch to 'preview' branch