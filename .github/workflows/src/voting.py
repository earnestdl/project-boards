from repo.config import col_in_progress
from api.github import cards, reactions, add_label

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
    if uvote == 0 and dvote == 0:
        print("no votes! adding label...")
        add_label(issue)
    if uvote > dvote:
        diff = uvote-dvote
        if diff > 2:
            print("there are 2 more upvotes than downvotes. move to next column!")
    elif dvote > uvote:
        diff = dvote-uvote
        if diff > 2:
            print("there are 2 more downvotes than upvotes. close this issue!")
