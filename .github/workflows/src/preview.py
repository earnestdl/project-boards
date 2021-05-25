from api.github import pulls

print('\nEnumerating Open Pull Requests:')
for pull in pulls(open):

    number = pull['number']
    print("\nPull Request: %s" % number)
