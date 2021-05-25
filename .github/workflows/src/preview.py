import os
from api.github import pulls

print('\nEnumerating Open Pull Requests:')
for pull in pulls(open):

    os.system("ls -l ../..")

    print("\nNumber: %s" % (pull['number']))
    print("\nTitle: %s\n" % (pull['title']))
