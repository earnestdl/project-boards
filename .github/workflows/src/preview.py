import os
from api.github import pulls

# demonstrate that we have access to repo files in 'preview branch'.  
# from here, we can merge following pull requests into preview and rebuild
print('Listing folders in root of branch:')
os.system("ls -l ../../..")

print('\nEnumerating open pull requests:')
for pull in pulls(open):

    print("\nTitle: %s" % (pull['title']))
    print("Number: %s" % (pull['number']))
    print("State: %s" % (pull['state']))
    print("Body: %s" % (pull['body']))
    print("Head Branch:  %s" % (pull['head']['ref']))
    print("Base Branch: %s" % (pull['base']['ref']))
    print("URL: %s" % (pull['url']))

# test for additional pull request from 'pull-requests' branch to 'preview' branch

# make some more changes to test additional PRs
